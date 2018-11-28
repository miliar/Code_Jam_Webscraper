#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <map>
#include <string>
#include <cmath>
#include <math.h>
#include <fstream>

using namespace std;

typedef struct
{
	int n,s,p;
	int a[200];
}DATA;

int t;
DATA data[200];

int main()
{
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		scanf("%d%d%d",&data[tt].n,&data[tt].s,&data[tt].p);
		for(int i=0;i<data[tt].n;i++)
			scanf("%d",&data[tt].a[i]);
	}
	for(int tt=1;tt<=t;tt++)
	{
		int ans=0;
		for(int i=0;i<data[tt].n;i++)
		{
			if(data[tt].a[i]%3==0)
			{
				int k=data[tt].a[i]/3;
				if(k>=data[tt].p) ans++;
				else if(k==data[tt].p-1&&data[tt].s&&k+1<=10&&k-1>=0)
					{data[tt].s--;ans++;}
			}
			else if(data[tt].a[i]%3==1)
			{
				int k=data[tt].a[i]/3+1;
				if(k>=data[tt].p) ans++;
			}
			else if(data[tt].a[i]%3==2)
			{
				int k=data[tt].a[i]/3+1;
				if(k>=data[tt].p) ans++;
				else if(k==data[tt].p-1&&data[tt].s)
					{data[tt].s--;ans++;}
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}