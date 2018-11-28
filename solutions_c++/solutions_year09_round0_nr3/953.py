#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const char *p="welcome to code jam";
char s[502];
int dp[502][22];

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i,j,k;
	scanf("%d",&n);
	gets(s);
	for(k=0;k<n;k++){
		gets(s);
		int l=strlen(s);
		memset(dp,0,sizeof(dp));
		for(i=0;i<=l;i++)dp[i][0]=1;
		for(i=1;i<=l;i++)
			for(j=1;j<=19;j++){
				dp[i][j]+=dp[i-1][j];
				dp[i][j]+=(s[i-1]==p[j-1])*dp[i-1][j-1];
				dp[i][j]%=10000;
			}
		printf("Case #%d: %04d\n",k+1,dp[l][19]);
	}
	return 0;
}
