# include <cstdio>
# include <cstring>
# include <vector>
using namespace std;
char map[26][26];
int n,co[26];
vector<char> res;
vector<int> anti[26];
int main()
{
	int test;
	scanf("%d",&test);
	for(int testcase=1;testcase<=test;testcase++)
	{
		memset(map,0,sizeof(map));
		memset(co,0,sizeof(co));
		res.clear();
		for(int i=0;i<26;i++) anti[i].clear();
		scanf("%d",&n);
		while(n--)
		{
			char str[5];
			scanf("%s",str);
			map[str[0]-65][str[1]-65]=map[str[1]-65][str[0]-65]=str[2];
		}
		scanf("%d",&n);
		while(n--)
		{
			char str[5];
			scanf("%s",str);
			anti[str[0]-65].push_back(str[1]-65);
			anti[str[1]-65].push_back(str[0]-65);
		}
		char str[150];
		scanf("%d%s",&n,str);
		for(int i=0;i<n;i++)
		{
			res.push_back(str[i]);
			co[str[i]-65]++;
			while(res.size()>1)
			{
				int a=res[res.size()-1]-65,b=res[res.size()-2]-65;
				if(map[a][b])
					res.pop_back(),res.pop_back(),res.push_back(map[a][b]),co[a]--,co[b]--,co[map[a][b]-65]++;
				else break;
			}
			if(!res.empty()&&!anti[res.back()-65].empty())
			  for(int j=0;j<anti[res.back()-65].size();j++)
				  if(co[anti[res.back()-65][j]])
				  {
					  memset(co,0,sizeof(co));
					  res.clear();
					  break;
				  }
		}

		printf("Case #%d: [",testcase);
		if(!res.empty())
		{
			printf("%c",res[0]);
			for(int i=1;i<res.size();i++)
				printf(", %c",res[i]);
		}
		printf("]\n");
	}
	return 0;
}