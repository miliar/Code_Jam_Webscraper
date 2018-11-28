#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <list>
#include <cmath>
#include <cctype>
using namespace std;
#define max(a,b) ((a)>(b)?(a):(b))
int nsc, sc;
int p;
int m[4000];
int prices[2000];
int index[20][2000];
int dp[4010][20];
bool was[4010][20];
int back[2000];
bool getbit(int n, int bit){
	return (n&(1<<bit))!=0;
}
void solvedp(int pos, int ost){
	if (was[pos][ost]) return;
	was[pos][ost]=true;
	if (getbit(pos, p-1)){
		int sootv=back[pos];
		if (ost>=m[sootv] && ost>=m[sootv+1]){
			dp[pos][ost]=0;
		}
		else if (ost+1>=m[sootv] && ost+1>=m[sootv+1]){
			dp[pos][ost]=prices[pos];
		}
		else
			dp[pos][ost]=-1;
	}
	else{
		dp[pos][ost]=-1;
		solvedp(2*pos, ost);
		solvedp(2*pos+1, ost);
		if(dp[2*pos][ost]>=0 &&
			dp[2*pos+1][ost]>=0){
			dp[pos][ost]=dp[2*pos][ost]+dp[2*pos+1][ost];
		}
		solvedp(2*pos, ost+1);
		solvedp(2*pos+1,ost+1);
		if (dp[2*pos][ost+1]>=0 && dp[2*pos+1][ost+1]>=0){
			int tmp=dp[2*pos][ost+1]+dp[2*pos+1][ost+1]+prices[pos];
			if (dp[pos][ost]==-1 || 
				dp[pos][ost]>tmp){
				dp[pos][ost]=tmp;
			}
		}
	}
}
void init(){
	scanf("%d", &p);
	for(int i=0; i<(1<<p);i++){
		scanf("%d", &m[i]);
		m[i]=p-m[i];
	}
	index[p-1][0]=1;
	for(int i=p-1; i>0; i--){
		for(int j=0; j<(1<<(p-1-i)); j++){
			index[i-1][2*j]=2*index[i][j];
			index[i-1][2*j+1]=2*index[i][j]+1;
		}
	}
	for(int i=0;i<(1<<p); i+=2){
		back[index[0][i/2]]=i;
	}
	
	for(int i=0,cnt=(1<<(p-1)); i<p;i++, cnt/=2){
		for(int j=0; j<cnt; j++){
			scanf("%d", &prices[index[i][j]]);
		}
	}
	memset(was, 0, sizeof(was));
	solvedp(1, 0);
	printf("Case #%d: %d\n", sc, dp[1][0]);
}
void solve(){
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &nsc);
	for(sc=1; sc<=nsc; sc++){
		init();
		solve();
	}
	return 0;
}