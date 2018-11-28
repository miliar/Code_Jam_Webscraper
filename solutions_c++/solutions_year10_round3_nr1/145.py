#include<iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int n;
int xx[1005],yy[1005];

bool interact(int x1,int y1,int x2,int y2 )
{
	if ((x1>x2&&y1<y2)||(x1<x2&&y1>y2))
	{
		return true;
	}
	return false;
}


int main()
{
	freopen("A-small.in","r",stdin);
	freopen("a-small.out","w",stdout);
	int i,j,Cases;
	int Test;
	scanf("%d",&Test);
	int Count;
	for (Cases = 1;Cases<=Test;Cases++)
	{
		Count = 0;
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%d %d",&xx[i],&yy[i]);
		}
		for (i=0;i<n;i++)
		{
			for (j=i+1;j<n;j++)
			{
				if (interact(xx[i],yy[i],xx[j],yy[j]))
				{
					Count++;
				}
			}
		}
		printf("Case #%d:%d\n",Cases,Count);
	}

}