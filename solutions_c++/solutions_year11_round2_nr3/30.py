#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cctype>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

int n,m;

vector<int> g[4444];
vector<bool> v[4444];
int col[11111];
int a[11111], b[11111];
bool cv[11111];

void ae(int i, int j){
	g[i].PB(j);
	v[i].PB(false);
	//g[j].PB(i);
	//v[j].PB(false);
}

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d%d", &n, &m);
	FOR(i,0,n){
		g[i].clear();
		v[i].clear();
		col[i] = -1;
	}
	FOR(i,0,n){
		ae(i, (i+1)%n);
	}
	FOR(i,0,m)scanf("%d", &a[i]);
	FOR(i,0,m)scanf("%d", &b[i]);
	FOR(i,0,m){
		ae(a[i]-1,b[i]-1);
		ae(b[i]-1,a[i]-1);
	}
	FOR(i,0,n){
		FOR(j,0,g[i].size())g[i][j]=(i-g[i][j]+n)%n;
		sort(g[i].begin(), g[i].end());
		FOR(j,0,g[i].size())g[i][j]=(i-g[i][j]+n)%n;
		//FOR(j,0,g[i].size())printf(" - %d", g[i][j]); printf("\n");
	}
	
	int msz = (1<<20);
	FOR(it,0,2){
		FOR(i,0,n)FOR(j0,0,g[i].size())v[i][j0] = false;

		FOR(i,0,n)FOR(j0,0,g[i].size())if(!v[i][j0]){
			if(it==1){
				memset(cv,0,sizeof(bool)*msz);
			}
			vector<int> kv;
			{
				int c = i, cj0 = j0;
				int sz = 0;
				int lcol = 0;
				while(!v[c][cj0]){
					
					if(it==1){
						if(col[c]>=0)cv[col[c]] = true;
						kv.PB(c);
					}
					//if(it==0)printf(" %d", c);
					v[c][cj0] = true;
					int j = g[c][cj0];
					int md = 0, kk=-1;
					FOR(k0,0,g[j].size()){
						int k = g[j][k0];
						//if(k == (j+n-1)%n)continue;
						int d = (k-c+n)%n;
						if(d>md){
							md = d;
							kk = k0;
						}
					}
					c = j;
					cj0 = kk;
					sz++;
				}
				//if(it==0)printf("\n");
				if(it==0){
					msz = min(msz, sz);
				}
			}

			if(it==1){
				FOR(c0,0,kv.size()){
					int c = kv[c0];
					int cp = kv[(c0+kv.size()-1)%kv.size()];
					int cn = kv[(c0+1)%kv.size()];

					if(col[c]<0){
						FOR(q,0,msz)if(!cv[q] && q!=col[cp] && q!=col[cn]){
							col[c] = q;
							cv[q]=true;
							break;
						}
						if(col[c]<0){
							col[c]=0;
							FOR(q,0,msz)if(q!=col[cp] && q!=col[cn]){
								col[c] = q;
								cv[q]=true;
								break;
							}
						}
					}
				}
				FOR(q,0,msz)if(!cv[q]){
					//printf("BAD!\n");
					break;
				}
			}

		}
	}

	printf("Case #%d: %d\n", ++tt, msz);
	FOR(i,0,n){
		if(i)printf(" ");
		printf("%d", col[i]+1);
	}
	printf("\n");
}
	return 0;
}


