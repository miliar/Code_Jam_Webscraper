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
#include <climits>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <stdio.h>
#include <conio.h>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

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

// Compare for QuickSort
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}


// Global variables


void Next (int& pCurrent, int& pN)
{
	pCurrent++;
	if (pCurrent == pN)
		pCurrent = 0;
}

int main() 
{
    /* Files */
    ifstream fin ("C-small.in");
	ofstream fout ("C-smal.out");
    
    /* Variables */
    int T, R, k, N;
	int g[1001];
	int64 Resp;
    
    /* Read File */
    fin >> T;
    For (n, 1, T)
    {
        // Read Case
        fin >> R >> k >> N ;
		Rep(i, N)
			fin >> g[i];

		// Process
		// Find cyclic point
		int Cyclic = 0;
		int Current = 0;
		int CurrentBoard;
		Resp = 0;
		do
		{
			Cyclic++;
			int OnBoard = 0;
			int nGroups = 0;
			while (((OnBoard + g[Current]) <= k) && (nGroups < N))
			{
				nGroups++;
				OnBoard += g[Current];
				Resp += g[Current];
				Next(Current, N);
			}
		} while ((Current != 0) && (Cyclic < R));
		// Calculate by cyclic
		if (R >= Cyclic)
		{
			int CyclicQuantity = R / Cyclic;
			Resp = Resp * CyclicQuantity;
			CurrentBoard = Cyclic * CyclicQuantity;	
			// Remainder boards
			while (CurrentBoard < R)
			{
				CurrentBoard++;
				int OnBoard = 0;
				int nGroups = 0;
				while (((OnBoard + g[Current]) <= k) && (nGroups < N))
				{
					OnBoard += g[Current];
					Resp += g[Current];
					Next(Current, N);
				}
			}
		}
		  
        /* Print answer */
        fout << "Case #" << n << ": " << Resp << endl;
    }
    
    //getch();
    //cin.get();
    fout.close();
    fin.close();
	exit(0);
}
