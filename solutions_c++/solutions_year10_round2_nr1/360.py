#include <stdio.h>
#include <string>
#include <set>

using std::string;
using std::set;

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int n = 0,m = 0;scanf("%d%d",&n,&m);
		char path[0x100] = { 0 };
		set<string> table;
		for(int i = 0;i < n;++i)
		{
			memset(path,0,sizeof(path));
			scanf("%s",path);
			size_t len = strlen(path);
			if(path[len-1] != '/') { path[len] = '/';++len; }
			for(size_t j = 1;j < len;++j)
			{
				if(path[j] != '/') continue;
				path[j] = 0;
				table.insert(path);
				path[j] = '/';
			}
		}
		int ret = 0;
		for(int i = 0;i < m;++i)
		{
			memset(path,0,sizeof(path));
			scanf("%s",path);
			size_t len = strlen(path);
			if(path[len-1] != '/') { path[len] = '/';++len; }
			for(size_t j = 1;j < len;++j)
			{
				if(path[j] != '/') continue;
				path[j] = 0;
				set<string>::iterator it = table.find(path);
				if(it == table.end()) { ++ret;table.insert(path); }
				path[j] = '/';
			}
		}
		printf("Case #%d: %d\n",iCases,ret);
	}
	return 0;
}