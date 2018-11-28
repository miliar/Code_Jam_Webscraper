#include <stdio.h>
#include <algorithm>
#include <set>
#define MAXN 3000 

//#define DEBUG

using namespace std;

int table[MAXN*2+1][MAXN*2+1];
set<int> x[MAXN*2+1];
set<int> y[MAXN*2+1];

int main()
{
	int icase, ncase;
	int n = MAXN;
	char cmd[33];
	int L, T;
	int i, j, k, l;
	int cx, cy, dir;
	set<int>::iterator t, s;
	int ans;

	scanf("%d", &ncase);
	for(icase=0; icase<ncase; ++icase){
		for(i=0; i<n*2+1; ++i){
			x[i].clear();
			y[i].clear();
		}

		scanf("%d", &L);
		cx = cy = dir = 0;
		for(k=0; k<L; ++k){
			scanf("%s%d", cmd, &T);
			while(T--){
				for(i=0; cmd[i]; ++i){
					if(cmd[i] == 'R')
						dir = (dir + 1) % 4;
					else if(cmd[i] == 'L')
						dir = (dir + 3) % 4;
					else if(cmd[i] == 'F'){
						if(dir == 0)
							y[MAXN + (cy++)].insert(cx);
						else if(dir == 1)
							x[MAXN + (cx++)].insert(cy);
						else if(dir == 2)
							y[MAXN + (--cy)].insert(cx);
						else if(dir == 3)
							x[MAXN + (--cx)].insert(cy);
					}
					else
						fprintf(stderr, "how could this be possible\n");
				}
			}
		}
		for(i=0; i<n*2+1; ++i)
			for(j=0; j<n*2+1; ++j)
				table[i][j] = 0;
		/*
		for(i=0; i<n; ++i){
			for(t=x[i].begin(); t != x[i].end(); ++t)
				fprintf(stderr, "%d ", *t);
			fprintf(stderr, "\n");
		}
		*/
		for(i=0; i<n*2+1; ++i){
			if(x[i].begin() != x[i].end()){
				for(t= ++x[i].begin(); t != x[i].end(); ++t){
					s = t;
					++t;
					if(t == x[i].end())
						break;
					for(k=*s; k<*t; ++k){
						table[i][k+MAXN] = 1;	
					}
				}
			}
			if(y[i].begin() != y[i].end()){
				for(t=++y[i].begin(); t != y[i].end(); ++t){
					s = t;
					++t;
					if(t == y[i].end())
						break;
					for(k=*s; k<*t; ++k){
						table[k+MAXN][i] = 1;
					}
				}
			}
		}
		ans = 0;
		for(i=0; i<n*2+1; ++i)
			for(j=0; j<n*2+1; ++j)
				if(table[i][j])
					++ans;

#ifdef DEBUG
		for(i=n-1; i>=0; --i)
			for(j=0; j<n; ++j)
				fprintf(stderr, "%d ", table[i][j]);
#endif
		printf("Case #%d: %d\n", icase+1, ans);
	}
	return 0;
}
