#include <iostream>
#include <cstdio>

#include <cstring>
#include <string>

static const char mstr[] = "welcome to code jam";
static const int mstl = strlen(mstr);

int count(char* str, int i)
{
	if (*str == 0) return (i == mstl);
	if (i == mstl) return 1;
	
	int res = 0; char *v = str;
	
	for (;;)
	{
		v = strchr(v, mstr[i]); if (!v) break;
		res += count(v + 1, i + 1); ++v;
	};
	
	return res;
};

int main()
{
	int cases; scanf("%d\n", &cases);
	for (int test = 1; test <= cases; ++test)
	{
		std::string s; getline(std::cin, s);
		char *p = (char*) s.c_str();
		
		printf("Case #%d: %04d\n", test, count(p, 0));
	};
};

