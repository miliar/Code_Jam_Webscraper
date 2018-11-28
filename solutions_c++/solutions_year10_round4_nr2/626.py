#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int maxx(int a,int b)
{
	return a<b?a:b;
}

int m[(1<<10)+5];

int main()
{
	int case_t;
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&case_t);
	int pp=1;
	while(case_t--)
	{
		int r;
		int i,j;
		scanf("%d",&r);
		for(i=0;i<(1<<r);++i)
			scanf("%d",m+i);
		int a;
		for(i=0;i<(1<<r)-1;++i)
			scanf("%d",&a);
		int p=(1<<r);
		int ans=0;
		while(1)
		{
			int q=0;
			if(p==1) break;
			for(i=0;i<p;i+=2)
			{
				if(m[i]<=0||m[i+1]<=0) ans++;
				m[q]=maxx(m[i]-1,m[i+1]-1);
				q++;
			}
			p=q;
		}
		printf("Case #%d: %d\n",pp++,ans);
	}
}