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

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

int main () {
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
	
    // insert code here...
	
	int T,N,i;
	uint64 V;
	uint64 K;
	
	cin >> T;
	
	for(i=0; i<T; i++)
	{
		cin >> N >> K;
		V = pow((double)2,(int)N);
		
		// check
		if( K < V - 1 )
		{
			cout << "Case #" << i+1 << ": " << "OFF" <<endl;
		}
		else if(K == V - 1)
		{
			cout << "Case #" << i+1 << ": " << "ON" <<endl;
		}
		else
		{
			K %= V;
			
			if(K == V - 1)
			{
				cout << "Case #" << i+1 << ": " << "ON" <<endl;
			}
			else
			{
				cout << "Case #" << i+1 << ": " << "OFF" <<endl;
			}
		}
	}
		
    return 0;
}
