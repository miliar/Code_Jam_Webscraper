#include<iostream>
#include<cstdio>
#include<map>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

#define INF 99999999

int main()
{
	int t,i,j,k,tc;
	cin>>tc;
	
	for(t=1;t<=tc;++t)
	{
		int s,q;
		cin>>s;
		char buf[1000];
		
		map<string,int> se;
		
		gets(buf);
		for(i=0;i<s;++i)
		{
			gets(buf);
			se[ (string) buf ]=i;
		}
		cin>>q;
		gets(buf);
		if(q<1)
		{
			printf("Case #%d: %d\n",t,0);
			continue;
		}
		
		
		vector<int> query;
		for(i=0;i<q;++i)
		{
			gets(buf);
			query.push_back(se[ (string) buf ] );
		}
		
		int best[1005][105];
		
		for(i=0;i<s;++i)
			best[0][i]=0;
		
		best[0][query[0]]=INF;
		
		for(i=1;i<query.size();++i)
		{
			for(j=0;j<s;++j)
			{
				best[i][j]=best[i-1][j];
				for(k=0;k<s;++k)
					best[i][j]=min(best[i][j],best[i-1][k]+1);
			}
			best[i][query[i]]=INF;
		
		}
		
		int ans=INF;
		for(i=0;i<s;++i)
			ans=min(ans,best[query.size()-1][i]);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
