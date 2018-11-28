#include <cstdio>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

const char welcome[] = "welcome to code jam";

vector <vector <int> > dp;

int doit(int index, int current, string &s)
{
	if (current >= sizeof(welcome) - 1) {
		return 1;
	}
	if (index >= s.size()) {
		return 0;
	}
	if (dp[index][current] >= 0) {
		return dp[index][current];
	}
	int ret = doit(index + 1, current, s);
	if (s[index] == welcome[current]) {
		ret = (ret + doit(index + 1, current + 1, s)) % 10000;
	}
	return dp[index][current] = ret;
}

int WelcomeToCodeJam(string s)
{
	dp.clear();
	dp.resize(s.size() + 1, vector <int>(sizeof(welcome), -1));

	return doit(0, 0, s);
}

int main()
{
	char inp[999];

	int cases;
	gets(inp); sscanf(inp, "%d", &cases);

	for (int caseno = 1; caseno <= cases; caseno++) {
		gets(inp); string s = inp;

		printf("Case #%d: %04d\n", caseno, WelcomeToCodeJam(s));
	}

	return 0;
}
