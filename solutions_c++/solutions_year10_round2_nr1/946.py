#include<iostream>
#include<map>

using namespace std;

struct directory {
	map<string, directory> paths;
};

void printpath(string root, map<string, directory> & childs) {
    cout << root << endl;
    map<string, directory>::iterator i;
    for(i = childs.begin(); i != childs.end(); ++i) {
        string n = i->first;
	map<string, directory> nc = childs[n].paths;
    	printpath(root + "/" + n, nc);
    }
}

int putpath(map<string, directory> & root, string name) {
	int created = 0;
	int pos = name.find("/", 1);
	if (pos == string::npos) {
		string dir = name.substr(1);		
		if (root.find(dir) == root.end()) {
			directory n; root[dir] = n;
			created++;
		}
	} else {
		string dir = name.substr(1, pos - 1);
		if (root.find(dir) == root.end()) {
			directory n; root[dir] = n;
			created++;
		}
		created += putpath(root[dir].paths, name.substr(pos));	
	}
	return created;
}

void solve(int tc) {
	int e, n; cin >> e >> n;
	map<string, directory> root;
	
	for (int i = 0; i < e; i++) {
		string name; cin >> name;
		putpath(root, name);
	}

	int total = 0;
	for (int i = 0; i < n; i++) {
		string name; cin >> name;
		total += putpath(root, name);
	}
	
	//printpath("", root);
	
	cout << "Case #" << tc << ": " << total << endl;
}

int main() {
	int ntc; cin >> ntc;
	for (int i = 0; i < ntc; i++) solve(i + 1);
	
	return 0;
}
