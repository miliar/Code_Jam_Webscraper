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
#include <limits.h>


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
	int arr[1000];
	int in[1000];
	int next[1000];

	fori(T) {
		int R, K , N;
		cin >> R >> K >> N;
		forj(N) cin >> arr[j];

		forj(N) {
			int size = 0;
			size += arr[j];
			int ptr = (j + 1) % N;

			while (true) {
				if (size + arr[ptr] > K || ptr == j) {
					in[j] = size;
					next[j] = ptr;
					break;
				}
				
				size += arr[ptr];
				ptr = (ptr + 1) % N;
			}
		}

		set<int> states;
		int j = 0;
		while (true) {
			if (states.find(j) != states.end()) {
				break;
			}
			states.insert(j);
			j = next[j];
		}

		int s = j;
		int len = 0;
		ULL income = 0;
		len ++;
		income += in[s];
		while (next[s] != j) s = next[s], len ++, income += in[s];

		int blen = 0;
		s = 0;
		ULL left = 0;
		while (s != j) left += in[s], s = next[s], blen ++;

		int elen = (R - blen ) % len;

		ULL inend = 0;
		s = j;
		fork(elen) left += in[s], s = next[s];

		cout << "Case #" << (i + 1) << ": " << (income * ((R-blen) / len) + left) << endl;
	}


	return 0;
}