#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
using namespace std;

int N;

bool ok(string &m)
{
	for (int i=0; i<N; ++i) {
		if (m[i]>i) return false;
	}
	return true;
}

int calc(string &m)
{
	queue<string> q;
	map<string, int> dist;
	set<string> visited;

	q.push(m);
	dist[m] = 0;
	visited.insert(m);

	int i;
	while (1) {
		string cur = q.front(); q.pop();
		int d = dist[cur];
		if (ok(cur)) return d;

		for (i=0; i<N-1; ++i) {
			string ss = cur;
			char ch = ss[i];
			ss[i] = ss[i+1];
			ss[i+1] = ch;
			if (visited.find(ss) == visited.end()) {
				visited.insert(ss);
				q.push(ss);
				dist[ss] = d+1;
			}
		}
	}
	return -1;
}

int main(void)
{
	int T;
	cin >> T;
	for (int ca=1; ca<=T; ++ca) {
		cin >> N;
		int i, j;
		string s;
		string m = "";
		for (i=0; i<N; ++i) {
			cin >> s;
			for (j=N-1; j>=0; j--) {
				if (s[j] == '1') break;
			}
			if (j==-1) j==0;
			m += j;
		}

		//cout << "N: " << N << endl;
		cout << "Case #" << ca << ": " << calc(m) << endl;
	}
	return 0;
}
