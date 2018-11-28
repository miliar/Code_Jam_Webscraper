#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <ctype.h>
#include <assert.h>
using namespace std;

typedef vector<int> VI;

int dt1[128], at1[128];
int dt2[128], at2[128];
VI adj[256];

int read_time() {
	string s;
	cin >> s;
	assert(s.size() == 5 && s[2] == ':');
	assert(isdigit(s[0]) && isdigit(s[1]));
	int h = (int)(s[0] - '0') * 10 + s[1] - '0';
	assert(h < 24);
	int m = (int)(s[3] - '0') * 10 + s[4] - '0';
	assert(m < 60);
	return h * 60 + m;
}


void read_schedule(int n, int *dt, int *at) {
	for (int i=0; i<n; ++i) {
		dt[i] = read_time();
		at[i] = read_time();
	}
}

char visit[256];
int pred[256], match[256];

int augment(int cur) {
	if (visit[cur])
		return 0;
	visit[cur] = 1;
	for (VI::iterator it=adj[cur].begin(); it!=adj[cur].end(); ++it)
		if (pred[*it] < 0 || augment(pred[*it])) {
			match[cur] = *it;
			pred[*it] = cur;
			return 1;
		}
	return 0;
}

int main() {
	int tc;
	cin >> tc;
	for (int x=1; x<=tc; ++x) {
		int T, na, nb;
		cin >> T >> na >> nb;
		assert(na >= 0 && na <= 100);
		assert(nb >= 0 && nb <= 100);
		read_schedule(na, dt1, at1);
		read_schedule(nb, dt2, at2);
		int N = na + nb;
		for (int i=0; i<na; ++i) {
			adj[i].clear();
			for (int j=0; j<nb; ++j) {
				if (at1[i] + T <= dt2[j])
					adj[i].push_back(na + j);
			}
		}
		for (int i=0; i<nb; ++i) {
			adj[i+na].clear();
			for (int j=0; j<na; ++j) {
				if (at2[i] + T <= dt1[j])
					adj[i+na].push_back(j);
			}
		}
		for (int i=0; i<N; ++i)
			pred[i] = -1;
		for (int i=0; i<N; ++i) {
			memset(visit, 0, N);
			augment(i);
		}
		int cnta = 0, cntb = 0;
		for (int i=0; i<na; ++i)
			if (pred[i] < 0)
				++cnta;
		for (int i=na; i<N; ++i)
			if (pred[i] < 0)
				++cntb;
		cout << "Case #" << x << ": " << cnta << " " << cntb << endl;
	}
	return 0;
}
