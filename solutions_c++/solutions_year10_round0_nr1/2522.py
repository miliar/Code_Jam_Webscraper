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

// Global variables


int main() 
{
    /* Files */
    ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");
    
    /* Variables */
    int T, N, K;
	int Snaps;
	bool On;
    
    /* Read File */
    fin >> T;
    For (n, 1, T)
    {
        // Read Case
        fin >> N >> K;
		Snaps = 0;

		// Process
        For (i, 1, N)
        {
            Snaps = Snaps * 2 + 1;
        }
		On = false;
        if (K >= Snaps)
			if ((K % (Snaps + 1)) == Snaps)
				On = true;
              
        /* Print answer */
        fout << "Case #" << n << ": " << (On ? "ON" : "OFF") << endl;
    }
    
    //getch();
    //cin.get();
    fout.close();
    fin.close();
	exit(0);
}
