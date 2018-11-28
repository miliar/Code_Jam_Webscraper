/*
 * A.cpp
 *
 *  Created on: May 23, 2010
 *      Author: lsyl
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <string>
#include <cmath>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cstring>


using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i, n) for((i)=0; (i)<(int)(n); (i)++)
#define REP2(i, n) for((i)=1; (i)<=(int)(n); (i)++)
#define REP3(i, n) for((i)=(int)(n)-1; (i)>=0; (i)--)




//ifstream fin("A-small.in");
//ofstream fout("A-small.out");



int main() {
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
    int CASES, cn;
    fin >> CASES;
   REP2(cn, CASES) {
    	int N; int i, j;
    	fin >> N;
    		int A[1000];
    		int B[1000];
    		int l[N][N];
    		int r[N][N];
    		//fin >> N;
    		//cerr << "N is: " << N << endl;

    		memset(l, 0, sizeof(l));
    		memset(r, 0, sizeof(r));
    		//memset(A, 0, sizeof(A));
    		//memset(B, 0, sizeof(B));

    		REP(i, N) {
    			fin >> A[i]; fin >> B[i];
    			//cerr << A[i] << " " << B[i] << endl;
    		}
    		REP(i, N) REP(j, N) {
    			l[i][j] = A[i]-A[j];
    			l[j][i] = l[i][j];
    		}
    		REP(i, N) REP(j, N) {
    				r[i][j] = B[i]-B[j];
    				r[j][i] = r[i][j];
    			}

    		int ans = 0;
    		REP(i, N) REP(j, N) {
    			if(l[i][j]*r[i][j]<0) ans++;
    		}


    		fout << "Case #" << cn << ": " << ans/2 << endl;
    		cerr << "Case #" << cn << ": " << ans/2 << endl;
    }
    return 0;
}
