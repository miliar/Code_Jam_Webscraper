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
#include <string>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
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

#ifndef NOMINMAX
  #ifndef max
    #define max(a,b) (((a) > (b)) ? (a) : (b))
  #endif
  #ifndef min
    #define min(a,b) (((a) < (b)) ? (a) : (b))
  #endif
#endif 

int cases, P, Q, num;

vector<int> prisoners;
bool c[101];


int do_case()
{
	memset(c, false, sizeof(c));
	int bribe = 0;

	For(i, 0, prisoners.size()-1)
	{
		c[prisoners[i]-1] = true;	
		int k = prisoners[i]-2;
		while (k >= 0 && !c[k])
		{
			bribe++;
			k--;
		}

		k = prisoners[i];
		while (k < P && !c[k])
		{
			bribe++;
			k++;
		}
	}

	return bribe;
}

int main()
{
	freopen("E:\\dev\\gcj\\C\\Debug\\C-small-attempt1.in", "r", stdin);
	int ccc = 1;
	cin >> cases;
	For(i, 0, cases-1)
	{
		cin >> P; cin >> Q;

		prisoners.clear();
		For(j, 0, Q-1)
		{
			cin >> num;
			prisoners.push_back(num);
		}

		int minb = 3457934875934875;
		do 
		{
			int a = do_case();
			minb = min(a, minb);
		} while(next_permutation(prisoners.begin(), prisoners.end()));

		printf("Case #%d: %d\n", ccc++, minb);
	}

	return 0;
}
