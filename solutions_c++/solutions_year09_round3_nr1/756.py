#include <cstdio>
#include <string>
#include <vector>

__int64 get_num(const std::string &str)
{
	if (str.size()==1) return 1;
	if (str.size()==2)
	{
		return str[0]==str[1]?3:2;
	}

	bool exists[256]={0};
	int value[256]={0};
	__int64 bz=2;
	int next = 2;

	exists[(unsigned char)str[0]] = true;
	value[(unsigned char)str[0]] = 1;
	for (size_t i=1; i<str.size(); ++i)
	{
		if (!exists[(unsigned char)str.at(i)])
		{
			exists[(unsigned char)str.at(i)] = true;
			value[(unsigned char)str.at(i)] = 0;
			break;
		}
	}
	for (size_t i=2; i<str.size(); ++i)
	{
		if (!exists[(unsigned char)str.at(i)])
		{
			++bz;
			exists[(unsigned char)str.at(i)] = true;
			value[(unsigned char)str.at(i)] = next;
			++next;
		}
	}

	__int64 bzz = 1, result=0;
	for (int i=str.size()-1; i>=0; --i)
	{
		result += value[(unsigned char)str.at(i)]*bzz;
		bzz *= bz;
	}
	return result;
}

int main()
{
	int N;
	char str[4000];

	scanf("%d\n", &N);
	for (int i=1;i<=N;++i)
	{
		scanf("%s\n", str);
		printf("Case #%d: %I64d\n", i, get_num(str));
	}

	return 0;
}