#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

int gg[105][105];
int clr[105];
int dt[105][30];
int n, k, maxcolor;
int dgr, dgrpos, maxdgr;

void coloring(int next)
{
	int i;
	int plt[105];

	for(i=0; i<n; i++) plt[i] = 0;

	for(i=0; i<n; i++) {
		if(gg[next][i] && clr[i] >= 0) {
			plt[clr[i]] = 1;
		}
	}	

	for(i=0; i<n; i++) {
		if(plt[i] == 0) break;
	}

	if(i > maxcolor) maxcolor = i;

	clr[next] = i;

}

int overlay(int c1, int c2)		// c1[0] > c2[0]
{
	int i;
	for(i=0; i<k; i++) {
		if(dt[c1][i] <= dt[c2][i]) return 1;
	}
	return 0;
}

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	//freopen("input.txt", "r", stdin);

	int i, j, tt, cas, now, judge, sol;
	scanf("%d\n",&cas);

	for(now = 1; now <= cas; now++) {
		printf("Case #%d: ",now);
		scanf("%d %d\n",&n,&k);
	
		for(i=0; i<n; i++) {
			clr[i] = -1;
			for(j=0; j<k; j++) {
				scanf("%d",&dt[i][j]);
			}
		}

		for(i=0; i<n; i++) {
			for(j=0; j<n; j++) {
				gg[i][j] = 0;
			}
		}

		for(i=0; i<n; i++) {
			for(j=i+1; j<n; j++) {
				if(dt[i][0] > dt[j][0]) judge = overlay(i, j);
				else judge = overlay(j, i);

				if(judge) {
					gg[i][j] = gg[j][i] = 1;
				}
			}
		}		

		maxcolor = -1;

		while(1) {			// graph coloring
			maxdgr = -1;
			dgrpos = -1;
			for(i=0; i<n; i++){
				dgr = 0;
				if(clr[i] >= 0) continue;
				for(j=0; j<n; j++) {
					if(gg[i][j]) dgr++;
				}
				if(dgr > maxdgr) {
					maxdgr = dgr;
					dgrpos = i;
				}
			}

			if(maxdgr == -1) break;
			else coloring(dgrpos);
		}
		

		
// 
// 		for(i=0; i<n; i++){
// 			if(clr[i] == -1) dfs_color(0);
// 		}

		printf("%d\n",maxcolor+1);
	}

	return 0;
}