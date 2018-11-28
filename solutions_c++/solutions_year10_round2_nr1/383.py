#include<iostream>
#include<vector>
#include<string>

using namespace std;

class Catalog {
public:
	vector<string> childrenNames;
	vector<Catalog *> children;
	
	Catalog() {}

	int addChild(string path) {
		if (path == "") {
			return 0;
		}
		string s = "";
		int i = 1;
		while(i < path.length() && path[i] != '/') {
			s = s + path[i];
			++i;
		}
		string newPath = "";
		for (int j = i; j < path.length(); ++j) {
			newPath = newPath + path[j];
		}
		for (int j = 0; j < childrenNames.size(); ++j) {
			if (s == childrenNames[j]) {
				return children[j]->addChild(newPath);
			}
		}
		childrenNames.push_back(s);
		Catalog * newChild = new Catalog();
		children.push_back(newChild);
		return newChild->addChild(newPath) + 1;
	}
};

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int m, n;
		cin >> n;
		cin >> m;
		Catalog * root = new Catalog();
		for (int k = 0; k < n; ++k) {
			string s;
			cin >> s;
			root->addChild(s);
		}
		int res = 0;
		for (int k = 0; k < m; ++k) {
			string s;
			cin >> s;
			res += root->addChild(s);
		}
		cout << "Case #" << i + 1 << ": " << res << endl;
	}
	return 0;
}