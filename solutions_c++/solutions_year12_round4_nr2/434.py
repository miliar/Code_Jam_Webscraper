#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#define N 3050
using namespace std;

struct node1
{
	int x,y;
}f[N];

struct node2
{
	int r,num;
}a[N];

int cmp(node2 aa,node2 bb)
{
	return aa.r>bb.r;
}

int main(void)
{
	int t,n,ys=0,w,l;
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	cin>>t;
	while (t--)
	{
		cin>>n>>w>>l;
		int mid;
		for (int i=0;i<n;i++)
		{
			cin>>a[i].r;
			a[i].num=i;
		}
		sort(a,a+n,cmp);

		int x=a[0].r;
		int y=a[0].r;

		f[a[0].num].x=f[a[0].num].y=0;
		mid=0;

		for (int i=1;i<n;i++)
		{
			if (x+a[i].r>w)
			{
				f[a[i].num].x=0;
				f[a[i].num].y=y+a[i].r;
				x=a[i].r;
				mid=y+a[i].r;
				y=y+a[i].r*2;

			}
			else
			{
				f[a[i].num].x=x+a[i].r;
				f[a[i].num].y=mid;
				x=x+a[i].r*2;
			}
		}

		printf("Case #%d: ",++ys);
		for (int i=0;i<n;i++)
			printf("%d %d%c",f[i].x,f[i].y,i==n-1?'\n':' ');
		//~ for (int i=0;i<n;i++)
			//~ for (int j=i+1;j<n;j++)
			//~ {
				//~ int d=(f[i].x-f[j].x)*(f[i].x-f[j].x)+(f[i].y-f[j].y)*(f[i].y-f[j].y);
				//~ if (d<(a[i].r+a[j].r)*(a[i].r+a[j].r))
					//~ cout<<"fuck"<<endl;
			//~ }
	}

	return 0;
}
