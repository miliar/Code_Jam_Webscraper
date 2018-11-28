
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

#ifdef LOCAL
#define cout fout
#define cin fin
ifstream fin;
ofstream fout;
#endif

void solve()
{
	int CN;
	cin >> CN;
	for (int T=0; T < CN; ++T) {
		int n, k;
		cin >> n >> k;

		bool ans=true;
		for (int i=0; i < n; ++i) {
			if ((k&1)==0) {
				ans = false;
				break;
			}
			k /= 2;
		}

		cout << "Case #" << T+1 << ": " << (ans?"ON":"OFF") << endl;
	}
}


int main()
{
#ifdef LOCAL 
	fin.open("A-large.in");
	//fin.open("in.txt");
	fout.open("out.txt");
#endif

    solve();

    return 0;
}