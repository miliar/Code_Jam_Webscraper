#include<cstdio>
#include<vector>
#include<list>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<time.h>
#include<iostream>
#include<map>
#include<set>
using namespace std;
#define REP(i,n) for(int i=0;i<(n); ++i)
#define FOREACH(it,V) for(typeof((V).begin()) it = (V).begin(); it!=(V).end(); ++it)
char c[1000][1000];
double WP[1000],OWP[1000],OOWP[1000],WPP[1000];
int main(){
	double res;
	int n, z, cnt; scanf("%d", &z); REP(jj,z) {
		scanf("%d", &n);
		REP(i,n) scanf("%s", c[i]);
		printf("Case #%d:\n", jj+1);
		REP(i,n){
			WP[i] = 0;
			cnt = 0;
			REP(j,n) if(c[i][j]!='.'){if(c[i][j]=='1') WP[i] += 1;  ++cnt;}
			WP[i]/=cnt;
		}
		//printf("debug\n"); REP(i,n) printf("%lf ", WP[i]); printf("\n");
		REP(ii,n){
			REP(i,n){
				WPP[i] = 0;
				cnt = 0;
				REP(j,n) if(c[i][j]!='.'&&j!=ii) {if(c[i][j]=='1') WPP[i] += 1; ++cnt;}
				WPP[i]/=cnt;
			}
			OWP[ii] = 0;
			cnt = 0;
			REP(j,n) if(c[ii][j]!='.'){
				OWP[ii] += WPP[j];
				++cnt;
				}
				OWP[ii]/=cnt;
		
		
		}
		//printf("debug\n"); REP(i,n) printf("%lf ", OWP[i]); printf("\n");
		REP(i,n){
			OOWP[i] = 0;
			cnt = 0;
			REP(j,n) if(i!=j&&c[i][j]!='.') { OOWP[i] += OWP[j]; ++cnt; }
			OOWP[i] /= cnt;
		}
		//printf("debug\n"); REP(i,n) printf("%lf ", OOWP[i]); printf("\n");
		REP(i,n){
			double rpi = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			printf("%.9lf\n", rpi);
		}
	}
	return 0;
}

