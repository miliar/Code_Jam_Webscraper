#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<set>
#include<string>
#include<vector>

using namespace std;

int tot;
set<string> adj[20005];
map<string,int> mp[20005];
vector< pair<string,int> > got[20005];

int visited[20005];

int main()
{
	freopen("A1.in","r",stdin);
	freopen("A1.out","w",stdout);
	int t,i,n,m,cs=0;
	char s[105],st[105];
	string ss;
	scanf("%d",&t);
	for(cs=0;cs<t;cs++)	
	{
		scanf("%d%d",&n,&m);
		memset(visited,0,sizeof(visited));
		for(i=0;i<tot;i++)
			adj[i].clear(),got[i].clear(),mp[i].clear();
		tot=1;
		for(i=0;i<n;i++)
		{
			int j;
			scanf("%s",s);
			for(j=0;s[j];j++)
				if(s[j]=='/')
					s[j]=' ';
			int bs=0,db;
			int k=0;
			while(sscanf(s+bs,"%s%n",st,&db)==1)
			{
				bs+=db;
				string ss=st;
				if(adj[k].find(ss)==adj[k].end())
					adj[k].insert(ss),got[k].push_back(make_pair(ss,tot)),
					mp[k][ss]=got[k].size()-1,tot++;
				k=got[k][mp[k][ss]].second;
				visited[k]=1;
			}
		}
		int cnt=0;
		for(i=0;i<m;i++)
		{
			int j;
			scanf("%s",s);
			for(j=0;s[j];j++)
				if(s[j]=='/')
					s[j]=' ';
			int bs=0,db;
			int k=0;
			while(sscanf(s+bs,"%s%n",st,&db)==1)
			{
				bs+=db;
				string ss=st;
				if(adj[k].find(ss)==adj[k].end())
					adj[k].insert(ss),got[k].push_back(make_pair(ss,tot)),
					mp[k][ss]=got[k].size()-1,tot++;
				k=got[k][mp[k][ss]].second;
				if(!visited[k])
					cnt++;
				visited[k]=1;
			}
		}
		printf("Case #%d: %d\n",cs+1,cnt);
	}
	return 0;
}