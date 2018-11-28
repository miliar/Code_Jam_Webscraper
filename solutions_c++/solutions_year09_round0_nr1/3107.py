#include <cstdio>
#include <string>
#include <vector>
#include <deelx.h>

void to_regexp(char *str)
{
	while(*str)
	{
		if (*str=='(') *str='[';
		else if (*str==')') *str=']';
		str++;
	}
}

int do_count(const std::vector<std::string> &dict, const char* pattern)
{
	CRegexpT <char> regexp(pattern);
	int count = 0;
	MatchResult result;

	for (size_t i=0;i<dict.size();++i)
	{
		result = regexp.Match(dict[i].c_str());
		if (result.IsMatched()) ++count;
	}
	return count;
}

int main()
{
	int L, D, N;
	char str[4000];
	std::vector<std::string> dict;

	scanf("%d %d %d\n", &L, &D, &N);
	for (int i=0;i<D;++i)
	{
		scanf("%s\n", str);
		dict.push_back(str);
	}

	for (int i=1;i<=N;++i)
	{
		scanf("%s\n", str);
		to_regexp(str);
		printf("Case #%d: %d\n", i, do_count(dict, str));
	}
	return 0;
}