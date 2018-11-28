#pragma comment(linker, "/STACK:1073741824")
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <iostream>
#include <functional>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
#include <cmath>
#include <ctime>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, b, a) for (int i = (int)(b); i >= (int)(a); i--)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef unsigned long long ull;
const int INF = 1000000000;

using namespace std;

void prepare(string s){
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt","w", stdout);
#else
	//freopen((s + ".in").c_str(), "r", stdin);
    //freopen((s + ".out").c_str(),"w", stdout);
#endif
}

int n;
string s;
string answer;

void readdata ()
{
	scanf ("%d", &n);
}

void writedata ()
{
	printf ("%s\n", answer.c_str());
}

map <char, char> m;
map <char, char> m2;
void init ();
void solve ()
{
	answer = s;
	for (int i = 0; i < s.length(); i++)
		answer[i] = m2[s[i]];
}

void init ()
{
	m[' '] = ' ';
	m['a'] = 'y';
	m['b'] = 'n';
	m['c'] = 'f';
	m['d'] = 'i';
	m['e'] = 'c';
	m['f'] = 'w';
	m['g'] = 'l';
	m['h'] = 'b';
	m['i'] = 'k';
	m['j'] = 'u';
	m['k'] = 'o';
	m['l'] = 'm';
	m['m'] = 'x';
	m['n'] = 's';
	m['o'] = 'e';
	m['p'] = 'v';
	m['q'] = 'z';
	m['r'] = 'p';
	m['s'] = 'd';
	m['t'] = 'r';
	m['u'] = 'j';
	m['v'] = 'g';
	m['w'] = 't';
	m['x'] = 'h';
	m['y'] = 'a';
	m['z'] = 'q';
	map <char, char> ::iterator it = m.begin();
	for (; it != m.end(); ++it)
	{
		m2[it->second] = it->first;
	}
}

int main()
{
    prepare("divgold");
	init ();
    readdata ();
	char ten = getchar ();
	forn(i, n)
	{
		printf ("Case #%d: ", i + 1);
		getline (cin, s);
		solve ();
		writedata ();
	}
    return 0;
}