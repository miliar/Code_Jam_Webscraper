#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

#define REP(I,N) for(int I=0 ; I<N ; I++)
#define SZ(A) ((int)(A).size())
#define PB push_back
#define F first
#define S second


int main() {

	int T;
	cin >> T;
	for(int t=0 ; t<T ; t++) {

		long long n, x;
		cin >> n;
		long long sum = 0;
		long long add = 0;
		long long mn = 10000001;
		REP(i, n) {
			cin >> x;
			if(mn > x) mn = x;
			add += x;
			sum ^= x;
		}
		
		if(sum != 0)
			printf("Case #%d: NO\n", t+1);
		else
			printf("Case #%d: %lld\n", t+1, add-mn);
	}
}
