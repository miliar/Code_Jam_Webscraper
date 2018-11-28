#include<iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;
int d[105];
int main()
{
	freopen("d:\\test.txt","w",stdout);
	int t,s,p,n,i,num,count=1;
	scanf("%d",&t);
	while(t--)
	{
		num=0;
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++)
			scanf("%d",&d[i]);
		int j=s;
		for(i=0;i<n;i++)
		{
			if(p>1)
			{
				if(d[i]%3)
					d[i]=d[i]/3+1;
				else
					d[i]=d[i]/3;
				if(d[i]>=p)
				{
					num++;
					continue;
				}
				if(d[i]==p-1)
				{
					if(j>0)
					{
						num++;j--;
					}
				}
			}
			else
			{
				if(d[i]%3)
					d[i]=d[i]/3+1;
				else
					d[i]=d[i]/3;
				if(d[i]>=p)
				{
					num++;
					continue;
				}
			}
		}

		printf("Case #%d: %d\n",count++,num);
	}	
	return 0;
}