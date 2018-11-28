#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<string>
#include<set>
#include<map>
using namespace std;
typedef long long lli;
inline lli gcd(lli a, lli b) { return b==0?a:gcd(b,a%b);	}
int main()
{
	int t,l,h,n,cnt,i,j,flag;
	lli g,L,ans;
	int pl[102];
	scanf("%d",&t);
	for(cnt=1;cnt<=t;cnt++)
	{
		scanf("%d%d%d",&n,&l,&h);
		flag=0;
		for(i=0;i<n;i++)
		scanf("%d",&pl[i]);
		sort(pl,pl+n);
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n&&(i%pl[j]==0||pl[j]%i==0);j++);
			if(j==n)
			{
				printf("Case #%d: %d\n",cnt,i);
				flag=1;
				goto end;
			}
		}
		end:
		if(flag==0)
		printf("Case #%d: NO\n",cnt);
		
	}
	return 0;
}
