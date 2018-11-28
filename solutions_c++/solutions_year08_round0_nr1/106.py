#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <map>
#include <string.h>
#include <string>
#include <assert.h>
using namespace std;
#define N 1000
int table[N][N];
int main()
{
	int t,ca;
	for(scanf("%d",&t),ca=1;ca<=t;ca++)
	{
		int s,q;
		scanf("%d",&s);
		assert(s<=N);
		map<string,int> engine;
		while(getchar()!='\n');
		char buf[200];
		for(int i=0;i<s;i++)
		{
			gets(buf);
			engine[buf]=i;
		}
		scanf("%d",&q);
		assert(q<=N);
		while(getchar()!='\n');
		for(int i=1;i<=q;i++)
		{
			gets(buf);
			int ind=-1;
			if(engine.find(buf)!=engine.end())
				ind=engine[buf];
			//printf("%d %d\n",i,ind);
			int best=q;
			for(int j=0;j<s;j++)best=min(best,table[i-1][j]);
			best++;
			for(int j=0;j<s;j++)
			{
				table[i][j]=min(best,table[i-1][j]);
				if(ind==j)table[i][j]=q;
			}
		}
		printf("Case #%d: %d\n",ca,*min_element(table[q],table[q]+s));
	}
	return 0;
}
