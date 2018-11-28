#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define seta(a, b) memset(a, b, sizeof(a))

const string name = "g";

map <char, char> M;
char s[10010];

int main()
{
	freopen((name + ".in").data(), "r", stdin);
	freopen((name + ".out").data(), "w", stdout);

	string b = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string a = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	int zn = 0;
	forn(i, a.length())
	{
		if (!M.count(b[i])) zn++;
		M[b[i]] = a[i];
	}
	M[' '] = ' ';
	M['q'] = 'z';
	M['z'] = 'q';
	int tst;
	cin >> tst;
	gets(s);
	forn(i, tst)
	{
		gets(s);
		cout << "Case #" << i + 1 << ": ";
		forn(i, strlen(s))
			cout << M[s[i]];
		cout << endl;
	}

	return 0;
}
