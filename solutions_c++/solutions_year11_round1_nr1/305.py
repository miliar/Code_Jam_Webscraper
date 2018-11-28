#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

int T, PG, PD, de, pd;
long long N;
bool ok;

int main () {
	
	ifstream fin ("input");
	ofstream fout ("output");
	
	fin >> T;
	
	for (int t = 1; t <= T; t ++) {
		fin >> N >> PD >> PG;
		pd = PD;
		de = 100;
		if (pd % 2 == 0) {
			pd /= 2;
			de /= 2;
		}
		if (pd % 2 == 0) {
			pd /= 2;
			de /= 2;
		}
		if (pd % 5 == 0) {
			pd /= 5;
			de /= 5;
		}
		if (pd % 5 == 0) {
			pd /= 5;
			de /= 5;
		}
		ok = true;
		if (de > N) {
			ok = false; 
		}
		if (PD != 100 && PG == 100) ok = false;
		if (PD != 0 && PG == 0) ok = false;
		fout << "Case #" << t << ": ";
		if (ok) fout << "Possible" << endl;
		else fout << "Broken" << endl;
	}
}