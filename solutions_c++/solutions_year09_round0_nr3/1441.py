using namespace std;
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<string> vs;


#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define GETS(s) getline(cin, s);
#define GETDS(s, d) getline(cin, s, d);
#define GETI(i) { string _s; getline(cin, _s); i = atoi(_s.c_str()); }
#define GETDI(i, d) { string _s; getline(cin, _s, d); i = atoi(_s.c_str()); }

void disp_vect(string name, vector<int> &v) {
	cout << name << ":";
	for (int i = 0; i < v.size(); i++) {
		cout << "[";
		cout << v.at(i);
		//cout << (*it).from << "|" << (*it).d << "-" << (*it).at ;
		cout << "]-";
	};
	cout << "|" << endl;
}

//----------------------------------------------------------------------------
int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int result;
	int N;
	string L;
	string W = "welcome to code jam";
	vc T;
	vi X, Y, *A, *B;
	int ti, wi, ai, bi;

	GETI(N);
	FOR(TestCase, 1, N) {
		result = 0;
		GETS(L);
		T.clear();
		X.clear();
		Y.clear();
		for (int i = 0; i < L.size(); i++) {
			T.push_back(L[i]);
			X.push_back(0);
			Y.push_back(0);
		}
		A = &X;
		B = &Y;
		// algorithm
		for (ti = T.size() - 1; ti >= 0; ti--) {
			if (T[ti] == W[W.size() - 1])
				(*A)[ti] = 1;
		}
		//disp_vect("A:", *A);
		for (wi = W.size() - 1; wi > 0; wi--) {
			for (ai = T.size() - 1; ai > 0; ai--) {
				if (T[ai] == W[wi]) {
					for (bi = ai - 1; bi >= 0; bi--) {
						if (T[bi] == W[wi - 1]) {
							(*B)[bi] += (*A)[ai];
							(*B)[bi] %= 10000;
						}
					}
				}
			}
			//disp_vect("A:", *A);
			//disp_vect("B:", *B);
			swap(A, B);
			for (bi = T.size() - 1; bi >= 0; bi--)
				(*B)[bi] = 0;

		}
		for (ti = T.size() - 1; ti >= 0; ti--) {
			if (T[ti] == W[0]) {
				result += (*A)[ti];
				result %= 10000;
			}
		}
		printf("Case #%d: %4.4d\n", TestCase, result);
	}
	return EXIT_SUCCESS;
}
