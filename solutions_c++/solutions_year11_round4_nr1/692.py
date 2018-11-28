#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;
string readLine();
int readIntLine();
vector<int> readVI(int n);
vector<string> readVS(int n);
vector<int> itokens(string s, string sep);
vector<string> stokens(string s, string sep);


double solveIt(int X, int S, int R, int t, int N) {
	vector<vector<int> > ww(N, vector<int>(3));
	for (int i = 0; i < N; i++) scanf("%d %d %d", &ww[i][0], &ww[i][1], &ww[i][2]);
	sort(ww.begin(), ww.end());

	int nonww = ww[0][0];
	for (int i = 0; i < ww.size(); i++) if (ww[i][1] > X) {
		ww.erase(ww.begin()+i--);
	} else {
		if (i+1 < ww.size()) nonww += ww[i+1][0]-ww[i][1];
	}
	nonww += X-ww.back()[1];
	for (int i = 0; i < ww.size(); i++) swap(ww[i][0], ww[i][2]);
	sort(ww.begin(), ww.end());

	double tottm = 0;
	double nwrt = nonww/(double)R;
	if (nwrt < t) {
		double trm = t-nwrt;
		tottm = nwrt;
		for (int i = 0; i < ww.size(); i++) {
			if (trm > 0.0) {
				double rt = (ww[i][1]-ww[i][2])/(double)(R+ww[i][0]);
				if (rt < trm) {
					tottm += rt;
					trm -= rt;
				} else {
					tottm += trm;
					double drm = (ww[i][1]-ww[i][2]) - (R+ww[i][0])*trm;
					trm = 0;
					tottm += drm/(S+ww[i][0]);
				}
			} else
				tottm += (ww[i][1]-ww[i][2])/(double)(S+ww[i][0]);
		}
	} else {
		tottm = t;
		double drm = nonww - R*t;
		tottm += drm/S;
		for (int i = 0; i < ww.size(); i++) {
			tottm += (ww[i][1]-ww[i][2])/(double)(S+ww[i][0]);
		}
	}

	return tottm;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int X, S, R, t, N;
		scanf("%d %d %d %d %d ", &X, &S, &R, &t, &N);

		double res = solveIt(X, S, R, t, N);
		printf("Case #%d: %.9lf\n", cn, res);
	}
	return 0;
}








string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}
int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}
vector<int> readVI(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}
vector<string> readVS(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<string> v(n);
	for (int i = 0; i < n; i++) v[i] = readLine();
	return v;
}
vector<string> stokens(string s, string sep = " \n\r\t") {
	vector<string> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(s.substr(start, end-start));
	}
	return res;
}
vector<int> itokens(string s, string sep = " \n\r\t") {
	vector<int> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(atoi(s.substr(start, end-start).c_str()));
	}
	return res;
}

