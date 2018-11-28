#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <cstring>
#include <complex>
#include <numeric>
#include <functional>
//#define NDEBUG
#include <assert.h>
using namespace std;
#ifndef NDEBUG
    #define debug(x) cerr<<#x<<"=\""<<x<<"\""<<" at line#"<<__LINE__<<endl;
    #define hline() cerr<<"-----------------------------------------"<<endl;
#else
    #define debug(x)
    #define hline()
#endif
typedef long long int llint;
#define low(x) ((((x)^((x)-1))&x))
#define two(x)  ((1)<<(x))
#define PB(x) push_back((x))
#define SORT(x) sort(x.begin(),x.end())
const int dir[][2]={{-1,0},{0,1},{1,0},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
const char dname[]="NWSE";
const string pattern="welcome to code jam";
const int mod=10000;
int main()
{
	int ca=1,tt;
	for(scanf("%d",&tt);tt--;ca++)
	{
		const int n=pattern.length();
		vector<int> dp(n+1);
		dp[0]=1;
		char ch;
		while(!isalpha(ch=getchar()));
		do
		{
			for(int i=n;i;i--)
			{
				if(ch!=pattern[i-1])continue;
				dp[i]+=dp[i-1];dp[i]%=mod;
			}
		}while((ch=getchar())==' '||isalpha(ch));
		int ans=dp[n];
		printf("Case #%d: %04d\n",ca,ans);
	}
	return 0;
}
