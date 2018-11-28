#include <cstdio>
#include <map>
#include <string>
#include <vector>

using namespace std;

map<string,bool> table;

int count(string path)
{
	string t="/";

	int res=0;
	for(int i=1; i<path.size(); i++)
	{
		if(path[i]=='/')
		{
			if(!table[t])
			{
				table[t]=true;
				res++;
				//printf("%s ", t.c_str());
			}
		}
		t+=path[i];
	}
	if(!table[t])
	{
		table[t]=true;
		res++;
		//printf("%s ", t.c_str());
	}

	return res;
}

int main()
{
	freopen("A.in","r",stdin);

	int T,C;
	scanf("%d",&T);
	for(C=1; C<=T; C++)
	{
		int N,M;
		scanf("%d %d",&N,&M);
		char buf[110];
		gets(buf);
		
		table.clear();
		for(int i=0;i<N;i++)
		{
			gets(buf);
			table[buf]=true;						
		}
		table["/"]=true;
		
		int res=0;
		for(int i=0;i<M;i++)
		{
			gets(buf);
			res += count(buf);			
		}

		printf("Case #%d: %d\n", C, res);
	}

	return 0;
}
