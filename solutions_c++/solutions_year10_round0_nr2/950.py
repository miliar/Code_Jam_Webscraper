#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <list>
#include <cln/cln.h>
using namespace std;
using namespace cln;

typedef long long int64;
typedef unsigned long long uint64;

#define FOR(i, a, b) for (uint64 i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (uint64 i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (uint64 i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (uint64 i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

template<class T>
T gcd(T m, T n)
{
  if (m < T(0) || n < T(0))
  {
    return T(-1);
  }

  T r;
  while (T(0) < n)
  {
		T r = m;
		while(r >= n){
			r -= n;
		}
    //r = m % n;
    m = n;
    n = r;
  }
  return m;
}


int main() {
	freopen("input_b.txt", "rt", stdin);
	freopen("output_b.txt", "wt", stdout);

	uint64 T, N;
	scanf("%lld", &T);

	cl_I g;
	vector<cl_I> gl;

	FOR(test, 1, T) {
		scanf("%lld", &N);

		gl.clear();
		REP(i, N) {
			cin >> g;
			gl.push_back(g);
		}
		//gl.push_back(0);
		sort(gl.begin(),gl.end(),std::greater<cl_I>());

		cl_I m,n;
		cl_I Euros=0;
		m=gl[0]-gl[1];
		if (N>2){
			FOR(i, 1, N-2) {
				n=gl[i]-gl[i+1];
				m=gcd(m,n);
			}
		}
		cl_I r1=gl[N-1];//-gl[N];
		cl_I r2 = r1;
		while(r2 >= m){
			r2 -= m;
		}
		cl_I ans;
		if (m==1||r2==0) {ans=0;
		}else{
			ans=m-r2;
		}
		
		cout << "Case #" << test << ": " << ans << endl;
	}

	exit(0);
}
