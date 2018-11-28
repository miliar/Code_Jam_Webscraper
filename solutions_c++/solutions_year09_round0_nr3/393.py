#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int dp[510][20];
char patter[]="welcome to code jam";
int len=0;

int solve(char str[],int x,int y)
{
	if(dp[x][y]!=-1) return dp[x][y];
	if(y==19) return 1;
	if(x==len) return 0;
	
	int ret=0;
	if(str[x] == patter[y])
		ret+=solve(str,x+1,y+1);
	ret+=solve(str,x+1,y);
	ret%=10000;
	return dp[x][y]=ret;
}
int main()
{
	freopen("cin.txt","r",stdin);
	freopen("cout.txt","w",stdout);

	int times;
	scanf("%d",&times);
	getchar();
	int count;
	char str[510];
	for(count=1;count<=times;count++)
	{
		gets(str);
//		printf("%s\n",str);
//		getchar();
		len=strlen(str);

		memset(dp,-1,sizeof(dp));
		int ret=solve(str,0,0);

		printf("Case #%d: %04d\n",count,ret);
	}
}