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

int a, b;

void Load()
{
	scanf ("%d%d", &a, &b);
}

bool was[4000000];

string toString (int x) {
	string s = "";
	while (x > 0) {
		s += x % 10 + '0';
		x /= 10;
	}
	reverse (s.begin(), s.end());
	return s;
}

int toInt (const string &s) {
	int x = 0;
	for (int i = 0; i < (int)s.size(); i++)
		x = x * 10 + s[i] - '0';

	return x;
}


void Solve()
{
	int ans = 0;
	memset (was, false, sizeof(was));
	for (int i = a; i <= b; i++) {
			string s = toString (i);
			for (int j = 0; j < (int)s.size(); j++) {
				s = s.substr (1) + s[0];
				if (s[0] != '0') {
					int q = toInt(s);
					if (i != q && i < q &&  a < q && q <= b && !was[q])	
						ans++;
						was[q] = true;
				} 					
			}
			for (int j = 0; j < (int)s.size(); j++) {
				s = s.substr (1) + s[0];
				if (s[0] != '0') {
					int q = toInt(s);
					if (i != q && i < q &&  a < q && q <= b)	
						was[q] = false;
				} 					
			}  
		}

	cout << ans << "\n";
		
}
                
int main()
{
	//ios_base::sync_with_stdio(0);
#ifndef ONLINE_JUDGE
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
#endif
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		Load();
		printf ("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}
