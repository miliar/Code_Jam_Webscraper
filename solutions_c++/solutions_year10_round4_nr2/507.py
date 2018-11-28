/*
TASK: 
ID: marijon1
LANG: C++
*/

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <complex>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#define mp make_pair
#define st first
#define nd second
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORO(i,n) for(int i=1;i<=(n);i++)
#define FORS(i,a,n) for(int i=(a);i<(n);i++)
#define FORB(i,a,n) for(int i=(a);i>=(n);i--)
#define foreach(v, i) for (typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define INRANGE(a,b,c,d) ((a)>=0&&(b)>=0&&(a)<(c)&&(b)<(d))
#define sz(v) ((int)(v).size())
#define pf printf

using namespace std;
typedef long long ll;

int P, Teams;
int Miss[2000];
int Prices[2000][12];
int Cache[12][1030][12];


int min_price(int round, int x, int have_tickets) {
	//pf("mp(%d, %d, %d)\n", round, x, have_tickets);
	if (round == P) {
		if (have_tickets < P - Miss[x])
			return 1000000;
		else {
			//pf("ok end: round=%d x=%d have_tickets=%d\n", round, x, have_tickets);
			return 0;
		}
	}
	else {
		if (Cache[round][x][have_tickets] != -1)
			return Cache[round][x][have_tickets];
		return Cache[round][x][have_tickets] = min(min_price(round+1, 2*x, have_tickets) + min_price(round+1, 2*x+1, have_tickets),
			min_price(round+1, 2*x, have_tickets+1) + min_price(round+1, 2*x+1, have_tickets+1) + Prices[x][round]);
	}
}

int xcase() {
	cin >> P;
	Teams = 1 << P;
	FOR(i, Teams)
		cin >> Miss[i];
	FORB(i, P-1, 0) {
		FOR(j, 1 << i) {
			cin >> Prices[j][i];
		}
	}
	fill(Cache[0][0], Cache[12][0], -1);
	//pf("pre:%d\n", min_price(2, 0, 1));
	return min_price(0, 0, 0);
}

int main() {
	//freopen("xxxxx.in", "r", stdin);
	//freopen("xxxxx.out", "w", stdout);
	int C;
	cin >> C;
	FOR(i, C) {
		pf("Case #%d: %d\n", i+1, xcase());
	}
	return 0;
}
