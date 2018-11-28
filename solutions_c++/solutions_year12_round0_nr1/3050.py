//#pragma comment(linker,"/STACK:256000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <cassert>
#include <stdio.h>
#include <string>
#include <memory.h>

using namespace std;

#define ldb long double
#define LL long long
#define nextline() {int c; while ((c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int INF = 1000 * 1000 * 1000;
const LL INF64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;

map <char, char> mp;

void Load()
{
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string s2 = "our language is impossible to understand";

	for (int i = 0; i < (int)s1.size(); i++)
		mp[s1[i]]  = s2[i];

	s1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s2 = "there are twenty six factorial possibilities";

	for (int i = 0; i < (int)s1.size(); i++)
		mp[s1[i]]  = s2[i];

	s1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	s2 = "so it is okay if you want to just give up";

	for (int i = 0; i < (int)s1.size(); i++)
		mp[s1[i]]  = s2[i];

	mp['q'] = 'z';
	mp['z'] = 'q';

	for (char i = 'a'; i <= 'z'; i++)
		if (mp.find(i) == mp.end()) {
			cerr << i << "\n";
		}
			
}

char s[1000];

void Solve()
{
	int n;
	cin >> n;
	nextline();
	for (int i = 0; i < n; i++) {
		gets (s);
		int m = strlen(s);
		for (int j = 0; j < m; j++)	{
			if (s[j] != ' ')
				s[j] = mp[s[j]];
		}
		printf ("Case #%d: %s\n", i + 1, s);
	}	
	
}
                
int main()
{
	//ios_base::sync_with_stdio(0);
#ifndef ONLINE_JUDGE
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
#endif
	Load();
	Solve();
	return 0;
}
