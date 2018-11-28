 
#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <list>
#include <string>

using namespace std;

int T, C, D, N;
char com [256] [256];
bool opp [256] [256];
int cnt [256];
string str;
char b1, b2;
list <char> lst;
char chr;

int main () {
	
	ifstream fin ("input");
	ofstream fout ("output");
	
	fin >> T;
	for (int t = 1; t <= T; t ++) {
		
		memset (com, 0, sizeof (com));
		memset (opp, 0, sizeof (opp));
		memset (cnt, 0, sizeof (cnt));
		lst.clear ();
		
		fin >> C;
		for (int c = 0; c < C; c ++) {
			fin >> b1 >> b2;
			fin >> com [b1] [b2];
			com [b2] [b1] = com [b1] [b2];
		}
		
		fin >> D;
		for (int d = 0; d < D; d ++) {
			fin >> b1 >> b2;
			opp [b2] [b1] = opp [b1] [b2] = true;
		}
		
		fin >> N >> str;
		for (int n = 0; n < N; n ++) {
			if (lst.empty ()) {
				lst.push_back (str [n]);
				cnt [str [n]] ++;
			}
			else if (com [str [n]] [lst.back ()]) {
				chr = lst.back ();
				cnt [chr] --;
				lst.pop_back ();
				cnt [com [str [n]] [chr]] ++;
				lst.push_back (com [str [n]] [chr]);
			}
			else {
				cnt [str [n]] ++;
				lst.push_back (str [n]);
				for (int c = 0; c < 256; c ++) {
					if (cnt [c] && opp [c] [str [n]]) {
						lst.clear ();
						memset (cnt, 0, sizeof (cnt));
					}
				}
			}
		}
		
		cout << "Case #" << t << ": [";
		fout << "Case #" << t << ": [";
		if (lst.size ()) {
			cout << lst.front ();
			fout << lst.front ();
			lst.pop_front ();
		}
		while (lst.size ()) {
			cout << ", " << lst.front ();
			fout << ", " << lst.front ();
			lst.pop_front ();
		}
		cout << "]" << endl;
		fout << "]" << endl;
	}
}