#include <cstdlib>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <map>
using namespace std;

int T, N, M;

class dir {
	public :
		string name;
		map<string, dir> child;
		
		dir() { name.clear(); child.clear(); }
		dir(string _n) { name = _n; child.clear(); }
		~dir() { child.clear(); }
};

dir ROOT("");

int add_dir(string x)
{
	vector<string> t;
	string n;
	int ret = 0;
	
	for (int i = 0; i < x.size(); ++i) if (x[i] == '/') x[i] = ' ';
	
	istringstream iss(x);
	while (iss >> n) {
		t.push_back(n);
	}
	
	dir* d = &ROOT;
	for (int i = 0; i < t.size(); ++i) {
		if (d->child.find(t[i]) == d->child.end() ) {
			++ret;
			d->child[t[i]] = dir(t[i]);
			//printf("INSERT - %s\n", t[i].c_str() );
		}
		d = &(d->child[t[i]]);
	}
	return ret;
}

int main(int argc, char *argv[])
{
    cin >> T;
    for (int i = 0; i < T; ++i) {
		cin >> N >> M;
		string x;
		int ans = 0;
		ROOT.child.clear();
		
		for (int j = 0; j < N; ++j) {
			cin >> x;
			add_dir(x);
		}
		for (int j = 0; j < M; ++j) {
			cin >> x;
			ans += add_dir(x);
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	
    return EXIT_SUCCESS;
}
