#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

char buf[1024*1024];
int g[1002];
int main() {
	freopen("C:\\Projects\\codejam\\input", "rt", stdin);
	freopen("C:\\Projects\\codejam\\output.txt", "wt", stdout);

	
	int m;
	cin >> m;

	/* Problem A
	for (int z=0;z<m;z++)
	{
		cout << "Case #" << (z+1) << ": ";
		int n,k;
		cin >> n >> k;
		bool res = (k + 1 ) % (2 << (n - 1));
		if (res == true) cout << "OFF"; else cout << "ON";
		cout << endl;
	}*/

	for (int z=0;z<m;z++)
	{
		int r,k,n;
		cin >> r >> k >> n;

		for (int y=0;y<n;y++) { cin >> g[y]; }

		long long res = 0;
		vector<int> pos;
		vector<long long> counts;
		int cur=0;
		int ctrip = 0;
		long long ccount=0;
		for (int i=0;i<r;i++) {
			ctrip++;

			long long count = 0;
			int end = 0;
			for (int j=0;j<n;j++) {
				int val = g[(cur + j) % n];
				if (count + (long long) val > (long long) k)
					break;
				count += val;
				ccount += val;
				res += val;
				end = (cur + j + 1) % n;
			}

			pos.push_back(cur);
			counts.push_back(ccount);

			for (int j=0;j<pos.size();j++) {
				if (pos[j] == end) {
					int cycles = (r - i - 1) / (ctrip - j);
					if (cycles > 0) {
						i += (cycles * (ctrip - j));
						long long init = 0;
						if (j > 0) init = counts[j-1];
						res += ((long long) cycles) * (ccount - init);
					}
					break;
				}
			}

			cur = end;
		}

		cout << "Case #" << (z+1) << ": ";
		cout << res << endl;
	}
}