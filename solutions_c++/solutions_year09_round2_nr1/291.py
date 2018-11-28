#include <iostream>
#include <cassert>
#include <boost/algorithm/string/trim.hpp>
#include <fstream>
#include <set>

using namespace std;
using namespace boost;
using namespace algorithm;


struct Node {
	string f;
	double w;

	Node* l;
	Node* r;
};


int lookForClosingRoundBracket(string& s, int start) {
	int open = 0;

	int i, len = s.length();
	for (i = start+1; i < len; i++) {
		open += (s[i] == '(');
		open -= (s[i] == ')');

		if (open < 0)
			break;
	}

	return i;
}

string substring(const string& str, int start, int end) {
	return str.substr(start, end-start);
}


Node* buildTree(string& s) {
	Node* node = new Node;

	trim(s);
	sscanf(s.c_str(), "%lf", &(node->w));

	for (int i = 0; i < s.length() && s[i] != ' '; i++) {
		s[i] = ' ';
	}
	trim(s);

	if (s.empty()) {
		return node;
	}

	string f = "";
	for (int i = 0; i < s.length() && s[i] != ' ' && s[i] != '('; i++) {
		f += s[i];
		s[i] = ' ';
	}
	node->f = f;

	trim(s);

	int i = 1;
	int temp = lookForClosingRoundBracket(s, i);

	string s1 = substring(s, i, temp);
	node->l = buildTree(s1);

	i = temp;
	while (s[i] != '(') {
		i++;
	}
	i++;

	temp = lookForClosingRoundBracket(s, i);
	string s2 = substring(s, i, temp);
	node->r = buildTree(s2);

	return node;
}


int main() {
	int n;

	ifstream fin("a.in");

	fin >> n;
	for (int t = 0; t < n; t++) {
		cout << "Case #" << t+1 << ":" << endl;
		int l, a;
		string s;

		fin >> l;
		getline(fin, s);
		s = "";
		for (int i = 0; i < l; i++) {
			string temp;
			getline(fin, temp);
			trim(temp);

			s += temp;
		}

		trim(s);
		s[0] = s[s.length()-1] = ' ';
		Node* node = buildTree(s);
		Node* backup = node;

		fin >> a;
		for (int i = 0; i < a; i++) {
			string name;
			int q;

			fin >> name >> q;
			set<string> fset;
			for (int j = 0; j < q; j++) {
				string temp;
				fin >> temp;

				fset.insert(temp);
			}

			double res = 1.0;
			while (true) {
				res *= node->w;

				if (node->f.empty())
					break;

				if (fset.find(node->f) == fset.end()) {
					node = node->r;
				} else {
					node = node->l;
				}
			}
			cout << res << endl;

			node = backup;
		}
	}
}

