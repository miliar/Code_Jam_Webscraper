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

int is_ugly(ll v)
{
	if (v < 0) { v = -v; }
	if (v == 0 ) { return 1; }
	if (v % 2 == 0) { return 1;}
	if (v % 3 == 0) { return 1;}
	if (v % 5 == 0) { return 1;}
	if (v % 7 == 0) { return 1;}
	return 0;
}

int g_len;
int calc_ugly(const char*digits, ll amari, int len)
{
	int sum = 0;
	if (len == 0) {
		return is_ugly(amari);
	}
	for (int i = 1; i <= len; i++) {
		/* val */
		ll val = 0;
		for (int j = 0; j < i; j++) {
			val *= 10;
			val += digits[j] - '0';
		}

		/* + */
		sum += calc_ugly(digits+i, amari + val, len-i);
		/* - */
		if (g_len != len)
		sum += calc_ugly(digits+i, amari - val, len-i);
	}
	return sum;
}

int main(int argc, char **argv)
{
	int Cn;
#ifdef DEBUG
	DOUT.open("/dev/stdout");
#else
	DOUT.open("/dev/null");
#endif

	cin >> Cn;
	DOUT << "Cn:" << Cn << endl;
	F1(Ci,Cn+1) {
		/* read INPUT */
		string digits;
		cin >> digits;
//2,3,5,7 0 is ugly
		/* debug */
//		DOUT << "digits:" << digits << endl;

		/* solve problem */
		g_len = digits.size();
		int sum = calc_ugly(digits.c_str(), 0, digits.size());

		/* answer */
		cout << "Case #" << Ci << ": " << sum << endl;
	}
}
