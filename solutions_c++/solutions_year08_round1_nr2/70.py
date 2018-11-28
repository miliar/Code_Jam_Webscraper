#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#define MAXN 2050

using namespace std;

int jmlcase;
int n,jmlcostumer;
int a,b,c,d,e,f;
int answer;
int ada;
int warna;
int jml;
int hahahihi;
int dipake[MAXN];

void gadajawab(void) {
	printf(" IMPOSSIBLE\n");
	}

int main() {
	
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
		printf("Case #%d:",e + 1);
		scanf("%d%d",&n,&jmlcostumer);
		vector<int> like[MAXN];
		vector<int> malt[MAXN];
		vector<int> die[MAXN];
		for (a = 0;a < jmlcostumer;a++) {
			scanf("%d",&b);
			for (c = 0;c < b;c++) {
				scanf("%d%d",&d,&f);
				like[a].push_back(d);
				malt[a].push_back(f);
				die[a].push_back(0);
				}
			}
		answer = 0;
		int solocarer;
		hahahihi = 1;
		memset(dipake,0,sizeof(dipake));
		while (1) {
			solocarer = -1;	
			for (a = 0;a < jmlcostumer;a++) {
				ada = 0;
				jml = 0;
				warna = -1;
				for (b = 0;b < like[a].size();b++) {
					if (die[a][b]) continue;
					ada++;
					if (malt[a][b] && dipake[like[a][b]]) continue;
					if (malt[a][b]) warna = like[a][b];
					}
				if (!ada) {
					hahahihi = 0;
					gadajawab();
					break;
					}
				if (ada == 1 && warna != -1) {
					solocarer = warna;
					}
				}
			if (!ada) break;
			if (solocarer == -1) break;
			warna = solocarer;
			answer++;
			dipake[warna] = 1;
			for (a = 0;a < jmlcostumer;a++) {
				for (b = 0;b < like[a].size();b++) {
					if (like[a][b] == warna && !malt[a][b]) die[a][b] = 1;
					}
				}
			}
		if (hahahihi) {
			for (a = 1;a <= n;a++) {
				printf(" %d",dipake[a]);
				}
			printf("\n");
			}
		}			

	
	return 0;
	}

