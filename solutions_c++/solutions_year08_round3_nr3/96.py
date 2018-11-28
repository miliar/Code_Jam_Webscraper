#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>


#define SZ 1005
#define SZ2 1005

__int64 data[SZ];
__int64 a[SZ];

__int64 store[SZ];


__int64 total;

int main()
{
	__int64 i,j,k,kase,inp,n,temp,res,m,x,y,z;

//	freopen("C-sample.in","r",stdin);
//	freopen("C-sample.out","w",stdout);

	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);

//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);

	
	scanf("%I64d",&inp);
	for(kase=1;kase<=inp;kase++)
	{
		total=0;
		scanf("%I64d %I64d %I64d %I64d %I64d",&n,&m,&x,&y,&z);
		for(i=0;i<m;i++)
		{
			scanf("%ld",&a[i]);
		}
		for(i=0;i<n;i++)
		{
			data[i]=a[i%m];
			a[i%m]=(x*a[i%m]+y*(i+1))%z;
		}
		store[0]=1;
		for(i=1;i<n;i++)
		{
			store[i]=1;
			for(j=0;j<i;j++)
			{
				if(data[j]<data[i])
					store[i]=(store[i]+store[j])%1000000007;
			}
		}
		res=0;
		for(i=0;i<n;i++)
		{
			res=(res+store[i])%1000000007;
		}
		printf("Case #%I64d: %I64d\n",kase,res);
	}
	return 0;
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
