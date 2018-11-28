#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>

using namespace std;

typedef long long 			LONGINT;
typedef unsigned long long 	ULONGINT;

typedef vector<int> 		INT_VEC;
typedef vector<string> 		STR_VEC;
typedef vector<double> 		DBL_VEC;

#define FOR_INC_INCL(i, a, b)		for (int i(a), max(b); i <= max; ++i)
#define FOR_INC_EXCL(i, a, b)		for (int i(a), max(b); i <  max; ++i)
#define FOR_DEC_INCL(i, a, b)		for (int i(a), min(b); i >= min; --i)
#define FOR_DEC_EXCL(i, a, b)		for (int i(a), min(b); i >  max; --i)

#define FOR(i, a, b)				FOR_INC_INCL(i, (a), (b))
#define FOR_D(i, a, b)				FOR_DEC_INCL(i, (a), (b))

#define ARR_SIZE(a)					(sizeof(a) / sizeof(*(a)))
#define ARR_SORT(a)					sort((a), (a) + ARR_SIZE(a))

#define VEC_ALL(v) 					(v).begin(), (v).end()
#define VEC_SORT(v)					sort( VEC_ALL(v) )

#define FOR_ALL(x, i)				for (int i(0), num(ARR_SIZE(x)); i < num; ++i)

#define FILL_NUM_WITH(x, c, n)		memset(x, (c), (n))
#define FILL_ALL_WITH(x, c)			memset(x, (c), sizeof(x))

#define REPEAT_INC(i, n)			for (int i(0), num(n); i < num; ++i)
#define REPEAT_DEC(i, n)			for (int i((n) - 1); i >= 0; ++i)

#define REP(i, n)	 				REPEAT_INC(i, n)
#define REP_D(i, n)	 				REPEAT_DEC(i, n)

template<typename T, typename S> T 	QCAST(S s)
{ T r; stringstream x; x << s; x >> r; return r; };

template<typename T> inline void 	CHECKMIN(T& a, T b) 	{ if (b < a) a = b; };
template<typename T> inline void 	CHECKMAX(T& a, T b) 	{ if (b > a) a = b; };
template<typename T> inline T 		SQR(T a) 				{ return a * a; };
template<typename T> inline int 	SIZE(const T& c) 		{ return (int)c.size(); };
