#include <stdio.h>
#include <iostream>
#include"algorithm"
#include <string>
#include <vector>
#include <map>
#include <math.h>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
struct point
{
	__int64 value;
	__int64 circleTime;
	int next;
	__int64 circleValue;
	int index;
};
point data[1000];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int i,j,Case,num,R,k,n,ii;
	__int64 ans;
	VI group;
	scanf("%d",&Case);
	num=1;
	while (Case--)
	{
		scanf("%d %d %d",&R,&k,&n);
		group.resize(n);
		for (i=0;i<n;i++)
		{
			scanf("%d",&group[i]);
		}
		for (i=0;i<n;i++)
		{
			data[i].value = 0;
			data[i].circleTime = 0;
			data[i].next = 0;
			data[i].circleValue = 0;
		}
		ans=0;
		__int64 t=0;
		int index =0;
		for (i=0;i<R;i++)
		{
			if(data[index].circleValue != 0)
			{ 
				data[index].circleTime = i - data[index].index;
				data[index].circleValue = ans - data[index].circleValue;
				t=(R-1-i)/data[index].circleTime;
				ans+=t*data[index].circleValue;
				i+=t*data[index].circleTime;
				if(i<R)
				{
					ans+=data[index].value;
					index = data[index].next;
				}
				continue;
			}
			t=0;
			ii = index;
			data[ii].circleValue = ans;
			data[ii].index = i;
			for(j=0;j<n;j++)
			{
			   if(t+group[index]<=k)
			   {
					t+=group[index];
					index=(index+1)%n;
			   }
			   else
			   {
				   data[ii].value=t;
				   data[ii].next=index;
			       break;
			   }
			}
			if(j==n)
			{
				   data[ii].value=t;
				   data[ii].next=index;		
			}
			ans+=t;
		}
		printf("Case #%d: %I64d\n",num++,ans);				
	}
	return 0; 
}
