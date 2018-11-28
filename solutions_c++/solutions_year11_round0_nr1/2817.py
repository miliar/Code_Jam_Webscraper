/**
 * bot-trust.cpp
 *
 * @date May 6, 2011
 * @author Arpan
 **/

#include <iostream>
#include <vector>

//#define DEBUG

using namespace std;

int main(int argc, char* argv[]) {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		long sum = 0;
		int N;
		cin >> N;
		char R[(const int)N];
		int P[(const int)N];
		char r; int p;
		for(int i = 0; i < N; i++) {
			cin >> r >> p;
			R[i] = r;
			P[i] = p;
		}

		int Bpos = 1, Opos = 1;
		int Bdir = 0, Odir = 0;
		int Bdst = 0, Odst = 0;
#ifdef DEBUG
		cout << endl << N << ':' << endl;
#endif
		for(int b = 0, o = 0; b < N || o < N;) {
			while(b < N && (R[b] != 'B')) b++;
			while(o < N && (R[o] != 'O')) o++;
			if(b < N) {
				Bdst = P[b] - Bpos;
				if(Bdst == 0)
					Bdir = 0;
				else if(Bdst < 0) {
					Bdir = -1;
					Bdst *= -1;
				}
				else
					Bdir = 1;
			}
			else
				Bdst = Bdir = 0;

			if(o < N) {
				Odst = P[o] - Opos;
				if(Odst == 0)
					Odir = 0;
				else if(Odst < 0) {
					Odir = -1;
					Odst *= -1;
				}
				else
					Odir = 1;
			}
			else
				Odst = Odir = 0;

#ifdef DEBUG
			cout << "sum: " << sum << endl;
			if(b < N)
				cout << "B: b=" << b << " Bpos=" << Bpos << " Bnxt=" << P[b] << " Bdir=" << Bdir << " Bdst=" << Bdst << endl;
			if(o < N)
				cout << "O: o=" << o << " Opos=" << Opos << " Onxt=" << P[o] << " Odir=" << Odir << " Odst=" << Odst << endl;
#endif

			if(b < N || o < N) {
				if(b < o) {
					sum += (Bdst + 1);
					Bpos = Bpos + (Bdir * Bdst);
					Opos = Opos + (Odir * min(Odst, (Bdst + 1)));
					b++;
				}
				else {
					sum += (Odst + 1);
					Opos = Opos + (Odir * Odst);
					Bpos = Bpos + (Bdir * min(Bdst, (Odst + 1)));
					o++;
				}
			}
		}
		cout << "Case #" << t << ": " << sum << endl;
	}
}
