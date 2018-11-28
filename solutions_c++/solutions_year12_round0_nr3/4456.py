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
#ifndef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt","w", stdout);
#else
	//freopen((s + ".in").c_str(), "r", stdin);
    //freopen((s + ".out").c_str(),"w", stdout);
#endif
}

int n;
int a, b;
int answer = 0;

string s[1001];

void readdata ()
{
	scanf ("%d", &n);
}

void writedata ()
{
	printf ("%d\n", answer);
}

string toint (int i)
{
	string ans = "";
	while (i > 0)
	{
		ans.pb (i % 10 + '0');
		i /= 10;
	}
	reverse (all(ans));
	return ans;
}

bool check (int i, int j)
{
	string s1 = s[i], s2 = s[j];
	if (s1.length() != s2.length())
		return false;
	for (int i = 1; i < s2.length(); i++)
	{
		if (s1 == s2.substr(i) + s2.substr(0, i)) 
			return true;
	}
	return false;
}

void solve ()
{
	for (int i = 1; i <= 1000; i++)
	{
		s[i] = toint ( i );
	}
	for (int i = a; i <= b; i++)
	{
		for (int j = i + 1; j <= b; j++)
		{
			if (check (i, j))
				answer ++;
		}
	}
}

int main()
{
    prepare("divgold");
    readdata ();
	forn(i, n)
	{
		answer = 0;
		printf ("Case #%d: ", i + 1);
		scanf ("%d %d", &a, &b);
		solve ();
		writedata ();
	}
    return 0;
}