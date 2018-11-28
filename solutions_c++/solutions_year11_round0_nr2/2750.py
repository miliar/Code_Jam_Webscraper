#include <iostream>
#include <list>
using namespace std;

int oppose[30],pairs[30],combine[30];

typedef list <int> el_list_t;

bool make_combine (el_list_t &l) {
	bool t = false;
	for (el_list_t::iterator i = l.begin(); i != l.end(); i ++) {
		el_list_t::iterator j = i;
		j ++;
		if (j != l.end()) 
			if (pairs[*j] == *i) {
				l.erase(j);
				*i = combine[*i];
				t = true;
			}
	}
	return t;
}

void make_oppose (el_list_t &l) {
	int was [30];
	for (int i = 0; i < 30; i ++) was[i] = 0;
	for (el_list_t::iterator i = l.begin(); i != l.end(); i ++) {
		was[*i] = 1;
		if (was[oppose[*i]]) {
			l.clear();
			return;
		}
	}
}

char s[200];

int main () {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n; cin >> n;
	for (int k = 0; k < n; k ++) {
		for (int i = 0; i < 30; i ++) pairs[i] = combine[i] = oppose[i] = 0;
		int m; cin >> m;
		for (int i = 0; i < m; i ++) {
			cin >> s;
			pairs[s[0] - 'A' + 1] = s[1] - 'A' + 1;
			pairs[s[1] - 'A' + 1] = s[0] - 'A' + 1;
			combine[s[0] - 'A' + 1] = combine[s[1] - 'A' + 1] = s[2] - 'A' + 1;
		}
		cin >> m;
		for (int i = 0; i < m; i ++) {
			cin >> s;
			oppose[s[0] - 'A' + 1] = s[1] - 'A' + 1;
			oppose[s[1] - 'A' + 1] = s[0] - 'A' + 1;
		}
		cin >> m;
		cin >> s;
		el_list_t l;
		for (int i = 0; i < m; i ++) {
			l.push_back(s[i] - 'A' + 1);
			while (make_combine(l));
			make_oppose(l);
		}
		cout << "Case #" << k + 1 << ": " << "[";
		if (l.empty()) cout << "]\n"; else {
			for (el_list_t::iterator i = l.begin(); i != --l.end(); i ++) 
				cout << (char)(*i + 'A' - 1) << ", ";
			cout << (char)(*(--l.end()) + 'A' - 1) << "]\n";
		}
	}
	return 0;
}