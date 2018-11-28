#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

#define REP(x,a,n) for(int x=(a); x<(n); x++)
#define rep(x,n) REP(x,0,n)

using namespace std;

int mkdirs;

class Dir {
	public:
	string name;
	vector<Dir> children;

	Dir(string n):name(n) {}
	void print() {
		for(vector<Dir>::iterator it = children.begin(); it < children.end(); it++) {
			cout << it->name << " (";
			it->print();
			cout << ")  ";
		}
	}
	void addPath(string path, bool creating) {
		if(path.length() == 0) return;

		string::size_type f = path.find_first_of('/');
		string d;
		if(f != string::npos) {
			d = path.substr(0,f);
			path = path.substr(f+1);
		} else {
			d = path;
			path = "";
		}
		bool found = false;
		for(vector<Dir>::iterator it = children.begin(); it < children.end(); it++) {
			if(d.compare(it->name) == 0) {
				found = true;
				it->addPath(path, creating);
			}
		}
		if(!found) {
			if(creating) {
				mkdirs++;
			}
			children.push_back(d);
			children.back().addPath(path, creating);
		}
	}
};

void main2() {
	Dir root("");
	int N, M;
	cin >> N >> M;
	rep(i,N) {
		string path;
		cin >> path;
		path = path.substr(1);
		root.addPath(path,false);
	}
	mkdirs = 0;
	rep(i,M) {
		string path;
		cin >> path;
		path = path.substr(1);
		root.addPath(path,true);
	}
	cout << mkdirs;
}

int main() {
	int T, caseno = 1;
	cin >> T;

	while(caseno <= T) {
		cout << "Case #" << caseno++ << ": ";
		main2();
		cout << endl;
	}
	return 0;
}
