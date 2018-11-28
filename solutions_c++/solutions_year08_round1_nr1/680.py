#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <assert.h>

using namespace std;
//#define DBG_PRINT printf
#define DBG_PRINT 

int cmp(const void *p1,const void *p2)
	{
		const long *px = (const long *)p1;
		const long *py = (const long *)p2;
		long dif = *px - *py;

		if(dif>0)
			return 1;
		if(dif<0)
			return -1;
		return 0;
	}
	long long  getMin(long *px,long *py,long n)
	{
		qsort(px,n,sizeof(long),cmp);
		qsort(py,n,sizeof(long),cmp);
		long long sum = 0;
		for (long i=0;i<n;i++)
		{
			sum += px[i]*py[n-1-i];
		}
		return sum;
	}
	int main()
	{
		DBG_PRINT("1-1\n");

		long T,n;
		scanf("%d\n",&T);
		DBG_PRINT("%d\n",T);
		for (long i=0;i<T;i++)
		{
			scanf("%d\n",&n);
			DBG_PRINT("%d\n",n);
			long * px=new long[n];
			long * py=new long[n];
			for (long j=0;j<n;j++)
			{
				scanf("%d",&px[j]);
			}
			for (long j=0;j<n;j++)
			{
				scanf("%d",&py[j]);
			}

			long long sum = getMin(px,py,n);
			printf("Case #%d: %lld\n",i+1,sum);
			delete []px;
			delete []py;
		}
		return 0;
	}