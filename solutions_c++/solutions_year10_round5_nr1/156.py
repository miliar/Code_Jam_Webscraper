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


#define MAXPRIME 1000003
int primes[MAXPRIME+1], pct;
int genPrimes() {
	memset(primes, -1, sizeof(primes));
	primes[0] = 2;
	int p = 1;
	for (int i = 3; i <= MAXPRIME; i += 2) if (primes[i]) {
		primes[p++] = i;
		if (i < 1000) for (int j = i*i; j <= MAXPRIME; j += 2*i) primes[j] = 0;
	}
	return p;
}

int tryseq(long long a, int p, vector<int> &vk) {
	if (vk.size() == 1) {
		return -1;
	} else {
		int b = (vk[1] - (a*vk[0])%p + p)%p;
		for (int i = 2; i < vk.size(); i++) {
			int n = (a*vk[i-1] + b)%p;
			if (n != vk[i]) return -1;
		}
		return (a*vk.back() + b)%p;
	}
}

int solveIt(int D, int K, vector<int> &vk) {
	if (K == 1) return -1;
	int res = -1, mpi = 0, mxk = 0, td = 10;
	for (int i = 1; i < D; i++) td *= 10;
	for (int i = 0; i < K; i++) if (vk[i] > mxk) mxk = vk[i];
	while (primes[mpi] <= mxk) mpi++;

	for (int pi = mpi; primes[pi] <= td; pi++) {
		int p = primes[pi];
		for (int a = 0; a < p; a++) {
			int r = tryseq(a, p, vk);
//if (r >= 0) 			printf("p %d, a %d -> r %d\n", p, a, r);
			if (r >= 0) {
				if (res < 0) res = r;
				else if (r != res) return -1;
			}
		}
	}

	return res;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	pct = genPrimes();
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int K, D;
		scanf("%d %d ", &D, &K);
		vector<int> vk = readVI(K);

		long long res = solveIt(D, K, vk);
		if (res < 0) printf("Case #%d: I don't know.\n", cn);
		else printf("Case #%d: %lld\n", cn, res);
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

