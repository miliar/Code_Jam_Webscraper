//	GCJ 2009 Round 1B (A)

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <bitset>
#include <complex>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef vector<int> vint;
typedef pair<int,int> pint;
#define mp make_pair

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
int in_c() { int c; while ((c = getchar()) <= ' ') { if (!~c) throw ~0; } return c; }
int in() {
	int x = 0, c;
	while ((uint)((c = getchar()) - '0') >= 10) { if (c == '-') return -in(); if (!~c) throw ~0; }
	do { x = (x << 3) + (x << 1) + (c - '0'); } while ((uint)((c = getchar()) - '0') < 10);
	return x;
}

char buf[100010];

int N;
double W[10010];
string S[10010], dump;
int L[10010], R[10010];

int readit(istringstream &iss, int n) {
	iss >> W[n] >> S[n];
//cout<<W[n]<<" "<<S[n]<<endl;
	if (S[n] != "~") {
		L[n] = readit(iss, N++);
		R[n] = readit(iss, N++);
		iss >> dump;
	}
	return n;
}

int main() {
	int n;
	string tree, tree2;
	string fe;
	
	for (int TC = atoi(gets(buf)), tc = 0; TC--; ) {
		printf("Case #%d:\n", ++tc);
		
		tree = tree2 = "";
		for (int nu = atoi(gets(buf)); nu--; ) {
			tree += gets(buf);
		}
		for (string::iterator it = tree.begin(), en = tree.end(); it != en; ++it) {
			if (*it == ')') {
				tree2 += " ~ ";
			} else if (*it == '(') {
				tree2 += ' ';
			} else {
				tree2 += *it;
			}
		}
		istringstream iss(tree2);
		
		memset(L, ~0, sizeof(L));
		memset(R, ~0, sizeof(R));
		N = 0;
		readit(iss, N++);
		
		for (int qry = atoi(gets(buf)); qry--; ) {
			gets(buf);
			istringstream fss(buf);
			set<string> fes;
			for (; fss >> fe; ) {
				fes.insert(fe);
			}
			double ans = 1.0;
			for (n = 0; ; ) {
				ans *= W[n];
				if (!~L[n]) break;
				if (fes.count(S[n])) {
					n = L[n];
				} else {
					n = R[n];
				}
			}
			printf("%.8f\n", ans);
		}
		
	}
	
	
	return 0;
}

