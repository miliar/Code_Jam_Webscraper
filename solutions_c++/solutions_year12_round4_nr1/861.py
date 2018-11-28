//Problem A. Password Problem
#include <algorithm>
#include <fstream>
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
#include <cstring>
#include <climits>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define foreach(itr, cont) for (typeof(cont.begin()) itr = cont.begin(); itr != cont.end(); itr++)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

//int d[10001], len[10001];
int main() {
	int T;

	ifstream in("A-large.in");
	ofstream out("A-large.out");
	//ifstream in("C-large.in");
	//ofstream out("C-large.out");
	//FILE *in = fopen("A-large.in", "r");	
	//FILE *out = fopen("A-large.out", "w");

	in >> T;
	//fscanf(in, "%d", &T);
	for (int cs = 1; cs <= T; cs ++) {
		out << "Case #" << cs << ": ";

		int N;
		in >> N;
		vector<int> d(N), l(N), len(N, 0);
		for (int i = 0; i < N; i ++) {
			in >> d[i] >> l[i];
		}
		int dis = 0;
		in >> dis;

		int cur = 0, pos = 0;
		bool ans = false;
		cout << "case " << cs << endl;
		len[0] = d[0];
		int farest = 0;
		for (int i = 0; i < N; i ++) {
			int ll = min(len[i], l[i]);
			for (int j = i + 1; j < N && d[j] <= d[i] + ll; j ++) {
				len[j] = max(len[j], d[j] - d[i]);
			}
			farest = max(farest, d[i] + ll);
		}
		out << (farest >= dis ? "YES" : "NO") << endl;
	}
	return 0;
}
