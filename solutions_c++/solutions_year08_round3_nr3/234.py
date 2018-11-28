#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
using namespace std;

#define pb push_back
#define pi 2*acos(0.0)
#define inf 1000000000
#define all(c) (c).begin(), (c).end()

#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define fo(i,n) for(i=0;i<(n);++i)
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

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

const double eps = 1e-9;

int N;
long long X, Y, Z, A[500001], sign[500001], sums[500001], m, n, total;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int numCase;

	cin >> numCase;
	For(test, 1, numCase)
	{
		total = 0;
		cin >> n >> m >> X >> Y >> Z;
		For(i,0,m-1)
		{
			cin >> A[i];
		}

		For(i,0,n-1)
		{
			sign[i] = A[i % m];
			A[i % m] = (X * A[i % m] + Y * (i+1)) % Z;
		}

		For(i,0,n-1)
		{
			sums[i] = 1;
			For(j,0,i-1)
				if (sign[j]<sign[i]) sums[i] = (sums[i] + sums[j]) % 1000000007;
			total = (total + sums[i]) % 1000000007;
		}

		cout << "Case #" << test << ": "<< total <<endl;
		fflush(stdout);
	}

	return 0;
}

