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

int arr[510][20];
char str[]="welcome to code jam";
int len=0;

int solve(char *s,int i,int j)
{
	if(arr[i][j]!=-1) 
		return arr[i][j];
	if(j == 19) 
		return 1;
	if(i == len) 
		return 0;
	int ans = 0;
	if(s[i] == str[j])
		ans += solve(s, i+1, j+1);
	ans += solve(s,i+1,j);
	ans%=10000;
	return arr[i][j]=ans;
}
int main()
{
	freopen("ccin.txt","r",stdin);
	freopen("ccout.txt","w",stdout);
	int i, t;
	scanf("%d",&t);
	getchar();
	char s[510];
	for(i=1;i<=t;i++)
	{
		gets(s);
		len=strlen(s);
		memset(arr,-1,sizeof(arr));
		int ans=solve(s,0,0);
		printf("Case #%d: %04d\n",i,ans);
	}
	return 0;
}