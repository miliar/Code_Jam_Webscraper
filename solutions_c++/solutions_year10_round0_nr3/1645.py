
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <sstream>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <complex>

#include <map>
#include <fstream>

#include <cstring>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cmath>

using namespace std;

typedef long long LL;
#define double long double

const double PI = acos(-1.0);
const double EPS = 1e-10;

//#ifdef LOCAL
//#define cout fout
#define dout fout
#define cin fin
ifstream fin;
ofstream fout;
//#endif

const int N = 1001;

void solve()
{
	int CN;
	cin >> CN;
	for (int T=0; T < CN; ++T) {
		LL r, n, k;
		cin >> r >> k >> n;
		LL g[N];
		for (int i=0; i < n; ++i) {
			cin >> g[i];
		}

		LL cost[N] = { 0 };
		int next[N] = { 0 };
		for (int i=0; i < n; ++i) {
			LL sum = 0;
			int p = i;
			while (true) {
				if (sum+g[p] > k) break;
				sum += g[p];
				++p;
				if (p==n) p = 0;
				if (p==i) break;
			}
			cost[i] = sum;
			next[i] = p;
		}

		LL ans = 0;
		int p = 0;
		for (int i=0; i < r; ++i) {
			ans += cost[p];
			p = next[p];
		}

		dout << "Case #" << T+1 << ": " << ans << endl;
		cout << "Case #" << T+1 << ": " << ans << endl;
	}
}


int main()
{
//#ifdef LOCAL 
	fin.open("C-large.in");
	//fin.open("in.txt");
	fout.open("out.txt");
//#endif

    solve();

    return 0;
}