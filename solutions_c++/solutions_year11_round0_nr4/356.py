// gcj D
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<map>
#include<string>
#include<cmath>
#include<set>
using namespace std;
const int MAX=1000+10;

map<int,int> my;
int N,a[MAX];
int find(int x)
{
	for(int i=x+1;i<=N;i++) if(a[i]==x) return i;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	
	int T;scanf("%d",&T);
	int CN=0;
	
	while(T--)
	{
		my.clear();
		
		scanf("%d",&N);
		for(int i=1;i<=N;i++) 
		{
			scanf("%d",&a[i]);
			my[a[i]]=1;
		}
		
		map<int,int>::iterator it;
		int D=0;
		for(it=my.begin();it!=my.end();it++) it->second=++D;
		for(int i=1;i<=N;i++) a[i]=my[a[i]];
		
		int cnt=0;
		for(int i=1;i<=N;i++)
		{
			if(a[i]!=i)
			{
				cnt++;
			
			}
		}
		
		printf("Case #%d: %.6f\n",++CN,(double)cnt);
	}
	
	return 0;
}
