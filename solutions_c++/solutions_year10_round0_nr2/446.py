#include <cstdio>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <math.h>
#include <limits.h>
#include <float.h>
#include <algorithm>
#include <iostream>
#include <gmpxx.h>

using namespace std;

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define FORR(a,s,b) for(int a=s;a<=b;a++)
#define CLR(a,b) memset(a,b,sizeof(a))
#define VI vector<int>
#define VS vector<string>
               
 
int main()
{
	typedef mpz_class INT;
	int C;
	cin >> C;

	INT t[1024];

	FORR(cn,1,C) {
		cout << "Case #"<<cn<<": ";
		int n;
		cin >> n;

		int latest=0;

		FOR(i,n) {
			cin >> t[i];
			if(t[i] < t[latest]) latest=i;
		}
		if(latest) swap(t[0],t[latest]); n--;
		latest=0;

		FORR(i,1,n) {
			t[i]-=t[0];
		}

		FORR(i,2,n)
			mpz_gcd (t[1].get_mpz_t(), t[1].get_mpz_t(), t[i].get_mpz_t());

		INT mod = t[0]%t[1];
		if(mod != 0) {
			mod = t[1]-mod;
		}

		cout << mod << "\n";

	}

	return 0;
}
