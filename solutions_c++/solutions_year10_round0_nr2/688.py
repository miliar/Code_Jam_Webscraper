#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

ifstream fin("B-small-attempt0.in");
ofstream fout("B-small.out");
typedef long long int ll;

ll x[1005];

inline ll gcd(ll a, ll b) {
	return b? gcd(b, a%b) : a;
}

int main() {
	int C;
	fin >> C;
	for(int i=0; i < C; i++) {
		int N;
		fin >> N;
		for(int j=0; j < N; j++) {
			ll t;
			fin >> t;
			x[j] = t;
		}
		sort(x, x + N);
		ll g = 0;
		for(int j=0; j < N-1; j++) {
			g = gcd(x[j+1] - x[j], g);
			cout << g << "\n";
		}
		ll r = x[0] % g;
		if(r == 0)
			fout << "Case #" << i+1 << ": " << 0 << "\n";
		else
			fout << "Case #" << i+1 << ": " << g - r << "\n";
			
	}
	return 0;
}
