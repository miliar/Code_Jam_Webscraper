
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct node {
	node* children[26];

	node() {
		for (int i = 0; i < 26; ++i)
			children[i] = NULL;
	}
};

node* root = new node();
int ccount;

void process (string tt, node* currLoc) {

//	cout << "processing " << tt << "; count = " << ccount << endl;

	if (tt.size() > 0) {
		if (tt[0] != '(') {
			if (currLoc->children[tt[0] - 'a'] == NULL) {
				return;
			} else {
				process (tt.substr(1, tt.size()), currLoc->children[tt[0]-'a']);
			}
		}
		else {
//			cout << "branch" << endl;
			int ind = 2; 
			while (tt[ind] != ')')
				++ind;
			for (int i = 1; i < ind; ++i) {
//				cout << "branching " << tt[i] << endl;
				if (currLoc->children[tt[i] - 'a'] == NULL) {
					continue;
				} else {
					process (tt.substr(ind+1, tt.size()), currLoc->children[tt[i]-'a']);
				}
			}
		}
	}
	else {
		++ccount;
	}
}


int main(int argc, _TCHAR* argv[])
{
	ifstream fin("test.in");
	ofstream fout("test.out");
	int l, d, n;
	fin >> l >> d >> n;

	for (int i = 0; i < d; ++i) {
		string tt;
		fin >> tt;
//		cout << tt << endl;
		node* tem = root;
		for (int j = 0; j < l; ++j) {
			int tm = tt[j] - 'a';
			if (tem->children[tm] == NULL) {
				tem->children[tm] = new node();
			}
			tem = tem->children[tm];
		}
	}

	for (int i = 0; i < n; ++i) {
		ccount = 0;
		string tt;
		fin >> tt;

		process(tt, root);
		
		fout << "Case #" << i + 1 << ": " << ccount << endl;

		cout << "Case #" << i + 1 << ": " << ccount << endl;
	}

	string ttt;
	cin >> ttt;

	return 0;
}

