#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
typedef long long ll;
const int inf=(1<<30);
#define mset(a,x) memset(a,x,sizeof(a))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#include <stdlib.h>

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int a,i,j,t=1;
	cin>>a;
	string str1,str2="welcome to code jam";
	getline(cin,str1);
	while (a--)
	{
		int dp[19]={0};
		getline(cin,str1);
		for (i=0 ;i<str1.size() ;i++ )
		{
			for (j=18 ;j>=1 ;j-- )
			{
				if(str1[i]==str2[j])
					dp[j]=(dp[j]+dp[j-1])%10000;				
			}
			if(str1[i]==str2[0])
				dp[0]=(dp[0]+1)%10000;
		}
		if (dp[18]>10000)
			dp[18]=dp[18]%10000;
		printf("Case #%d: %04d\n",t++,dp[18]);
	}
	return 0;
}

/*
*/
