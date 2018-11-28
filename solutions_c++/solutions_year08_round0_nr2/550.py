#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

//const string FIN = "B-small-attempt1.in";
//const string FIN = "B.in";
const string FIN = "B-large.in";
const string FOUT = "B.out";

int N, NA, NB, T;
struct schedule {
	int s, e;
};
bool operator<(const schedule& X, const schedule& Y) {
	if (X.s != Y.s) return X.s < Y.s;
	if (X.e != Y.e) return X.e < Y.e;
	return true;
}
schedule A [100], B [100];
int getTime (string s) {
	int res = 0;
	res += (s [0] - '0') * 10 + s [1] - '0';
	res *= 60;
	res += (s [3] - '0') * 10 + s [4] - '0';
	return res;
}
int MA [100], MB [100];

int isStart (int iA) {
	for (int i = 0; i < NB; ++i)
	    if (MB [i] == 0 &&
	        A [iA].s >= B [i].e + T) return 0;
	return 1;
}
void markA (int iA) {
	int iB = 0;
	MA [iA] = 1;
	schedule c = A [iA];
	while (1) {
		while (iB < NB &&
			(MB [iB] ||
			(!MB [iB] && B [iB].s < c.e + T))) ++iB;
		if (iB == NB) break;
		MB [iB] = 1;
		c = B [iB];

		while (iA < NA &&
			(MA [iA] ||
			(!MA [iA] && A [iA].s < c.e + T))) ++iA;
		if (iA == NA) break;
		MA [iA] = 1;
		c = A [iA];
	}
}

void markB (int iB) {
	int iA = 0;
	MB [iB] = 1;
	schedule c = B [iB];
	while (1) {
		while (iA < NA &&
			(MA [iA] ||
			(!MA [iA] && A [iA].s < c.e + T))) ++iA;
		if (iA == NA) break;
		MA [iA] = 1;
		c = A [iA];

		while (iB < NB &&
			(MB [iB] ||
			(!MB [iB] && B [iB].s < c.e + T))) ++iB;
		if (iB == NB) break;
		MB [iB] = 1;
		c = B [iB];
	}
}
int main () {

	ifstream fin;
	ofstream fout;
	int n;
	fin.open (FIN.c_str());
	fout.open (FOUT.c_str());
	
	string s;
	fin >> N;
	//cout << n << endl;
	cout << N;
	for (int xxx = 1; xxx <= N; ++xxx) {
		cout << xxx << endl;
		fin >> T;
		fin >> NA >> NB;
		for (int i = 0; i < NA; ++i) {
			string t;
			fin >> t;
			A [i].s = getTime (t);
			fin >> t;
			A [i].e = getTime (t);
		}
		for (int i = 0; i < NB; ++i) {
			string t;
			fin >> t;
			B [i].s = getTime (t);
			fin >> t;
			B [i].e = getTime (t);
		}
		cout << "Sorting.." << endl;
		sort (A, A + NA);
		sort (B, B + NB);
		
		//for (int i = 0; i < NA; ++i)
		//    cout << A [i].s / 60 << ":" << A [i].s % 60<< " " << A [i].e / 60 << ": " << A [i].e % 60<< endl;
		memset (MA, 0, sizeof (MA));
		memset (MB, 0, sizeof (MB));
		int resA = 0, resB = 0;
		int iA, iB;
		iA = iB = 0;
		while (iA < NA || iB < NB) {
			while (iA < NA && MA [iA]) ++iA;
			while (iB < NB && MB [iB]) ++iB;
			if (iA == NA && iB == NB) break;
			if (iA == NA) {
				++resB; markB (iB);
			} else
			if (iB == NB) {
				++resA; markA (iA);
			} else
			if (A [iA] < B [iB]) {
				++resA; markA (iA);
			} else {
				++resB; markB (iB);
			}
		}

		for (int i = 0; i < NA; ++i) cout << MA [i] << " "; cout << endl;
		for (int i = 0; i < NB; ++i) cout << MB [i] << " "; cout << endl;
		
		fout << "Case #" << xxx << ": " << resA << " " << resB << endl;
	}
	fout.close ();
	fin.close ();
}
