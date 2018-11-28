#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int GCD(int a,int b)
{
	if(a==0)return b;
	if(b==0)return a;
	if(a>b)return GCD(a%b,b);
	else return GCD(a,b%a);
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t,n,Pd,Pg,i,j,z=0;
	scanf("%d",&t);
	while(t--)
	{
		z++;
		printf("Case #%d: ",z);
		scanf("%d%d%d",&n,&Pd,&Pg);
		if((Pg==0&&Pd!=0)||(Pg==100&&Pd!=100))
			printf("Broken\n");
		else
		{
			if(n<(100/GCD(Pd,100)))printf("Broken\n");
			else printf("Possible\n");
		}
	}
}
