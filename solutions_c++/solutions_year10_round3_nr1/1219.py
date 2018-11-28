#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

struct point
{
	int one,two;
};
point seg[1005];
bool comp(point a,point b)
{
	return a.one<b.one;
}
int main()
{
	freopen("d://A-small-attempt0.in","r",stdin);
	freopen("d://2.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		memset(seg,0,sizeof(seg));
		int n;
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			scanf("%d%d",&seg[j].one,&seg[j].two);
		}
		sort(seg,seg+n,comp);
		int res=0;
		for(int j=0;j<n;j++)
		{
			for(int k=j+1;k<n;k++)
			{
				if(seg[j].two>seg[k].two)
					res++;
			}
		}
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}