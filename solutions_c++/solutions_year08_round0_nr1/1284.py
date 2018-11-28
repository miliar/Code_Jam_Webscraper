#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<string> svec;

static int solve(const vector<string>& s, const vector<string>& q)
{
	int rv = 0;
	svec::const_iterator send = s.end();
	svec::const_iterator qend = q.end();
	svec::const_iterator qi = q.begin();
	while (qi != qend) {
		svec::const_iterator nextqi = qi;
		for (svec::const_iterator si = s.begin(); si != send; ++si) {
			svec::const_iterator qii = find(qi, qend, *si);
			if (qii > nextqi) nextqi = qii;
		}
		qi = nextqi;
		if (qi != qend) ++rv;
	}
	return rv;
}

int main(int argc, char* argv)
{
	int N;
	string buf;
	cin >> N;
	for (int n = 0; n < N; ++n) {
		int S, Q;
		vector<string> se, queries;
		cin >> S;
		getline(cin, buf);
		for (int s = 0; s < S; ++s) {
			getline(cin, buf);
			se.push_back(buf);
		}
		cin >> Q;
		getline(cin, buf);
		for (int q = 0; q < Q; ++q) {
			getline(cin, buf);
			queries.push_back(buf);
		}
		cout << "Case #" << (n + 1) << ": " << solve(se, queries) << endl;
	}
	return 0;
}