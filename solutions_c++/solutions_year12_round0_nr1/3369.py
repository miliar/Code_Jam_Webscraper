#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>

#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>	

#include <algorithm>
#include <utility>
#include <cstdlib>
#include <limits>
#include <cmath>

#define rep(i, k, n) for(ll (i)=(k);(i)<(n);++(i))
#define repit(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define all(x) x.begin(), x.end()
#define clr(a,v) memset((a),(v),sizeof(a))
#define sortt(a) sort((a).begin(), (a).end())
#define frr() freopen("test.in", "r", stdin)
#define fro() freopen("test.out", "w", stdout)
#define sqr(x) ((x) * (x))
#define abss(x) (int) abs ((double) x)
#define inf 10e9
using namespace std;

typedef long long ll;
typedef pair <ll, ll> pll;
typedef pair <int, int> pii;
typedef pair <short, short> pss;
typedef unsigned long long ull;
typedef long double lcd;
typedef vector<int> vii;
typedef vector<string> vs;

typedef pair <pll, ll> triple;

int distance1(pii a, pii b)
{
	return (a.first - b.first)*(a.first - b.first) + (a.second - b.second)*(a.second - b.second);
}

int main() 
{
	frr();
	fro();

	map <char, char> translate;
	translate['y']='a';
	translate['n']='b';
	translate['f']='c';
	translate['i']='d';
	translate['c']='e';
	translate['w']='f';
	translate['l']='g';
	translate['b']='h';
	translate['k']='i';
	translate['u']='j';
	translate['o']='k';
	translate['m']='l';
	translate['x']='m';
	translate['s']='n';
	translate['e']='o';
	translate['v']='p';
	translate['z']='q';
	translate['p']='r';
	translate['d']='s';
	translate['r']='t';
	translate['j']='u';
	translate['g']='v';
	translate['t']='w';
	translate['h']='x';
	translate['a']='y';
	translate['q']='z';

	int n;
	string s;
	char c;
	cin >> n;
	c = getchar();
	rep (i, 0, n)
	{
		getline (cin, s);

		cout << "Case #" << i+1 << ": "; 
		rep (j, 0, s.size())
		{
			if ( s[j] == ' ' )
				cout << ' ';
			else 
				cout << translate[s[j]];
		}

		cout << endl;
	}
	return 0;
}