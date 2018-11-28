#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int cmp(const void* pa, const void* pb)
{
	int *pInta = (int*)pa;
	int *pIntb = (int*)pb;

	return *pInta - *pIntb;
}
int main() 
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
    int T,i,j;

	scanf("%d", &T);
	for(i=1; i<=T; i++)
	{
		int nCount, N, S, p, a[100];

		scanf("%d%d%d",&N,&S,&p);
		for(j=0;j<N;j++)
		{
			scanf("%d", &a[j]);
		}

		qsort(a, N, sizeof(a[0]), cmp);

		for(j=0,nCount=0;j<N;j++)
		{
			if (a[j] < 3*p-4)
			{
				// no increment of nCount
			}
			else if ((a[j] == 3*p-4 || a[j] == 3*p-3) && p >= 2)
			{
				if (S)
				{
					nCount += 1;
					S--;
				}
			}
			else if ((a[j] == 3*p-2 || a[j] == 3*p-1) && p >= 1)
			{
				nCount++;
			}
			else if (a[j] >= 3*p)
			{
				nCount += N-j;
				break;
			}
		}

		printf("Case #%d: %d\n", i, nCount);
	}
    return 0;
}