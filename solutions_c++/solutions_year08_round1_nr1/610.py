#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define SZ 805

__int64 data1[SZ];
__int64 data2[SZ];

int sortfunc1(const void *a, const void *b);
int sortfunc2(const void *a, const void *b);

int main()
{
	long inp,i,n,kase;
	__int64 temp,res;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%ld",&inp);
	for(kase=1;kase<=inp;kase++)
	{
		scanf("%ld",&n);
		for(i=0;i<n;i++)
		{
			scanf("%I64d",&data1[i]);
		}
		for(i=0;i<n;i++)
		{
			scanf("%I64d",&data2[i]);
		}
		qsort(data1,n,sizeof(__int64),sortfunc1);
		qsort(data2,n,sizeof(__int64),sortfunc2);
		res=0;
		for(i=0;i<n;i++)
		{
			temp=data1[i]*data2[i];
			res=res+temp;
		}
		printf("Case #%ld: %I64d\n",kase,res);
	}
}

int sortfunc1(const void *a, const void *b)
{
	__int64 *x=(__int64 *)a;
	__int64 *y=(__int64 *)b;
	if(*x>*y)
		return 1;
	if(*x<*y)
		return -1;
	return 0;
}

int sortfunc2(const void *a, const void *b)
{
	__int64 *x=(__int64 *)a;
	__int64 *y=(__int64 *)b;
	if(*x>*y)
		return -1;
	if(*x<*y)
		return 1;
	return 0;
}