// SquareTiles.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <string>
using namespace std;

int readi() { int a; scanf( "%d", &a ); return a; }
double readf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string readstr() { scanf( "%s", sbuf ); return sbuf; }
long long readll() { long long a; scanf( "%lld", &a ); return a; }
#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )

int _tmain(int argc, _TCHAR* argv[])
{
	int T, R, C;
	int i, j, k, r, s, t;
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);	

	T = readi();
	string strCur, strNext;
	bool bad;
	vector<string> output;
	vector<string>::iterator it;
	for(r  = 1; r <= T; r++) {

		R = readi(); C=readi(); s = 0; bad = false; output.clear();

		printf("Case #%d:\n", r);

		strCur = ""; strNext = "";

		for(j = 0; j < R; ++j) {

			if(R == 1) {
				strCur = readstr();
				for (i = 0; i < strCur.size(); i++) {
					if(strCur[i] == '#')  {bad = true; goto e;}					
				}

				printf("%s\n", strCur.c_str());
				continue;
			}

			if(j == 0) {
				strCur = readstr(); ++s;
				strNext = readstr(); ++s;
			} else if (j == R - 1){
				strCur = strNext;
			} else {
				strCur = strNext;
				strNext = readstr(); ++s;
			}

			if(j != R-1) {
				for(i = 0; i < (strCur.size() - 1); ++i) {
					if((strCur[i] == '#') && (strCur[i+1] == '#') && (strNext[i] == '#') && (strNext[i+1] == '#')) {
						strCur[i] = '/'; 
						strCur[i+1] = '\\'; 
						strNext[i] = '\\'; 
						strNext[i+1] = '/';
					}
				}
			}

			for(i = 0; i < strCur.size(); ++i) {
				if(strCur[i] == '#') {bad = true; }
			}
			
			output.push_back(strCur);

			if(j == R - 1){
				if(bad) {printf("Impossible\n");}
				else {
					for(it = output.begin(); it!= output.end(); ++it) {
						printf("%s\n", (*it).c_str());
					}
				}
			}
			continue;
	e:
			printf("Impossible\n");
			break;
		}
	}


	return 0;
}

