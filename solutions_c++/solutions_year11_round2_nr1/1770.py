#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;

FILE * fin;
FILE * fout;

char s[101][101];
int win[101], total[101];
double owp[101], oowp[101];

void run(int casenr) {
	memset(win, 0, sizeof(win));
	memset(total, 0, sizeof(total));
	memset(owp, 0, sizeof(owp));
	memset(oowp, 0, sizeof(oowp));
	int n;
	fscanf(fin, "%d",&n);
	FOR(i, 0, n) {
		fscanf(fin, "%s", s[i]);
		int t = 0, w = 0;
		FOR(j, 0, n) {
			if ('1' == s[i][j]) {
				t++;
				w++;
			} else if ('0' == s[i][j]) {
				t++;
			}
		}
		win[i] = w;
		total[i] = t;
	}
	FOR(i, 0, n) {
		double total_wp = 0;
		FOR (j, 0, n) {
			if ('1' == s[i][j]) {
				total_wp += 1.0 * win[j] / (total[j] - 1);
			} else if ('0' == s[i][j]) {
				total_wp += 1.0 * (win[j] - 1) / (total[j] - 1);
			}
		}
		owp[i] = total_wp / total[i];
	}
	FOR(i, 0, n) {
		FOR(j, 0, n) {
			if ('1' == s[i][j] || '0' == s[i][j]) {
				oowp[i] += owp[j];
			}
		}
		oowp[i] /= total[i];
	}
	fprintf(fout, "Case #%d:\n",casenr);
	FOR(i, 0, n)
		fprintf(fout, "%.12g\n", 0.25 * win[i] / total[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
}

int main() {
	fin = fopen("H:\\temp\\A-large.in", "r");
	fout = fopen("H:\\temp\\A.out", "w");
	int n; fscanf(fin, "%d",&n); FORE(i,1,n) run(i);
	fclose(fin);
	fclose(fout);
	return 0;
}