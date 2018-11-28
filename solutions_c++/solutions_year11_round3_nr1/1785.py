#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define equal(a,b) (ABS((a)-(b))<eps)
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pair pair<int,int>
#define MAX 52
using namespace std;
char s[MAX][MAX];
int dp[MAX][MAX];
int main(){
	string filename, fileword;
	fileword = "A";
	filename = fileword;
	filename = fileword+"-small-attempt1";
	filename = fileword+"-large";
	freopen((filename+".in").c_str(),"r",stdin);
	freopen((filename+".out").c_str(),"w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		printf("Case #%d:\n",t);
		int R,C;
		scanf("%d %d",&R,&C);
		memset(dp,0,sizeof(dp));
		int count=0;
		for(int i=0; i<R; i++) scanf("%s",s[i]);
		for(int i=1; i<=R; i++)
		for(int j=1; j<=C; j++){
			if(s[i-1][j-1]=='#') {
				int mn=min(dp[i-1][j-1],min(dp[i][j-1],dp[i-1][j]));
				int mx=max(dp[i-1][j-1],max(dp[i][j-1],dp[i-1][j]));
				if(mn==1) {
					if(mx==2)
						dp[i][j]=1;
					else
						dp[i][j]=2;
				}
				else {
					dp[i][j]=1;
				}
				count++;
			}
			else dp[i][j]=0;
		}
		for(int i=1; i<=R; i++)
		for(int j=1; j<=C; j++){	
			if(dp[i][j]%2==0&&dp[i][j]>0) {
				s[i-2][j-2]='/'; s[i-2][j-1]='\\';
				s[i-1][j-2]='\\'; s[i-1][j-1]='/';
				if(dp[i][j+1]%2==0) dp[i][j+1]=0;
				if(dp[i+1][j+1]%2==0) dp[i+1][j+1]=0;
				if(dp[i+1][j]%2==0) dp[i+1][j]=0;
				count-=4;
			}
		}
		if(count!=0) printf("Impossible\n");
		else{
			for(int j=0; j<R; j++){
				printf("%s\n",s[j]);
			}
		}
	}
	//system("pause");
	return 0;
}
