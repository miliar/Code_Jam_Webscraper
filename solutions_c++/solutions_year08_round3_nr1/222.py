#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <set>
#include <vector>
#include <iostream>
#include <fstream>

#ifdef DEBUG
#define DPF(...) printf(__VA_ARGS__)
#else
#define DPF(...) 
#endif

using namespace std;
ofstream DOUT;

typedef long long ll;
typedef unsigned long long ull;
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<n;i++)

/*
void sample()
{
	char buf[1024];
	while (fgets(buf, sizeof(buf), stdin) > 0) {
		buf...;
	}
}
*/
/* global */

int main(int argc, char **argv)
{
	ll Cn;
#ifdef DEBUG
	DOUT.open("/dev/stdout");
#else
	DOUT.open("/dev/null");
#endif

	cin >> Cn;
	DOUT << "Cn:" << Cn << endl;
	F1(Ci,Cn+1) {
		/* read INPUT */
		ll P;
		cin >> P;
		ll K;
		cin >> K;
		ll L;
		cin >> L;
		vector<ll> f; // freq
		f.resize(L);
		F0(i,L) cin >> f[i];


		/* debug */
		DOUT << "P:" << P << endl;
		DOUT << "K:" << K << endl;
		DOUT << "L:" << L << endl;
		F0(i,L) DOUT << " " << f[i];
		DOUT << endl;

		/* solve problem */
		sort(f.begin(), f.end());
		vector<ll> s; // strok
		s.resize(K, 1);

		ll sum = 0;
		F0(i,L) {
			ll num = f[L-i-1];

			ll min = 99999;
			ll key_pos = 0;
			ll j;
			for (j = 0; j < K; j++) {
				if (s[j] < min) {
					min = s[j];
					key_pos = j;
				}
			}

			sum += s[key_pos] * num;
			s[key_pos]++;
		}

		/* answer */
		cout << "Case #" << Ci << ": " << sum << endl;
	}
}
