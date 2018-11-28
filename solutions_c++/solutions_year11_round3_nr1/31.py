#include <stdio.h>
#include <string>
#include <vector>

using std::vector;
using std::string;

bool slove(vector<string>& pattern)
{
	size_t size = pattern.size();
	size_t len = pattern[0].size();
	for(size_t i = 0;i < size;++i)
	{
		for(size_t k = 0;k < len;++k)
		{
			if('#' != pattern[i][k]) continue;
			if(i+1 == size || k+1 == len) return false;
			if(pattern[i][k+1] != '#') return false;
			if(pattern[i+1][k] != '#') return false;
			if(pattern[i+1][k+1] != '#') return false;
			pattern[i][k] = '/';pattern[i+1][k+1] = '/';
			pattern[i][k+1] = '\\';pattern[i+1][k] = '\\';
		}
	}
	return true;
}

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int r = 0,c = 0;scanf("%d%d",&r,&c);
		char buff[0x100] = { 0 };
		vector<string> pattern(r);
		for(int i = 0;i < r;++i)
		{
			scanf("%s",buff);
			pattern[i] = buff;
		}
		bool res = slove(pattern);
		printf("Case #%d:\n",iCases);
		if(!res) printf("Impossible\n");
		else
		{
			for(int i = 0;i < r;++i) printf("%s\n",pattern[i].c_str());
		}
	}
	return 0;
}