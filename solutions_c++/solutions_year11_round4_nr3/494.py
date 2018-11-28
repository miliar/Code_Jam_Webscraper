
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
int a[1001],ans1[1001],ta[1001];
int init1(int n)
{
	int i,num,j,t,ct=0,flag;

	memset(a,0,sizeof(a));
	for(i=n;i>=1;i--)
	{
		flag=0;
		memset(ta,0,sizeof(ta));
		num=i;
	
		for(j=2;j*j<=i;j++)
		{
			if( num%j==0)
			{
				while(num%j==0)
				{
					num/=j;
					ta[j]++;
				}
			}
		}
		ta[num]++;
		for(j=1;j<=i;j++)
		{
			if( a[j]<ta[j])
			{
				if( flag==0)
				{
					ct++;
					flag=1;
				}
				a[j]=ta[j];
			}
		}
	}
	return ct;
}
void init2()
{
	int i,num,j,t,ct=0,flag;

	memset(a,0,sizeof(a));
	for(i=1;i<=1000;i++)
	{
		flag=0;
		memset(ta,0,sizeof(ta));
		num=i;
	
		for(j=2;j*j<=i;j++)
		{
			if( num%j==0)
			{
				while(num%j==0)
				{
					num/=j;
					ta[j]++;
				}
			}
		}
		ta[num]++;
		for(j=1;j<=i;j++)
		{
			if( a[j]<ta[j])
			{
				if( flag==0)
				{
					ct++;
					flag=1;
				}
				a[j]=ta[j];
			}
		}
		ans1[i]=ct;
	}
}
bool prime(int num)
{
	int i;

	if( num<2) return 0;
	for(i=2;i*i<=num;i++)
		if( num%i==0) return false;
	return true;
}

int main()
{
	int repeat,ri=1,i,n,k,ct;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("1.out","w",stdout);

	init2();

	scanf("%d",&repeat);
	while(repeat--)
	{
		scanf("%d",&n);
		ct=0;
		printf("Case #%d: ",ri++);
		if( n==1) {puts("0"); continue;}
		for(i=1;i<=n;i++)
		{
			if( prime(i) ) ct++;
		}
		printf("%d\n",ans1[n]-ct);
	}
	return 0;
}
