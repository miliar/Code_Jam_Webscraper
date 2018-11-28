#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
const int BIG=0x3f3f3f3f;
#define cc(x) cout<<#x<<':'<<x<<endl;
#define MAX 101
int dp[MAX][257],a[MAX],x;
int gcd(int a,int b)
{
	if(b==0)
		return 0;
	if(a/b>1)
		return 0;
	return gcd(b,a%b)+1;
}
int main()
{
	int a1,a2,b1,b2,i,j,cs,dd,ans;
	scanf("%d",&cs);
	for(dd=1;dd<=cs;dd++)
	{
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		for(ans=0,i=a1;i<=a2;i++)
			for(j=b1;j<=b2;j++)
				if(gcd(max(i,j),min(i,j))%2==0)
					ans++;
		printf("Case #%d: %d\n",dd,ans);
	}
}