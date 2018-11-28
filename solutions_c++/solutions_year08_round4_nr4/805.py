#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

typedef int resulttype;

void skipEOL() { string foo; getline(cin,foo); }

#define MAXS 50000
#define MAXK	16


int M[MAXK][MAXK][1<<MAXK];
int M2[MAXK][MAXK][1<<MAXK];

int Score[MAXK][MAXK];
int Back[MAXK][MAXK];

#define BAD -100000

int K;

resulttype OneCase() {
	cerr << "ONE CASE" << endl;

	resulttype result;

	
	
	string S;
	cin >> K;
	cin >> S;
	int L = S.length();
	for (int A=0; A<K; ++A) for (int B=0; B<K; ++B) {
		int score = 0;
		for (int i=0; i<L; i+=K) if (S[i+A]==S[i+B]) ++score;
		if (A==B) score = BAD;
		Score[A][B] = score;
		int t = score;
		score = 0;
		for (int i=K; i<L; i+=K) if (S[i+A-K]==S[i+B]) ++score;
		if (A==B) score = BAD;
		Back[A][B] = score;
		cerr << A << "," << B << ": " << t << "/" << score << endl;
	}

	int opt = -1;

	unsigned all = (1<<K)-1;

	
	for (int Q = 0; Q<=all; ++Q) for (int A=0; A<K; ++A) for (int B=0; B<K; ++B) {
		if (A==B && (Q==(1<<A))) M[A][B][Q] = 0; else M[A][B][Q] = BAD;
	}

	
	for (int now = 1; now<K; ++now) {
		memset(M2,-2,sizeof(M2));
		//cerr << "?? =" << M2[0][0][0] << endl;
		for (int B = 0; B<K; ++B) for (int C=0; C<K; ++C) if (C!=B) {
			int cost0 = Score[C][B]; int bm = 1<<B; int bmcm = bm + (1<<C);
			for (int A=0; A<K; ++A) {
				for (int Q = 0; Q<=all; ++Q) 
					if ((Q & bmcm)==bmcm) {
						int t = M[A][C][Q-bm] + cost0;
						if (M2[A][B][Q] < t) M2[A][B][Q] = t;
					}
				// A,B,Q <= A,C,Q' + cost0;
			}
		}
		memcpy(M,M2,sizeof(M2));
	}
	

	for (int i=0; i<K; ++i) for (int j=0; j<K; ++j) {
		int sc = M[i][j][all] + Back[j][i];
		if (sc > opt) opt = sc;
	}
	cerr << L << " " << opt << endl;

	result = L -opt;
	return result;
}

int main() {
	int Anz;
	cin >> Anz;
	skipEOL();
	for (int run=1; run<=Anz; ++run) {
		resulttype result = OneCase();

		cout << "Case #" << run << ": " << result << endl;
	}
	return 0;
};
