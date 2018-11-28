#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <time.h>
#include <algorithm> 
#include <iostream>  
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <cassert>
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
#define FILL(a,b) memset(a, (b), sizeof(a));
typedef long long ll; 
const double EPS = 1e-7;

void openfiles() {
	#ifndef ONLINE_JUDGE
		freopen("A-large.in","rt",stdin);
		freopen("A-large.out","wt",stdout);   
	#endif
}

void solve() {
	vector<string> words;
	int L, D, N;
	scanf("%d %d %d ", &L, &D, &N);
	
	for (int i = 0; i < D; i++)
	{
		char line[100];
		gets(line);
		words.push_back(line);
	}

	
	for (int i = 0; i < N; i++) 
	{
		char line[10000];
		gets(line);

		set<int> s;
		for (int ii = 0; ii < D; ii++)
			s.insert(ii);

		int kk = 0;
		for (int ii = 0; ii < L; ii++)
		{
			set<int> next;
			if (line[kk] == '(') {
				kk++;
				while (line[kk] != ')') {
					for (set<int>::iterator jj = s.begin(); jj != s.end(); jj++) {
						if (words[*jj][ii] == line[kk]) {
							next.insert(*jj);
						}
					}
					kk++;
				}
				kk++;
			}
			else {
					for (set<int>::iterator jj = s.begin(); jj != s.end(); jj++) {
						if (words[*jj][ii] == line[kk]) {
							next.insert(*jj);
						}
					}
				kk++;
			}

			s = next;
		}

		static int ntest = 0;
		printf("Case #%d: %d\n", ++ntest, (int)s.size() );
	}
}

int main() {
	openfiles();
	
	solve();

	return 0;
}