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

int solveIt(vector<vector<int> > &h, vector<vector<int> > &d, int t = 1) {
	int s = 0;
	while (t-- && !h.empty()) {
		bool played = false;
		for (int i = 0; i < h.size(); i++) if (h[i][2]) {
			played = true;
			for (int j = 0; j < h[i][0] && !d.empty(); j++) {
				h.push_back(d[0]);
				d.erase(d.begin());
			}
			s += h[i][1];
			t += h[i][2];
			h.erase(h.begin()+i);
			break;
		}
		if (played) continue;

		int cc = 0, hc = -1, hci = -1, hnc = -1, hnci = -1;
		for (int i = 0; i < h.size(); i++)
			if (h[i][0]) {
				cc++;
				if (h[i][1] > hc) hc = h[i][1], hci = i;
			} else {
				if (h[i][1] > hnc) hnc = h[i][1], hnci = i;
			}

		if (!cc) {
			// no c cards, so play highest scoring
			s += hnc;
			h.erase(h.begin()+hnci);
			continue;
		}

		if (hc >= hnc) {
			// highest scoring c card better than non-c, so play it
			s += hc;
			h.erase(h.begin()+hci);
			if (!d.empty()) {
				h.push_back(d[0]);
				d.erase(d.begin());
			}
			continue;
		}

		if ((t > h.size() && !d.empty()) || (t && !d.empty() && d[0][2] > 1)) {
			// I have more turns than I need, so acquire another card,
			// or the next card will give me an extra turn to make up for drawing it
			int bs = -1, bi = 0;
			for (int i = 0; i < h.size(); i++) if (h[i][0] && h[i][1] > bs) {
				bs = h[i][1];
				bi = i;
			}
			if (bs >= 0) {
				s += bs;
				h.push_back(d[0]);
				d.erase(d.begin());
				h.erase(h.begin()+bi);
				continue;
			}
		}

		if (d.empty()) {
			// empty deck, so c cards no better than non-c
			int bs = -1, bi = 0;
			for (int i = 0; i < h.size(); i++) if (h[i][1] > bs) {
				bs = h[i][1];
				bi = i;
			}
			if (bs >= 0) {
				s += bs;
				h.erase(h.begin()+bi);
				continue;
			}
		}

		if (!t) {
			// play the highest scoring card
			int bs = -1, bi = 0;
			for (int i = 0; i < h.size(); i++) if (h[i][1] > bs) {
				bs = h[i][1];
				bi = i;
			}
			if (bs >= 0) {
				s += bs;
				h.erase(h.begin()+bi);
				continue;
			}
		}

		{ // DFS - yuck
			vector<vector<int> > ch = h, cd = d, nh = h, nd = d;
			ch.erase(ch.begin()+hci);
			ch.push_back(cd[0]);
			cd.erase(cd.begin());
			int psch = s + hc + solveIt(ch, cd, t);

			nh.erase(nh.begin()+hnci);
			int psnh = s + hnc + solveIt(nh, nd, t);
			return psch > psnh ? psch : psnh;
		}

		printf("Oops - didn't handle this condition!\n");
		printf("%d turns\n", t);
		printf("Hand\n");
		for (int i = 0; i < h.size(); i++) printf(" %d %2d %2d\n", h[i][0], h[i][1], h[i][2]);
		printf("Deck\n");
		for (int i = 0; i < d.size(); i++) printf(" %d %2d %2d\n", d[i][0], d[i][1], d[i][2]);
		break;
	}
	return s;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int N, M;
		vector<vector<int> > h, d;
		scanf("%d ", &N);
		for (int i = 0; i < N; i++) {
			vector<int> c(3);
			scanf("%d %d %d", &c[0], &c[1], &c[2]);
			h.push_back(c);
		}
		scanf("%d ", &M);
		for (int i = 0; i < M; i++) {
			vector<int> c(3);
			scanf("%d %d %d", &c[0], &c[1], &c[2]);
			d.push_back(c);
		}

		long long res = solveIt(h, d);
		printf("Case #%d: %lld\n", cn, res);
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

