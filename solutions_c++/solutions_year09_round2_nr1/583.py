#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>

using namespace std;

struct dtree
{
	double weight;
	bool subtrees;
	string prop;
	dtree *yes, *no;

	dtree() : yes(NULL), no(NULL), subtrees(false) { }

	void read(istringstream& s)
	{
		char c;
		do { s >> c; } while (c != '(');
		s >> weight;
		do { s >> c; } while (c != ')' && !isalpha(c));
		if (c != ')') {
			s.seekg(-1, ios::cur);
			subtrees = true;
			s >> prop;
			yes = new dtree; no = new dtree;
			yes->read(s); no->read(s);
			do { s >> c; } while (c != ')');
		}		
	}

	double calc(const set<string>& props) const
	{
		double res = weight;
		if (subtrees) {
			if (props.find(prop) != props.end()) res *= yes->calc(props);
			else res *= no->calc(props);
		}
		return res;
	}

	~dtree() { if (subtrees) { delete yes; delete no; } }
};

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int a, l;
		cin >> l;
		string tree, s;
		getline(cin, s);
		for (int j = 0; j < l; ++j) {
			getline(cin, s);
			tree += s;
		}
		dtree root;
		root.read(istringstream(tree));
		cin >> a;
		map<string, set<string>> animals;
		cout << "Case #" << (i + 1) << ":" << endl;
		for (int j = 0; j < a; ++j) {
			int n;
			string animal;
			set<string> props;
			cin >> animal;
			cin >> n;
			for (int k = 0; k < n; ++k) {
				string prop;
				cin >> prop;
				props.insert(prop);
			}
			cout.precision(7);
			cout << fixed << root.calc(props) << endl;
		}
	}
}
