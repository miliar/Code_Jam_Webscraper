#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

int i,j,k;
int t,T;
int n;
int a[500];
int s;
double l,h,m,z,x;
double p;
int it;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for(t=1; t<=T; t++)
	{
		s = 0;
		scanf("%d", &n);
		for (i=0; i<n; i++)
		{
			scanf("%d", &a[i]);
			s+=a[i];
		}


		printf("Case #%d:", t);
		for (k=0; k<n; k++)
		{
			for (l=0, h=1, it=0; h-l>1e-9 && it<100; it++)
			{
				m = (l+h)/2;
				p = a[k]+s*m;
				z = 1-m;

				for(i=0; i<n; i++)
				{
					if(i==k)
					{
						continue;
					}
					if (a[i] < p)
					{
						z-=(p-a[i])/s;
						if(z<0)
						{
							break;
						}
					}
				}
				if (i<n)
				{
					h = m;
				}
				else
				{
					l = m;
				}
			}
			printf(" %lf", m*100);
		}
		printf("\n");
    }
	fflush(stdout);
	return 0;
}