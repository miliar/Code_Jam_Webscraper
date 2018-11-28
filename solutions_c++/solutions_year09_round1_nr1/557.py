#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

#define sqr(x) ((x)*(x))

vector<int> bases;

void get_bases(char* inp)
{
	while(inp && *inp)
	{
		int base;
		sscanf(inp, "%d", &base);
		bases.push_back(base);
		inp = strchr(inp, ' ');
		if (inp) ++inp;
	}
}

string base_to(int n, int base)
{
	char res[1024];
	int len = 0;
	while(n)
	{
		res[len] = (n % base) + '0';
		n /= base;
		++len;
	}
	res[len] = '\0';

	reverse(res, res+len);
	return res;
}

bool is_happynumber(int n, int base)
{
	set<string> exist;
	while(n != 1)
	{
		string cur = base_to(n, base);
		if (exist.find(cur) != exist.end())
			return false;
		exist.insert(cur);
		n = 0;
		for(int i = 0; i < cur.length(); ++i)
		{
			n += sqr(cur[i]-'0');
		}
	}

	return true;
}

int solve()
{
	int n = 1;
	bool happynumber;
	do
	{
		++n;
		happynumber = true;
		for(int i = 0; i < bases.size() && happynumber; ++i)
		{
			happynumber = happynumber && is_happynumber(n, bases[i]);
		}
	} while(!happynumber);
	return n;
}

int main()
{
	char inp[1024];
	int T;
	scanf("%d", &T);
	gets(inp);

	for(int i = 1; i <= T; ++i)
	{
		gets(inp);
		bases.clear();
		get_bases(inp);
		printf("Case #%d: %d\n", i, solve());
	}
}