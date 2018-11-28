#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

int T, N, M;
string D [10000];
string L;
int b, c;
string s, u;

int main () {
	
	ifstream fin ("input");
	ofstream fout ("output");
	
	fin >> T;
	
	for (int t = 1; t <= T; t ++) {
		fout << "Case #" << t << ":";
		cout << "Case #" << t << ":";
		
		fin >> N >> M;
		
		for (int i = 0; i < N; i ++) fin >> D [i];
		for (int i = 0; i < M; i ++) {
			fin >> L;
			b = -1;
			s = "";
			for (int j = 0; j < N; j ++) {
				//cout << endl;
				u = "";
				for (int k = 0; k < D [j].length (); k ++)
					u += "_";
				c = 0;
				bool g [256];
				fill (g, g + 256, false);
				while (u != D [j]) {
					//cout << D [j] << endl;
					//cout << u << endl;
					bool lose = true;
					for (int k = 0; k < L.length (); k ++) {	//go through letters
						bool ok = false;
						for (int l = 0; l < N; l ++) {		//go through dictionary
							bool ok2 = true;
							if (D [l].length () != u.length ()) ok2 = false;
							else {
								bool ok3 = false;
								for (int m = 0; m < u.length (); m ++) {
									if (D [l] [m] == L [k] && u [m] != '_') ok2 = false;
									if (u [m] != '_' && D [l] [m] != u [m]) ok2 = false;
									if (u [m] == '_' && g [D [l] [m]]) ok2 = false;
									if (D [l] [m] == L [k]) ok3 = true;
								}
								if (!ok3) ok2 = false;
							}
							if (ok2) ok = true;
						}
						if (g [L [k]]) ok = false;
						if (ok) {
							//cout << L [k] << endl;
							for (int l = 0; l < u.length (); l ++) {
								if (D [j] [l] == L [k]) {
									u [l] = L [k];
									lose = false;
								}
							}
							g [L [k]] = true;
							break;
						}
					}
					if (lose)
						c ++;
				}
				if (c > b) {
					b = c;
					s = D [j];
				}
			}
			fout << " " << s;
			cout << " " << s; //<< " " << c;
		}
		
		fout << endl;
		cout << endl;
		//if (ok) fout << "Possible" << endl;
		//else fout << "Broken" << endl;
	}
}