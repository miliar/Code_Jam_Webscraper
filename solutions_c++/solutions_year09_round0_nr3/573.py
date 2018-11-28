//poj 

#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<vector>
#include<set>
#include<queue>

using namespace std;
typedef long long llt;

#define maxv 510

#define LEN 19
#define myAbs(x) ((x)>=0?(x):-(x))
#define Max(x,y) ((x)>(y)?(x):(y))
#define Min(x,y) ((x)<(y)?(x):(y))
#define inf 1999999999
#define MOD 10000
#define eps 1e-8
#define EPS 1e-8
#define M_PI 3.14159265358979323846



char str[maxv];
int slen;
int ttt;
int dp[maxv][LEN+1];
char wel[]="welcome to code jam";

void solve(){
	int i,j,k;
	int res;
	gets(str);
	slen=strlen(str);
	//str[slen++]='a';
	
	dp[0][0]=1;
	for(i=1;i<=LEN;++i){
		dp[0][i]=0;
	}
	for(i=1;i<=slen;++i){
		dp[i][0]=dp[i-1][0];
		for(j=1;j<=LEN;++j){
			dp[i][j]=dp[i-1][j];
			//dp[i][j]=0;
			if(str[i-1]==wel[j-1]){/*
				for(k=0;k<i;++k){
					dp[i][j]+=dp[k][j-1];
				}*/
				dp[i][j]+=dp[i-1][j-1];
				dp[i][j]%=MOD;
				//printf("add %d %d\n",i,j);
			}
		}
	}
	res=0;/*
	for(i=0;i<=slen;++i){
		//printf("%d %d\n",i,dp[i][LEN-1]);
		res+=dp[i][LEN];
	}*/
	res= dp[slen][LEN];
	res%=MOD;
	printf("Case #%d: ",++ttt);
	printf("%04d\n",res);
}
int main(){
	//freopen("out.txt","w",stdout);
	ttt=0;
	int t;
	scanf("%d",&t);
	while(getchar()!='\n');
	while(--t>=0)
		solve();
	//system("PAUSE");
	return 0;
}



/*
100
oeoooamjeccoomdoottwlh
wwelocome to codde jamm
wwelocome to codde jammx
wwelocome to codde jamm
welcome to code jamm
100
oeoooamjeccoomdoottwlh
wwelocome to codde jamm
*/
