#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

long int power(int a,int b)
{
	long int rslt=1;
	for(int i=0;i<b;i++)
		rslt=(long int)a*rslt;
	return rslt;
}
int recyle_btwn(long int a,long int b);
int main()
{
	int t,cnt=0,i,r;
	long int a,b;
	freopen("C-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%ld %ld",&a,&b);
		r=recyle_btwn(a,b);;
		scanf("\n");
		printf("Case #%d: %d\n",++cnt,r);
	}
	return 0;
}

int recyle_btwn(long int a,long int b)
{
	int r=0,bs,dgt;
	long int alt,tmp1,tmp2,i;
	char cur[10];
	for(i=a;i<=b;i++)
	{
		itoa(i,cur,10);
		dgt=strlen(cur);
		bs=10;
		while(i/bs>0)
		{
			tmp1=i/bs;
			tmp2=i-tmp1*bs;
			alt=tmp2*(power(10,dgt-1))+tmp1;
			//printf("\n%ld,%ld,%ld,",tmp1,tmp2,alt);
			bs=bs*10;
			dgt--;
			if(alt==i)
				break;
			if(alt>i && alt<=b)
			{
				//printf("\n%ld,%ld,",i,alt);
				r++;
			}
		}
	}
	return r;
}