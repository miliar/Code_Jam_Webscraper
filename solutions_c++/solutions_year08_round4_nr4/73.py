#include <iostream>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(a,b,c) for(int a=b;a<=c;a++)
char str[50999];
int tab[20],k,n;

int ms[20][20],ost[20][20];

inline char on_pos(int x){
	return str[(x/k)*k+tab[x%k]];
}

int dp[17][1<<16][17];

int go(int mask,int prev,int first){
	int &res = dp[first][mask][prev];
	if( res != -1 )return res;
	res = 0;
	if( mask == ((1<<k)-1) )return res = ost[first][prev];
	else{
		REP(i,k)if( ((mask>>i)&1)==0 ){
			res >?= go(mask|(1<<i),i,first)+ms[prev][i];
		}
	}
	return res;
}

int main(){
	int d;
	scanf("%d",&d);
	REP(test,d){
		scanf("%d %s",&k,str);
		n = strlen(str);
		memset(ms,0,sizeof(ms));
		memset(ost,0,sizeof(ost));
		memset(dp,-1,sizeof(dp));

		REP(i,n/k){
			int pos = i*k;
			REP(j,k)FOR(q,j+1,k-1)if( str[pos+j]==str[pos+q] ){
				ms[j][q]++;
				ms[q][j]++;
			}
			if( pos+k < n ){
				REP(j,k)REP(q,k)if( str[pos+j]==str[pos+k+q] ){
					ost[q][j]++;
				}
			}
		}
		int res = 1000000;
		REP(i,k){
			res <?= n-go(1<<i,i,i);
		}
		printf("Case #%d: %d\n",test+1,res);
	}
	return 0;
}
