#include <iostream>
#include <vector>

using namespace std;

struct node {
	node* child['z'-'a'+1];
	char c;
};

node* roots['z'-'a'+1];

void addword(string w, node** roots) {
	if (w.length() == 0) return;
	int i = w[0] - 'a';
	if (roots[i] == NULL) {
		roots[i] = new node;
		roots[i]->c = i;
	}
	
	addword(w.substr(1), roots[i]->child);
}

int solve(string t, node** roots, int l, int cl) {
	if (t.length()==0) {
		if (l == cl) return 1;
		return 0;	
	}
	int cases = 0;
	if (t[0] == '(') {
		int  i = 1;
		string h;
		while (t[i] != ')') {
			h += t[i];
			i++;
		}	
		for (int j = 0; j < h.length(); j++) {
			if (roots[h[j] - 'a'] != NULL)
				cases += solve(t.substr(h.length() + 2), roots[h[j] - 'a'] -> child, l, cl + 1);
		}
	} else {
		if (roots[t[0] - 'a'] != NULL)
			cases += solve(t.substr(1), roots[t[0] - 'a'] -> child, l, cl + 1);
	}

	return cases;
}

int main() {
	int l, d, n;

	cin >> l >> d >> n;

	for (int i = 0; i < d; i++){
		string s;
		cin >> s;
		addword(s, roots);
	}


	for (int i = 0; i < n ; i++) {
		string t; cin >> t;
		int c = solve(t, roots, l, 0);
		cout << "Case #" << (i+1) << ": " << c << endl;
	}
}
