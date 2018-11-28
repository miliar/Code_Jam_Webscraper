#include <set>   
#include <deque>   
#include <stack>   
#include <bitset>   
#include <algorithm>   
#include <functional>   
#include <numeric>   
#include <utility>   
#include <sstream>   
#include <iostream>   
#include <iomanip>   
#include <cstdio>   
#include <cmath>   
#include <cstdlib>   
#include <ctime>   
#include <queue>   
#include <map> 
#include <string.h> 
#include <queue> 
using namespace std;


struct stu
{
	char str[5];
	int pa;
}arr[101];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,n,i,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s %d",arr[i].str,&arr[i].pa);
		}
		int ans=0;
		int h[2]={1,1},Nh=0;
		while(Nh<n)
		{
			int r,r1;
			if(arr[Nh].str[0]=='O')
			{
				r=0;
			}
			else r=1;
			r1=(r+1)%2;
			for(i=Nh+1;i<n;i++)
			{
				if(arr[i].str[0]!=arr[i-1].str[0])break;
			}
			int m=i;
			if(i==n)
			{
				for(i=Nh;i<n;i++)
				{
					ans+=abs(h[r]-arr[i].pa)+1;
					h[r]=arr[i].pa;
				}
				break;
			}
			else
			{
				int ct=abs(h[r1]-arr[m].pa);
				int at=0;
				for(i=Nh;i<m;i++)
				{
					at+=abs(h[r]-arr[i].pa)+1;
					h[r]=arr[i].pa;
				}
				ans+=at;
				h[r]=arr[m-1].pa;
				if(ct<=at)
				{
					h[r1]=arr[m].pa;
				}
				else
				{
					h[r1]=arr[m].pa-(at-ct);
				}
				Nh=m;
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}

