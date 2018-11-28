#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int n;
int na;
int nb;
int t;
int aleave[100];
int aarrive[100];
int bleave[100];
int barrive[100];

int aneed;
int bneed;

int aleft;
int bleft;

int atimes[1440];
int btimes[1440];

int compare(const void* a, const void* b) {
	return *((int *)a) -  *((int *)b);
}

int main() {
	fstream in;
	in.open("prob2.in", fstream::in);
	fstream out;
	out.open("prob2.out", fstream::out);

	in >> n; 
	for (int i = 0; i < n; i++) {
		in >> t;
		in >> na;
		in >> nb;
		int t1,t2,t3,t4;
		char temp;
		for (int a = 0; a < na; a++) {
			in >> t1 >> temp >> t2 >> t3 >> temp >> t4;
			aleave[a] = t1 * 60 + t2;
			barrive[a] = t3 * 60 + t4 + t;
		}
		for (int b = 0; b < nb; b++) {
			in >> t1 >> temp >> t2 >> t3 >> temp >> t4;
			bleave[b] = t1 * 60 + t2;
			aarrive[b] = t3 * 60 + t4 + t;
		}
		qsort(aleave,na,sizeof(int),compare);
		qsort(bleave,nb,sizeof(int),compare);
		qsort(aarrive,nb,sizeof(int),compare);
		qsort(barrive,na,sizeof(int),compare);

		for (int c = 0; c < 1440; c++) {
			atimes[c] = 0;
			btimes[c] = 0;
		}
		for (int d = 0; d < na; d++) {
			atimes[aleave[d]] += 1;
			btimes[barrive[d]] -= 1;
		}
		for (int e = 0; e < nb; e++) {
			atimes[aarrive[e]] -= 1;
			btimes[bleave[e]] += 1;
		}

		aleft = 0;
		bleft = 0;
		aneed = 0;
		bneed = 0;

		for (int x = 0; x < 1440; x++) {
			if (atimes[x] > aleft) {
				aneed += atimes[x] - aleft;
				aleft = atimes[x];
			}
			if (btimes[x] > bleft) {
				bneed += btimes[x] - bleft;
				bleft = btimes[x];
			}
			aleft -= atimes[x];
			bleft -= btimes[x];
		}
		out << "Case #" << i + 1 << ": " << aneed << " " << bneed << endl;
	}

	in.close();
	out.close();

	return 0;
}