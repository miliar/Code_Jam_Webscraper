#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
typedef long long LL;
int gcd(int x,int y)
{
	if(!x)return y;
	if(!y)return x;
	return gcd(y,x%y);
}
LL n;
int _,ca,pd,pg;
int main()
{
//	while(~scanf("%d%d",&pd,&pg))printf("%d\n",gcd(pd,pg));
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&_);ca=0;
	while(_--)
	{
		ca++;
		cin>>n>>pd>>pg;
		bool can=true;
		if(pg==100||pg==0)
		{
			if(pd!=pg)can=false;
		}
		else
		{
			int tt=gcd(pd,100);
			int w1=pd/tt;
			int s1=100*w1/pd;
			if((LL)s1<=n)can=true;
			else can=false;
		}
		printf("Case #%d: ",ca);
		if(can)puts("Possible");
		else puts("Broken");
	}
}
