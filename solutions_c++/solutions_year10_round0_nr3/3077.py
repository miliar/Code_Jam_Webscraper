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
#include <deque>
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
	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
	
	uint64 T,N,i,j,k,sumR,x;
	uint64 R,K,M,r;
	
	cin >> T;
	// cout << T << endl;
	
	for(i=0; i<T; i++)
	{
		M=0;
		cin >> R >> K >> N;
		// cout << R <<" "<< K <<" "<< N << endl;
		
		deque<uint64>g(N);
		
		// input g's
		for(j=0; j<N; j++)
		{
			cin >> g[j];
			// cout << g[j] <<" ";
		}
		
		// per R
		for(r=0; r<R; r++)	// next R
		{
			for(j=0,sumR=0; j<N; j++)		// next g
			{	
				if(sumR + g[j] > K)
				{
					// push and pop
					for(k=0; k<j; k++)
					{
						x = g.front();
						g.pop_front();
						g.push_back(x);
					}
					// goto ENDR;
					break;
					
				}
				else
				{
					sumR += g[j];
				}
			}
			//ENDR:
			M += sumR;
		}
		
		cout << "Case #" << i+1 << ": " << M << endl;
		
	}
		
    return 0;
}
