#include <iostream>
#include <map>
#include <list>

#include <string.h>

using namespace std;

struct node {
	map<char, node*> child;
};

int l, d, n, len, pos, c;
node *trie;
char beseda[100000];
list<char> crke[15];

void insert() {
	node *p = trie, *t;
	for (int i = 0; i < l; i++) {
		if (p->child.find(beseda[i]) != p->child.end()) {
			p = p->child[beseda[i]];
		} else {
			t = new node;
			p->child.insert(make_pair(beseda[i], t));
			p = t;
		}
	}
}

void solve(int pos, node *p) {
	if (p == NULL)
		return;
	if (pos == l) {
		c++;
		return;
	}
	for (list<char>::iterator i = crke[pos].begin(); i != crke[pos].end(); i++) {
		solve(pos + 1, p->child[*i]);
	}
}

int main() {
	cin >> l >> d >> n;
	trie = new node;
	for (int i = 0; i < d; i++) {
		scanf("%s", beseda);
		insert();
	}
	for (int i = 0; i < n; i++) {
		scanf("%s", beseda);
		len = strlen(beseda);
		pos = 0;
		for (int j = 0; j < len; j++, pos++) {
			if (beseda[j] == '(') {
				for (j++; beseda[j] != ')'; j++)
					crke[pos].push_back(beseda[j]);
			} else {
				crke[pos].push_back(beseda[j]);
			}
		}
		c = 0;
		solve(0, trie);
		cout << "Case #" << i + 1 << ": " << c << endl;
		for (int i = 0; i < l; i++)
			crke[i].clear();
	}
}

