#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <list>
#include <string>
#include <queue>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>
using namespace std;

#define forsn(i, i0, n) for(int i = i0; i < (int)(n); ++i)
#define forn(i, n) forsn(i,0,n)
#define forall(it, X) for(typeof((X).begin()) it = (X).begin();it != (X).end(); ++it)

typedef vector<int> vint;

void mask2set(int n, vint& set)
{
	int pos = 0;
	while(n>0) {
		set[pos] = n&1;
		n = n>>1;
		pos++;
	}
}

int solve(int N, vint& values)
{
	int MASK = pow(2,N);
	int max = -1;
	forn(m,MASK) {
		vint patrick(N,0);
		mask2set(m, patrick);

		int xor_patrick = 0;
		int xor_sean = 0;
		int sum_sean = 0;
		int sum_patrick = 0;
		forn(n,N){
			if(patrick[n]>0){
				xor_patrick = xor_patrick ^ values[n];
				sum_patrick += values[n];
			}else{
				xor_sean = xor_sean ^ values[n];
				sum_sean += values[n];
			}
		}

		if(xor_sean == xor_patrick && sum_patrick >0 && sum_sean>0){
			if(sum_sean > max){
				max = sum_sean;
			}
		}

	}
	return max;
}

int main(int argc, char **argv)
{
	int T;
	cin >> T;
	forn(t,T) {
		int N;
		cin >> N;
		vint values(N);
		forn(n,N){
			cin >> values[n];
		}

		int max = solve(N,values);


		if(max<0)
			cout << "Case #" << t+1 << ": NO" << endl;
		else
			cout << "Case #" << t+1 << ": " << max << endl;
	}

}

