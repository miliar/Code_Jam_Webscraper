#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long int datum;

datum my_sgn(datum x) {
	return (x>0)-(x<0);
}
datum my_abs(datum x) {
	return x*my_sgn(x);
}
datum gcd(datum _a, datum _b)
{
	datum c = 0;
	datum a = max(_a, _b);
	datum b = min(_a, _b);
	if(!b) { return a; }
	while(c = a%b) {
		a = b;
		b = c;
	}
	return b;
}

int solve(datum N, datum D, datum G) {
	datum D_ = 100 - D;
	datum G_ = 100 - G;
	datum Dk = gcd(D, D_);
	datum Gk = gcd(G, G_);
	datum Dx = D / Dk, Dy = D_ / Dk;
	datum Gx = G / Gk, Gy = G_ / Gk;

	if(Dx+Dy>N) { return 1; }
	if(Dx!=0 && Gx == 0) { return 1; }
	if(Dy!=0 && Gy == 0) { return 1; }
	return 0;
}

int main(void)
{
	int T;
	cin >> T;
	string result[2] = {"Possible", "Broken"};

	for(int t = 0; t < T; ++t) {
		datum N, D, G;
		cin >> N >> D >> G;
		cout << "Case #" << (t+1) << ": " << result[solve(N, D, G)] << endl;
	}
	return 0;
}
