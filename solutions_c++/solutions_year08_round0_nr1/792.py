#include <iostream>
#include <fstream>
using namespace std;

struct node
{
	char str[105];
}w[1005],s[15],mem[15];

int N,S,Q;

int solve()
{
	int ans=0;
	int i,j,t=0;
	for(i=0;i<Q;i++)
	{
		for(j=0;j<t;j++)
			if(strcmp(mem[j].str,w[i].str)==0)break;
		if(j==t)
		{
			strcpy(mem[t++].str,w[i].str);
			if(t==S)
			{
				ans++;
				t=0;
				strcpy(mem[t++].str,w[i].str);
			}
		}

	}
	return ans;
}

int main()
{	
	
	freopen("in.txt","r",stdin);

	int i,count=1;
	
	scanf("%d",&N);
	while(N--)
	{		
		scanf("%d",&S);
		
		gets(s[0].str);

		for(i=0;i<S;i++)			
			gets(s[i].str);
		
		scanf("%d",&Q);
		
		gets(w[0].str);

		for(i=0;i<Q;i++)
		
			gets(w[i].str);

		int ans=solve();
		printf("Case #%d: %d\n",count++,ans);
	}
	return 0;
}