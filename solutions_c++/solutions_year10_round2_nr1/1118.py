#include <iostream>
#include <vector>
#include <iterator>
#include <set>

using namespace std;

set<string>	sset;
int		m;

void
sinsert(string &s) {
	int	k = 0;

	sset.insert(s);
	while ((k = s.find('/', k+1)) != string::npos) {
		sset.insert(s.substr(0, k));
	}
}

int
get(vector<string> &v) {
	int	ans = 0, k, i;
	string	s, t, u;
	vector<string>::iterator it;

	for (it = v.begin();  it != v.end(); it++) {
		k = 0;
		u = *it;
		while ((k = u.find('/', k+1)) != string::npos) {
			t = u.substr(0, k);
			if (sset.find(t) == sset.end()) {
				sset.insert(t);
				ans++;
			}
		}
		if (sset.find(u) == sset.end()) {
			sset.insert(u);
			ans++;
		}
	}
	
	return ans;
}

int
main(void) {
	int		t, n, i, j;
	string		s;
	unsigned long long	r, k;
	vector<string>	v;

	cin >> t;

	for (i=0;i<t;i++) {
		sset.clear();
		v.clear();
		sset.insert(string("/"));
		cin >> n >> m;
		for (j=0;j<n;j++) {
			cin >> s;
			sinsert(s);
		}
		for (k=0;k<m;k++) {
			cin >> s;
			v.push_back(s);
		}
		cout << "Case #" << (i+1) << ": " << get(v) << endl;
	}

	return 0;	
}
