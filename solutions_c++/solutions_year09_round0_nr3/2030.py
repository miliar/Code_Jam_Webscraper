#include <iostream>
#include <memory.h>

using namespace std;

const int mod = 1000;

int n;
string welcome;
int answer[700][100];

int solve(string s, int pos, int matched)
{
	if (matched == welcome.length())
		return 1;
		
	if (pos == s.length())
		return 0;
		
	if (answer[pos][matched] != -1)
		return answer[pos][matched];
		
	if (s[pos] == welcome[matched])
		answer[pos][matched] = (solve(s, pos + 1, matched + 1) + solve(s, pos + 1, matched)) % mod;
	else
		answer[pos][matched] = solve(s, pos + 1, matched);
	
	return answer[pos][matched];
}

int main()
{
	int i;
	char tmp[1000];
	string s;
	
	welcome = "welcome to code jam";
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> n;
	gets(tmp);
	for (i = 0; i < n; i++)
	{
		gets(tmp);
		s = tmp;
		memset(answer, 255, sizeof(answer));
		printf("Case #%d: %04d\n", i + 1, solve(s, 0, 0));
	}
	return 0;
}
