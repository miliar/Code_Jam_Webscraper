#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <math.h>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cstdio>

using namespace std;

typedef vector <int> VI;
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(i, a, b) for (int i = (a); i <= (b); ++i)
#define PB push_back
#define ALL(x) x.begin(),x.end()

long double High = 0;

long long lnko(long long a, long long b) {
	long long rez = 1;
	long long cur = 2;
	while (a > 1 || b > 1) {
		long double testA = a, testB = b;
		if (cur > testA / cur && cur > testB / cur) {
			if (High / a < rez) return 0;
			else {
				rez *= a;
				if (b % a == 0) b /= a;
				a = 1;
			}
			if (High / b < rez) return 0;
			else {
				rez *= b;
				if (a % b == 0) a /= b;
				b = 1;
			}
		}

		while (a % cur == 0) {
			if (High / cur < rez) return 0;
			rez *= cur;
			a /= cur;
			if (b % cur == 0)
				b /= cur;
		}
		while (b % cur == 0) {
			if (High / cur < rez) return 0;
			rez *= cur;
			b /= cur;
			if (a % cur == 0)
				a /= cur;
		}
		cur++;
	}
	return rez;
}

long long lnko_V(vector <long long> V) {
	if (V.size() == 0) return 0;
	long long rez = V[0];
	for (size_t i = 1; i < V.size(); i++) {
		long long tmp = lnko(rez, V[i]);
		if (tmp == 0) return 0;
		else rez = tmp;
	}
	return rez;
}

int main() {
	ifstream in("C.in");
	ofstream out("C.out");

	int T = 0;
	in >> T;
	for (int k = 1; k <= T; k++) {
		cout << k << endl;
		long long N, L, H;
		in >> N >> L >> H;
		High = 2 * H;
		vector <long long> V;
		for (int i = 0; i < N; i++) {
			long long a;
			in >> a;
			if (a > 1)
				V.push_back(a);
		}

		sort(ALL(V));
		vector <long long> osztok;
		long long large = V[V.size()-1];
		for (long long i = 1; i * i <= large; i++) {
			if (large % i == 0) {
				if (L <= i && i <= H) osztok.push_back(i);
				if (L <= large / i && large / i <= H) osztok.push_back(large / i);
			}
		}

		bool found = false;
		long long rez = 0;
		sort(ALL(osztok));
		for (size_t i = 0; i < osztok.size(); i++) {
			bool flagG = true;
			for (size_t j = 0; j < V.size(); j++) {
				bool flag = false;
				if (V[j] % osztok[i] == 0) flag = true;
				if (osztok[i] % V[j] == 0) flag = true;
				if (!flag) {
					flagG = false;
					break;
				}
			}
			if (flagG) {
				found = true;
				rez = osztok[i];
				break;
			}
		}

		if (found) {
			out << "Case #" << k << ": " << rez << endl;
		} else {
			long long oszto = lnko_V(V);
			if (oszto > H || oszto == 0) {
				out << "Case #" << k << ": NO" << endl;
			} else {
				long long tmp = L / oszto;
				if (L % oszto != 0) tmp++;
				oszto *= tmp;
				if (L <= oszto && oszto <= H) {
					out << "Case #" << k << ": " << oszto << endl;
				} else {
					out << "Case #" << k << ": NO" << endl;
				}			
			}
		}
	}

	return 0;
}