#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define MAXN 1000

int node[MAXN];
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("CS.txt","w",stdout);
	int ca,cs=1;
	int n;
	scanf("%d",&ca);
	int size;
	while(ca--)
	{
		scanf("%d",&n);
		size=0;
		int a,b;
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&a,&b);
			for(int j=0;j<b;j++)
				node[size++]=a;	
		}
		int ans=0;
		int last=-1000000000;
		bool T=true;
		while(T)
		{	
			T=false;
			last = -100000000;
			for(int i=0;i<size-1;i++)
			{
				if(node[i]==node[i+1] && node[i]!=last)
				{
					last = node[i];
					node[i]--;
					node[i+1]++;
					i++;
					ans++;
					T=true;
				}
			}
			sort(node,node+size);
		}
		printf("Case #%d: %d\n",cs++,ans);
			
	}
	return 0;	
} 


