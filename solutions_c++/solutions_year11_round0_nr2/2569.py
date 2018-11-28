// CodeJam2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define FOR(i, x) for(int i = 0; i<(x); i++)


void jeden() {
	int c; cin>> c;
	vector<string> C(c);
	for(int i = 0; i<c; i++) cin >> C[i];
	int d; cin >> d;
	vector<string> D(d);
	for(int i = 0; i<d; i++) cin >> D[i];

	int n; cin>> n;
	string input;
	cin >> input;


	string s = "";

	FOR(i, n) {
		s.push_back(input[i]);

		bool done = false;
		while(!done) {
			if(s.length() >=2 ) {
				FOR(j, c) {
					if((s[s.length()-1] == C[j][0] && s[s.length()-2] == C[j][1]) || (s[s.length()-1] == C[j][1] && s[s.length()-2] == C[j][0])) {
						s.pop_back();
						s.pop_back();
						s.push_back(C[j][2]);
						goto once_again;
					}
				}
				FOR(j, d) {
					char k = s[s.length()-1];
					char l;
					if(D[j][0] == k) {
						l = D[j][1];
					} else if(D[j][1] == k) {
						l = D[j][0];
					} else continue;


					FOR(a, s.length() - 1) {
						if(s[a] == l) {
							s.clear();
							goto once_again;
						}
					}

				}

			}
			done = true;
		once_again:;
		}
	}
	cout << '[';
	FOR(i, s.length()) {
		if(i != 0) cout << ", ";
		cout << s[i];
	}
	cout << ']' << endl;

}

int _tmain(int argc, _TCHAR* argv[])
{
	int d; cin >> d;
	for(int i = 1; i<=d; i++) {
		printf("Case #%d: ", i);

		jeden();
	}
}

