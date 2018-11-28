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

int main() {
	freopen("C:\\Projects\\GCJ\\input", "rt", stdin);
	freopen("C:\\Projects\\GCJ\\output.txt", "wt", stdout);

	int c;
	cin >> c;
	for (int z=0;z<c;z++)
	{
		int n,temp;
		cin >> n;
		vector<int> a,b;
		for (int i=0;i<n;i++) {
			cin >> temp;
			a.push_back(temp);
			cin >> temp;
			b.push_back(temp);
		}

		int count = 0;
		for (int i=0;i<n;i++) {
			for (int j=i+1;j<n;j++) {
				if ((a[i] > a[j] && b[i] > b[j]) || (a[i] < a[j] && b[i] < b[j])) continue;
				count++;
			}
		}

		cout << "Case #" << (z+1) << ": " << count << endl;
	}

	exit(0);
}
