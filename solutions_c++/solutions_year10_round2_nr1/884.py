#include <cstdio>
#include <map>
#include <string>
#include <vector>

void split(const std::string &path, std::vector<std::string> &paths)
{
	paths.clear();
	if (path.empty()||path[0]!='/')
	{
		printf("ERROR PATH!\n");
		return;
	}

	size_t p = path.find('/',1);
	while (p!=std::string::npos)
	{
		paths.push_back(path.substr(0,p));
		p = path.find('/',p+1);
	}
	paths.push_back(path);
}

void add_paths(const std::string &path, std::map<std::string, bool> &fs)
{
	std::vector<std::string> v;
	split(path, v);
	for (size_t i=0;i<v.size();++i)
	{
		fs[v[i]]=true;
	}
}

int calc_paths(const std::string &path, std::map<std::string, bool> &fs)
{
	std::vector<std::string> v;
	split(path, v);

	int res = 0;
	for (size_t i=0;i<v.size();++i)
	{
		if (!fs[v[i]])
		{
			++res;
			fs[v[i]]=true;
		}
	}
	return res;
}

void main()
{
	int nCases, N, M, nCnt;
	scanf("%d", &nCases);
	char buf[4096];

	for(int nCase=1;nCase<=nCases;++nCase)
	{
		std::map<std::string, bool> fs;

		scanf("%d %d\n", &N, &M);
		for(int i=0;i<N;++i)
		{
			add_paths(gets(buf), fs);
		}

		nCnt = 0;
		for(int i=0;i<M;++i)
		{
			nCnt += calc_paths(gets(buf), fs);
		}

		printf("Case #%d: %d\n", nCase, nCnt);
	}
}

