#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

const int N = 102, INF=123456789;

int main()
{
	
	int i,j,k,h,test;
	int f[N][N], a[N], room, people;
	int ca;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d", &ca);
	for(test=1;test<=ca;++test)
	{
		
		scanf("%d%d", &room, &people);
		memset(f,0,sizeof(f));
		memset(a,0,sizeof(a));
		for(i=1;i<=people;++i) scanf("%d", a+i);
		a[0]=0;
		a[people+1]=room+1;

		for(i=1;i<=people;++i) f[i][i]=a[i+1]-a[i-1]-2;
		for(h=1;h<=people;++h)
		for(i=1;i+h<=people;++i)
		{	
			{
				j=i+h;
				{
					f[i][j] = INF;
					for(k=i;k<=j;++k)
					{
						f[i][j] = min(f[i][j], 
							f[i][k-1]+f[k+1][j]+a[j+1]-a[i-1]-2);
					}
				}
			}
		

		}
		printf("Case #%d: %d\n", test, f[1][people]);
	}
	return 0;
}