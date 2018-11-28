// RPI.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
using namespace std;

int readi() { int a; scanf( "%d", &a ); return a; }
double readf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string readstr() { scanf( "%s", sbuf ); return sbuf; }
long long readll() { long long a; scanf( "%lld", &a ); return a; }
#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )

#define MAX  100
int _tmain(int argc, _TCHAR* argv[])
{
	int T, N;

	int i, j, k, r, s, m;
	

	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	T = readi();
	for(r = 1; r <= T; ++r) {
		printf("Case #%d:\n", r);
		N = readi();
		
		double WP[MAX][MAX+1];
		double OWP[MAX];
		double OOWP[MAX];
		vector<int> OP[MAX];
		vector<int>::iterator it;
		
		for(i = 0; i < MAX; i++)  {
			for(j = 0; j < MAX +1; j++) WP[i][j] = 0;
			OWP[i] = 0;
			OOWP[i] = 0;
		}

		for(m = 0; m < N; ++m) { //the whole player
			string strList = readstr();
			for(i = 0; i < strList.size(); ++i) {
				if (strList[i] == '.') continue;
				else if(strList[i] == '1') {
					WP[m][MAX] += 1;
					for(j = 0; j < MAX; ++j) {
						if(i != j) WP[m][j] += 1;
					}
				}
				OP[m].push_back(i); // Add opponents;
			}

			//calculate
            s = OP[m].size(); 
			if( s > 0) {
				WP[m][MAX] = WP[m][MAX] / s;
				if (s > 1) {
					for(j = 0; j < MAX; ++j) WP[m][j] = WP[m][j] / (s - 1);
				}
			}
		}

		for(m = 0; m < N; m++) {
			for(it = OP[m].begin(); it != OP[m].end(); ++it){
				j = *it;
				OWP[m] += WP[j][m];
			}
			
			if(OP[m].size() > 0) OWP[m] = OWP[m] / OP[m].size();
			else OWP[m] = 0;
		}

		for(m = 0; m < N; m++) {
			for(it = OP[m].begin(); it != OP[m].end(); ++it){
				j = *it;
				OOWP[m] += OWP[j];
			}
			if(OP[m].size() > 0) OOWP[m] = OOWP[m] / OP[m].size();
			else OOWP[m] = 0;
		}

		double score;
		for(m = 0; m < N; m++) {
			score = 0.25 * WP[m][MAX] + 0.50 * OWP[m] + 0.25 * OOWP[m];
			printf("%.12f\n", score);
		}
	}


	return 0;
}

