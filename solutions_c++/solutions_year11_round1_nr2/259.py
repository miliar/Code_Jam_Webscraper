#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAXL 11
#define MAXN 10005

struct Word {
	char w[MAXL];
	int orgIndex;
	int loss;
} dict[MAXL][MAXN];

int ct[MAXL];

//char dict[MAXN][MAXL];
int n,m;
char list[30];
char res[MAXL];

bool f[MAXN];

void process() {
	int i,j,L,k,a,b,rem;
	char pos[MAXL];
	bool flag;
	bool ff[30];
	
	for(i=1;i<MAXL;i++) {
		rep(j, ct[i]) dict[i][j].loss = 0;
	}
	L = strlen(list);
	for(i=1;i<MAXL;i++) {
		if(ct[i] <= 1) continue;
		rep(j, ct[i]) { //cur word
			rep(k, ct[i]) f[k] = 1;
			rem = ct[i];
			rep(k,L) {
				memset(ff,0,sizeof(ff));
				rep(a, ct[i]) if(f[a]) {
					rep(b, i) ff[ dict[i][a].w[b]-'a'] = 1;
				}
				if(ff[ list[k]-'a'] == 0) continue;
				memset(pos,0,sizeof(pos));
				flag = 0;
				rep(a, i) {
					if(dict[i][j].w[a] == list[k]) { pos[a] = 1; flag = 1; }
				}
				if(!flag) dict[i][j].loss++;
				rep(a, ct[i]) if(f[a]) {
					rep(b, i) {
						if(dict[i][a].w[b] == list[k] && pos[b] == 0) { f[a] = 0; rem--; break; }
						if(dict[i][a].w[b] != list[k] && pos[b] == 1) { f[a] = 0; rem--; break; }
					}
				}
				if(rem <= 1) break;
			}
		}
	}

	int mxloss = -1, orgI = -1;
	for(i=1;i<MAXL;i++) {
		rep(j, ct[i]) {
			if(dict[i][j].loss > mxloss) {
				mxloss = dict[i][j].loss;
				strcpy(res, dict[i][j].w);
				orgI = dict[i][j].orgIndex;
			}
			else if(dict[i][j].loss == mxloss) {
				if(dict[i][j].orgIndex < orgI) {
					orgI = dict[i][j].orgIndex;
					strcpy(res, dict[i][j].w);
				}
			}
		}
	}
}

int main() {
	int T,kase=1;
	int i;
	char s[MAXL];
	int L;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d:",kase++);
		scanf(" %d %d",&n,&m);
		memset(ct,0,sizeof(ct));
		rep(i,n) {
			scanf(" %s", s);
			L = strlen(s);
			strcpy(dict[L][ct[L]].w,s);
			dict[L][ct[L]++].orgIndex = i;
		}

		rep(i,m) {
			scanf(" %s",list);
			process();
			printf(" %s",res);
		}
		printf("\n");
	}
	return 0;
}