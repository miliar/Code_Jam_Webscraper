//RPI
//Author : Sushant Bhatia
#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<iomanip>
#include<cmath>
#include<cstring>
#define FOR(i,j,k) for(i = j;i < k;i++)
#define RFOR(i,j,k) for(i = k-1;i >= j;i--)
#define LL long long
#define GET(x) scanf("%d",&x)
#define OUT(x) printf("%d\n",x)
#define SET(x) memset(x,0,sizeof(x))
#define S(x) x.size()
bool comp(int i,int j){ return i > j; }
using namespace std;
char a[105][105];
int to[105];
int w[105];
double wp[105], owp[105],oowp[105];
int main(){
	int t,n;
	double an;
	int i,j;
	GET(t);
	int c;
	double sm,opp,tot,wn;
	FOR(c,1,t+1){
		printf("Case #%d:\n",c);
		GET(n);
		SET(to);SET(w);
		FOR(i,0,n) scanf("%s",a[i]);
		FOR(i,0,n){
			FOR(j,0,n){
				if(a[i][j] != '.'){
					if(a[i][j] == '1')
						w[i]++;
					to[i]++;
				}
			}
			wp[i] = (double)w[i]/to[i];
			//cout<<wp[i]<<"  ";
		}
		//cout<<endl;
		FOR(i,0,n){
			opp = 0;
			sm = 0;
			FOR(j,0,n){
				if(i == j || a[i][j] == '.') continue;
				tot = to[j]-1;
				wn = w[j];
				if(a[i][j] == '0') wn--;
				opp += 1;
				sm += (wn/tot);
			}
			owp[i] = sm/opp;
			//cout<<owp[i]<<" ";
		}
		//cout<<endl;
		FOR(i,0,n){
			opp = sm = 0;
			FOR(j,0,n){
				if(i == j || a[i][j] == '.') continue;
				sm += owp[j];
				opp += 1;
			}
			oowp[i] = (sm/opp);
		}
		FOR(i,0,n){
			an = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
			cout<<setprecision(14)<<an<<endl;
		}
	}
	return 0;
}
	
