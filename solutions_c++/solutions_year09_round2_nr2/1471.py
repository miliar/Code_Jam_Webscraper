#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<algorithm>
#include<functional>
#include<utility>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdio>
#include<ctime>
#include<string>
using namespace std;

bool cmp(int u,int v)
{
	return u>v;
}

int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	int i,j,kth=1;
	while(t--)
	{ 
		int n;
		scanf("%d",&n);
		int a[10];
		int m=n,i,j=0;
		while(m>0)
		{
          a[j++]=m%10;
		  m=m/10;
		}
		int len=j;
		for(i=1;i<len;i++)
		{
			int minn=1000;
			int biao=-1;
			for(j=0;j<i;j++)
			{
				if(a[j]>a[i])
				{
					if(a[j]<=minn)
					{
						minn=a[j];
					    biao=j;
					}
				}
			}
			if(biao!=-1)
			{
                int t=a[i];
				a[i]=a[biao];
				a[biao]=t;
				sort(a,a+i,cmp);
				break;
			}
		}
		int p=0;
		if(i>=len)
		{
			 sort(a,a+len);
			 for(i=0;i<len;i++)
				 if(a[i]!=0)
					 break;
			 int t=a[i];
			 a[i]=a[0];
			 a[0]=t;
			 p=1;
		}
		int d=0;
		if(p==0)
		{
		for(i=len-1;i>=0;i--)
			d=d*10+a[i];
		}
		else
		{
			d=d+a[0];
			d=d*10;
            for(i=1;i<len;i++)
			 d=d*10+a[i];
		}
		printf("Case #%d: %d\n",kth++,d);
	} 
	return 0;
}

