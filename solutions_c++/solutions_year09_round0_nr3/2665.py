#include <iostream>
#include <string>
using namespace std;

int c;

void backtrack(const string& text, const string& pattern, int ti, int pi)
{
	if (pi == pattern.size())
	{
		c++;
		return;
	}
	if (ti == text.size())
		return;
	if (text.size()-ti < pattern.size()-pi)
		return;

	if (text[ti] == pattern[pi])
		backtrack(text, pattern, ti+1, pi+1);
	backtrack(text, pattern, ti+1, pi);
}

int main()
{
	int N, i;
	string line;
	string pattern = "welcome to code jam";

	cin >> N;
	cin.ignore();
	for (i = 0; i < N; i++)
	{
		getline(cin, line);

		c = 0;
		backtrack(line, pattern, 0, 0);
		printf("Case #%d: %04d\n", i+1, c);
	}

	return 0;
}
