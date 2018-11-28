#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>


#define SZ 100
#define SZ2 100

char str[SZ];
long signs[SZ];

long tobase3(long t);

int main()
{
	long i,j,k,kase,inp,n,temp,res,count,tot,len,total;
	__int64 sum,now,mult;
//	freopen("B-sample.in","r",stdin);
//	freopen("B-sample.out","w",stdout);

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);

//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);

	scanf("%ld",&inp);
	for(kase=1;kase<=inp;kase++)
	{
		scanf("%s",str);
		len=strlen(str);
		total=pow(3,len-1);
		count=0;
		for(i=0;i<total;i++)
		{
			memset(signs,0,sizeof(signs));
			tot=tobase3(i);
			sum=0;
			now=0;
			mult=1;
			for(j=0;j<len;j++)
			{
				now=now+(str[len-j-1]-'0')*mult;
				if(signs[j]==0)
				{
					mult=mult*10;
				}
				if(signs[j]==1)
				{
					sum=sum+now;
					now=0;
					mult=1;
				}
				if(signs[j]==2)
				{
					sum=sum-now;
					now=0;
					mult=1;
				}
			}
			sum=sum+now;
			if(sum%2==0||sum%3==0||sum%5==0||sum%7==0)
				count++;
		}
		printf("Case #%ld: %ld\n",kase,count);
	}
	return 0;
}

long tobase3(long t)
{
	long i;
	i=0;
	while(t>0)
	{
		signs[i]=t%3;
		t=t/3;
		i++;
	}
	return(i);
}

int sortfunc(const void *a, const void *b)
{
	long *x=(long *)a;
	long *y=(long *)b;
	if(*x>*y)
		return 1;
	if(*x<*y)
		return -1;
	return 0;
}
