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
#include <utility>
#include <conio.h>
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

const double pi = 2*acos(0.0);

int main() 
{
	freopen("B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T, t, N, S, p, ti, resp, timod, tidiv, respcopy;

	cin >> T;
	For(t, 1, T) 
	{
		cin >> N >> S >> p;

		resp=0;
		For(i, 1, N)
		{
			cin >> ti;

			timod = ti % 3;
			tidiv = ti / 3;

			// Without surpricing
			respcopy = resp;
			switch (timod)
			{
				case 0: if (tidiv>=p) resp++; break;
				case 1: if (tidiv+1>=p) resp++; break;
				case 2: if (tidiv+1>=p) resp++; break;
			}

			// with surpricing
			if (respcopy == resp)
			{
				if (S > 0)
				{
					respcopy = resp;

					switch (timod)
					{
						case 0: if (tidiv+1>=p && tidiv>0) resp++; break;
						case 2: if (tidiv+2>=p) resp++; break;
					}
					if (resp > respcopy)
						S--;
				}
			}
		}

		printf("Case #%d: %d\n", t, resp);
	}

	fclose (stdin);
	fclose (stdout);

	exit(0);
}
