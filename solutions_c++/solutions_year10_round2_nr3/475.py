/*
 * Google Code Jam template :-)
 */

#include <iostream>
#include <string>
//#include <sstream>
//#include <algorithm>
//#include <vector>
//#include <ctype.h>
//#include <assert.h>
//#include <math.h>
//#include <set>
//#include <map>

using namespace std;

typedef unsigned idx;
typedef unsigned long num;

#define maxN 25
#define modulo 100003
num sol[maxN+1][maxN+1]; //sol[n][k] == how many sets S under {2..n} of cardinality k?
num chooses[maxN+1][maxN+1]; //binomial coefs mod modulo

void computeBC(idx row)
    //assumes all for t<row is precomputed
{
    chooses[row][0] = chooses[row][row] = 1;
    for(idx i=1; i<row; ++i)
    {
	chooses[row][i] = 0;
	chooses[row][i] += chooses[row-1][i-1];
	chooses[row][i] += chooses[row-1][i];
	chooses[row][i] %= modulo;
    }
}

void compute(idx n)
    //assumes all for m<n is precomputed
{
    sol[n][1] = 1;

    for(idx k=2; k<n; ++k) //compute sol[n][k]: |S|=k => S is k-th elem.
    {
	sol[n][k] = 0;
	for(idx t=1; t<k; ++t) //|S\cap{2..m}|=t
	{
	    sol[n][k] += sol[k][t] * chooses[n-k-1][k-t-1];
	    sol[n][k] %= modulo;
	}
    }
}

void solve(const num t)
{
    idx n;
    num sum=0;

    cin >> n;

    for(idx k=1; k<n; ++k)
    {
	sum += sol[n][k];
	sum %= modulo;
    }
    cout << "Case #" << t << ": " << sum << endl;
}

int main(void)
{
    num T;

    for(idx i=0; i<=maxN; ++i) computeBC(i);
    for(idx i=2; i<=maxN; ++i) compute(i);

    cin >> T;
    for(num t=1; t<=T; ++t) solve(t);

    return 0;
}
