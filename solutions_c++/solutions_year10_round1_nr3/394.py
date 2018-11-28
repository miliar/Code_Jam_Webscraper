#pragma warning(disable:4996)
#pragma warning(disable:4010)//×¢ÊÍ
#include<iostream>
#include<cstdio>
#include<ctime>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<cmath>
#include<cstring>
#include<map>
#include<string>
using namespace std;
#include <iostream>
using namespace std;

int sum=0;

int GCD(int a,int b)
{
	int tmp;
	if(a==b || !a || !b) 
		return 0;
	if(a<b) 
	{
		a^=b;
		b^=a;
		a^=b;
	}
	if((b<<1)<=a)
		return 1;
	++sum;
	return GCD(a%b,b);
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.txt","w",stdout);
	int t,pzj;
	scanf("%d",&t);
	for(pzj=1;pzj<=t;++pzj)
	{
	int i,j,ans=0;
	int a[3];
	int b[3];
	scanf("%d %d %d %d",a,a+1,b,b+1);
	for(i=a[0];i<=a[1];++i)
		for(j=b[0];j<=b[1];++j)
		{	
			sum=0;
			if(GCD(i,j) && 0==(sum&1)) 
				++ans;
		}
	printf("Case #%d: %d\n",pzj,ans);
	}
	return 0;
}
