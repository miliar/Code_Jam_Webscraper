#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, a) for (int i = 0; i < int(a.size()); i++)
#define fors(i, a) for (int i = 0; i < int(a.length()); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

int k;
string s;                                                                                                      
int ans;

int d[20][20];
long long res[1 << 16][20];
int FF;
long long INFL, result;

void outdata() {
	cout << result << endl;
}

int check(string s) {
	return unique(all(s)) - s.begin();
}

long long calc(int msk, int ls) {
	long long &ans = res[msk][ls];
	if (ans != -1) return ans;
	if (msk == ((1 << k) - 1)) {
		return ans = d[FF][ls];
	}
	ans = INFL;
	forn(i, k) if ((msk & (1 << i)) == 0) {
		ans = min(ans, d[i][ls] + calc(msk ^ (1 << i), i));
	}
	return ans;
}

void solve() {
	INFL = 100000000;
	INFL *= INFL;
	result = INFL;
	vector<int> p(k);
	forn(i, k) p[i] = i;
	int num = s.length() / k;
	ans = s.length();
	memset(d, 0, sizeof d);
	forn(c, k) forn(n, k) if (c != n) {
	  	forn(i, num) {
        	if (s[i * k + c] != s[i * k + n]) ++d[c][n];	  		
		}
	}
	forn(fr, k) {
		memset(res, 255, sizeof res);
		forn(ls, k) {
			int cans = 1;
		  	forn(i, num - 1) {
    	    	if (s[i * k + ls] != s[(i + 1) * k + fr]) ++cans;
			}
			int msk = (1 << fr) | (1 << ls);
			FF = fr;
			result = min(result, cans + calc(msk, ls));
		}
	}
}

void readdata() {
	cin >> k >> s;
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		readdata();
		solve();
		outdata();
	}
	return 0;
}
