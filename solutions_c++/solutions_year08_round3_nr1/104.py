#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>


#define SZ 1005
#define SZ2 1005

__int64 data[SZ];

int sortfunc(const void *a, const void *b);

int main()
{
	__int64 i,j,k,kase,inp,n,l,p,temp,res;

//	freopen("A-sample.in","r",stdin);
//	freopen("A-sample.out","w",stdout);

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%I64d",&inp);
	for(kase=1;kase<=inp;kase++)
	{
		scanf("%I64d %I64d %I64d",&p,&k,&l);
		printf("Case #%I64d:",kase);
		for(i=0;i<l;i++)
		{
			scanf("%I64d",&data[i]);
		}
		if(p*k<l)
		{
			printf(" Impossible\n");
		}
		qsort(data,l,sizeof(__int64),sortfunc);
		res=0;
		for(i=0;i<l;i++)
		{
			res=res+(data[i]*(i/k+1));
		}
		printf(" %I64d\n",res);
	}
	return 0;
}

int sortfunc(const void *a, const void *b)
{
	__int64 *x=(__int64 *)a;
	__int64 *y=(__int64 *)b;
	if(*x>*y)
		return -1;
	if(*x<*y)
		return 1;
	return 0;
}
