// google-code-jame2010.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define S(X) ((int)(X).size())
#define FOR(I, N) for (int I=0; I<N;++I)
#define fori(N) FOR(i,N)
#define forj(N) FOR(j,N)
#define fork(N) FOR(k,N)
#define P(a,b) make_pair((a),(b))

typedef long long LL;
typedef unsigned long long ULL;

const double eps = 1e-11;
const double pi=acos(-1.0);

template<typename T, typename U> U cast(T arg){
    ostringstream oss;
    oss << arg;
    istringstream iss(oss.str());
    U rv;
    iss >> rv;
    return rv;
}

using namespace std;



int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;

	int f[30];

	f[0] = 1;
	for (int i = 1; i < 30; ++ i) {
		f[i] = f[i-1] * 2 + 1;
	}

	fori(T) {
		int N;
		int K;
		cin >> N >> K;
		
		N --;

		if (K % (f[N] + 1) == f[N]) {
			cout << "Case #" << (i+1) << ": ON\n";
		} else {
			cout << "Case #" << (i+1) << ": OFF\n";
		}
	}

	return 0;
}

