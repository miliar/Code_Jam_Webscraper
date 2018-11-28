
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

struct Tree {
	double weight;
	string feature;
	Tree* first;
	Tree* second;
};

struct Animal {
	string name;
	vector<string> features;

	bool hasFeature(string s) {
		return find(features.begin(), features.end(), s) != features.end();
	}

	void addFeature(string s) {
		features.push_back(s);
	}

public:
	Animal(string n)
		: name(n) {}
};

double
isCute(Animal* animal, Tree* tree)
{
	double p = 1.0;
	while (tree) {
		p *= tree->weight;
		tree = animal->hasFeature(tree->feature)? tree->first: tree->second;
	}
	return p;
}

Tree*
mkTree()
{
	double w;
	string s;
	char c;

	Tree* t = 0;
	cin >> c;
	if (c == '(') {
		cin >> w;
		t = new Tree();
		t->weight = w;
	} else
		return t;
	cin >> c;
	if (c == ')')
		return t;
	cin.putback(c);
	cin >> s;
	t->feature = s;
	t->first = mkTree();
	t->second = mkTree();
	cin >> c;
	return t;
}

int
main()
{
	int N, L, A;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cout << "Case #" << i + 1 << ":" << endl;
		cin >> L;
		Tree* t = mkTree();
		cin >> A;
		for (int k = 0; k < A; k++) {
			string name, feat;
			cin >> name;
			Animal* an = new Animal(name);
			int nf;
			cin >> nf;
			for (int cf = 0; cf < nf; cf++) {
				cin >> feat;
				an->addFeature(feat);
			}
			cout << fixed << isCute(an, t) << endl;
		}
	}

}
