#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <fstream>
#include <numeric>
#include <map>
#include <iterator>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define INF 99999999
#define EPS 1e-7
#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)
#define REP(i,n) for(i=0; i<(n); i++)
#define FOR(i,a,b) for(i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()


#define SIZE 100+10
#define IN freopen("A-large.in","r",stdin);
#define OUT freopen("out","w",stdout);

int T,N,win[SIZE],tot[SIZE];
char table[SIZE][SIZE];
double WP[SIZE],OWP[SIZE],OOWP[SIZE];

int main()
{
	IN
	OUT
	int t,i,j;
	double tmp;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d:\n",t);
		scanf("%d",&N);
		REP(i,N) scanf("%s",table[i]);
		memset(win,0,sizeof(win));
		memset(tot,0,sizeof(tot));
		
		REP(i,N){
			
			REP(j,N){
				if(table[i][j] == '.') continue;
				if(table[i][j] == '1') win[i]++;
				tot[i]++;
			}
			WP[i] = win[i]/(tot[i]*1.0);
			//printf("WP[%d]: %lf\n",i,WP[i]);
		}
		
		REP(i,N){
			tmp = 0;
			REP(j,N){
				if(table[i][j] == '.') continue;
				if(table[j][i] == '1'){
					tmp += (win[j]-1)/(1.0*tot[j]-1);
				}else{
					tmp += win[j]/(1.0*tot[j]-1);
				}
				//printf("%.6lf\n",tmp);
			}
			OWP[i] = tmp/tot[i];
			//printf("%.6lf/%d ... OWP[%d]: %lf\n",tmp,tot[i],i,OWP[i]);
		}
		
		REP(i,N){
			tmp = 0;
			REP(j,N){
				if(table[i][j] == '.') continue;
				tmp += OWP[j];
			}
			OOWP[i] = tmp/tot[i];
			//printf("%lf OOWP[%d]: %lf\n",tmp,i,OOWP[i]);
		}
		double rank;
		REP(i,N){
			rank = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			printf("%.12g\n",rank);
		}
		
	}
	return 0;
}

