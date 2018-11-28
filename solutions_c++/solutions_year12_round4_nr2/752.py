#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#define pow(x) ((x)*(x))

using namespace std;

const int N=100;

int i,j,k,m,n,l;
int x,y;
int a[N+10];
double a_x[N+10],a_y[N+10];
bool flag;

bool cmp(int a, int b)
{
	return a>b;
}

double dis(int i,int j)
{
	return sqrt(pow(a_x[i]-(double)a_x[j])+pow(a_y[i]-(double)a_y[j]));
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas=1; cas<=T; cas++)
	{
		scanf("%d%d%d", &n, &x, &y);
		for (i=1; i<=n; i++)
			scanf("%d", &a[i]);
		
		
		for (i=1; i<=n; i++)
		{

			for (j=200; j>=1; j--)
            for (k=200; k>=1; k--)
				{
					a_x[i]=x/(double)j;
					a_y[i]=y/(double)k;

					flag=true;
					for (l=1; l<i; l++)
					if (dis(i,l)<=a[i]+a[l]+2)
					{
						flag=false;
						break;
					}
					if (flag) goto here;
				}
			here:;
			
		}
		printf("Case #%d:",cas);
		for (i=1; i<=n; i++)
			
			printf(" %.6lf %.6lf",a_x[i],a_y[i]);
		cout<<endl;
	}
	return 0;
}
