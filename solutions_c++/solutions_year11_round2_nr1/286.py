#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int N = 110;
char tab[N][N];
double gp[N];
double gw[N];
double wp[N];
double owp[N];
double oowp[N];
int n;

main(){
	int q;
	scanf("%d",&q);
	REP(w,q){
		scanf("%d",&n);
		REP(i,n) gp[i] = gw[i] = wp[i] = owp[i]=oowp[i] = 0.0;
		REP(i,n)
			scanf("%s",tab[i]);
		REP(i,n){
			REP(j,n){
				if(tab[i][j] == '1'){
					gp[i]++;
					gp[j]++;
					gw[i]++;
				}
				else if(tab[i][j] == '0'){
					gp[i]++;
					gp[j]++;					
					gw[j]++;
				}
			}
		}
		REP(i,n){
			gp[i]/=2;
			gw[i]/=2;
		}
		REP(i,n){
			wp[i] = gw[i] / gp[i];
		}
		REP(i,n){
			owp[i] = 0;
			int ile =0 ;
			REP(j,n){
				if(j != i){
					if(tab[i][j] == '1' || tab[i][j] == '0'){
						if(tab[i][j] == '1')
							owp[i] += (gw[j] / (gp[j] - 1));
						else
							owp[i] += ((gw[j] - 1) / (gp[j] - 1));
						ile++;
					}
				}
			}
			owp[i] = owp[i]/ile;
		}
		REP(i,n){
			oowp[i] = 0;
			int ile = 0;
			REP(j,n){
				if(j != i){
					if(tab[i][j] == '0' || tab[i][j]=='1')oowp[i] += owp[j],ile++;
				}
			}
			oowp[i] = oowp[i]/ile;
		}
		printf("Case #%d:\n",w+1);
		REP(i,n){
			printf("%.10lf\n",0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
		}
	}
}
