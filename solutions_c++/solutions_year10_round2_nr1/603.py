#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int n,m,id;
map<string,int> mp;
string get,path;
int trie[11000][11000],root,node_id;
int ans = 0;


void insert(int cur,int num[],int nn)
{
	for(int i=0;i<nn;i++)
	{
		if(trie[cur][num[i]] == -1)
		{
			trie[cur][num[i]] = node_id++;
		}
		cur = trie[cur][num[i]];
	}
}

void insert2(int cur,int num[],int nn)
{
	for(int i=0;i<nn;i++)
	{
		if(trie[cur][num[i]] == -1)
		{
			ans++;
			trie[cur][num[i]] = node_id++;
		}
		cur = trie[cur][num[i]];
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int cs,cn=1,i,j,k;
	int num[1000],nn;
	char in[1000];
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d%d",&n,&m);
		mp.clear();
		id = 0;
		memset(trie,-1,sizeof(trie));
		root = 0;node_id = 1;
		for(i=0;i<n;i++)
		{
			scanf("%s",in);
			path = string(in+1);
			nn = 0;
			while((j=path.find('/')) != -1)
			{
				get = path.substr(0,j);
				path = path.substr(j+1);
				if(mp.find(get) == mp.end())
				{
					mp[get] = id++;
				}
				num[nn++] = mp[get];
			}
			if(mp.find(path) == mp.end())
			{
				mp[path] = id++;
			}
			num[nn++] = mp[path];

			insert(root,num,nn);
		}
		ans = 0;
		for(i=0;i<m;i++)
		{
			scanf("%s",in);
			path = string(in+1);
			nn = 0;
			while((j=path.find('/')) != -1)
			{
				get = path.substr(0,j);
				path = path.substr(j+1);
				if(mp.find(get) == mp.end())
				{
					mp[get] = id++;
				}
				num[nn++] = mp[get];
			}
			if(mp.find(path) == mp.end())
			{
				mp[path] = id++;
			}
			num[nn++] = mp[path];

			insert2(root,num,nn);
		}
		printf("Case #%d: %d\n",cn++,ans);
	}
	return 0;
}

