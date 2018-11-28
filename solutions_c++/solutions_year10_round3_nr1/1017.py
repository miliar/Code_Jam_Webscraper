#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
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
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

int main (int argc, char * const argv[]) {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int T,i,N,j,k;
	int A[1000],B[1000];
	long int count;
	
	cin >> T;
	
	for(i=0; i<T; i++)
	{
		count=0;
		cin >> N;
		
		for(j=0; j<N; j++)
		{
			cin >> A[j] >> B[j];
		}
		
		for(j=0; j<N; j++)
		{
			for(k=j+1; k<N; k++)
			{
				if( (A[j] > A[k] && B[j] < B[k]) || (A[j] < A[k] && B[j] > B[k]) )
				{
					count++;
				}
			}
		}
		
		cout << "Case #" << i+1 << ": " << count << endl;
	}
    return 0;
}
