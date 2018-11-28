/*
 * Paweł Barszcz (nkoder)
 *
 * Google Code Jam
 * Qualification Round - Problem A: Saving the Universe
 * (stu.cpp)
 */
#include <iostream>
#include <string>
#include <map>
using namespace std;

const int MAX_N = 20;
const int MAX_S = 100;
const int MAX_Q = 1000;

map <string, int> engines;

void reset_engines () {
	map <string, int> :: iterator I;
	for (I = engines.begin(); I != engines.end(); ++I) {
		I->second = 0;
	}
}

int main () {

	int N,S,Q;
	string engine;

	scanf("%d\n", &N);
	int used;
	int counter;
	for (int n=1; n<=N; ++n) {
		scanf("%d\n", &S);
		engines.clear();
#ifdef TEST
		cout << "* Wyszukiwarki ("<<S<<"): " <<endl;
#endif
        for (int s=0; s<S; ++s) {
			getline(cin, engine);
#ifdef TEST
			cout << "* wczytałem: " << engine << endl;
#endif
			engines[engine] = 0;
		}

		scanf("%d\n", &Q);
		used = 0;
		counter = 0;
#ifdef TEST
		cout << "* Zapytania ("<<Q<<"): " <<endl;
#endif
		for (int q=0; q<Q; ++q) {
			getline(cin, engine);
#ifdef TEST
			cout << "* wczytałem: " << engine << endl;
#endif
			if (engines[engine] == 0) {
				engines[engine] = 1;
				used++;
			}
			if (used == S) {
				counter++;
				reset_engines();
				engines[engine] = 1;
				used = 1;
			}
		}

		cout << "Case #" << n << ": " << counter << endl;
	}

	return 0;
}

