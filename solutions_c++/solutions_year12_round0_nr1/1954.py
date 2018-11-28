#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cstring>
#include <string>
#include <queue>

#pragma comment(linker, "/STACK:64000000") 

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef pair<int64,int64> pii64;
typedef pair<double, int> pdi;
typedef pair<double, double> pdd;
typedef pair<pii, int> piii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;

#define xn _dsfhsdfsj
#define yn _dthsdfshj

#define toMod 1000000007

int n;
char s1[1 << 10], s2[1 << 10];
string ss1, ss2;
int c[1 << 10];
map <char, char> a;
char s[1 << 10];

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	/*
	memset(c, -1, sizeof c);
	scanf("%d\n", &n);
	for (int i = 0; i < n; ++i)
	{
		gets(s1);
		gets(s2);
		stringstream din1(s1);
		stringstream din2(s2);
		while (din1 >> ss1)
		{
			din2 >> ss2;
			int l = (int)ss1.length();
			for (int i = 0; i < l; ++i)
			{
				int x = (int)ss1[i];
				int y = (int)ss2[i];
				c[x] = y;
			}
		}
	}

	for (int x = 1; x < 300; ++x)
	{
		if (c[x] == -1) continue;
		int y = c[x];
		cout << "a['" << (char)x << "'] = '" << (char)y << "';" << endl; 
	}
	*/
	
	a['a'] = 'y';
	a['b'] = 'h';
	a['c'] = 'e';
	a['d'] = 's';
	a['e'] = 'o';
	a['f'] = 'c';
	a['g'] = 'v';
	a['h'] = 'x';
	a['i'] = 'd';
	a['j'] = 'u';
	a['k'] = 'i';
	a['l'] = 'g';
	a['m'] = 'l';
	a['n'] = 'b';
	a['o'] = 'k';
	a['p'] = 'r';
	a['q'] = 'z';
	a['r'] = 't';
	a['s'] = 'n';
	a['t'] = 'w';
	a['u'] = 'j';
	a['v'] = 'p';
	a['w'] = 'f';
	a['x'] = 'm';
	a['y'] = 'a';
	a['z'] = 'q';

	scanf("%d", &n);
	gets(s);

	for (int i = 0; i < n; ++i)
	{
		gets(s);
		int l = (int)strlen(s);
		printf("Case #%d: ", i + 1);
		for (int j = 0; j < l; ++j)
		{
			if (s[j] == ' ')
				printf(" ");
			else
				printf("%c", a[s[j]]);
		}
		printf("\n");
	}

	return 0;
}