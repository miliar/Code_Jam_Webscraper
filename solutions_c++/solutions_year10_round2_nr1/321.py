#include <sstream>
#include <set>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <map>
using namespace std;

set<string> adj[50000];
map<string, int> mapa;
int counter = 0;

int addpath(string dir){
	replace(dir.begin(), dir.end(), '/', ' ');
	istringstream is(dir);
	string acu = "/";
	int ret = 0;
	string folder;
	int index;
	while(is >> folder){
		int index = mapa[acu];
		acu += folder + "/";
		if(adj[index].count(folder) == 0){
			adj[index].insert(folder);
			ret++;
			mapa[acu] = counter++;
		}
	}
	//cout << dir << " " << ret << endl;
	return ret;
}

int main(){
	int t; cin >> t;
	for(int tt = 1; tt <= t; tt++){
		int n, m;
		cin >> n >> m;
		mapa.clear();
		counter = 0;
		mapa["/"] = counter++;
		
		for(int i = 0; i < 50000; i++)
			adj[i] = set<string>();
		
		for(int i = 0; i < n; i++){
			string dir; cin >> dir;
			dir += "/";
			addpath(dir);
		}
		int res = 0;
		for(int i = 0; i < m; i++){
			string dir; cin >> dir;
			dir+="/";
			res += addpath(dir);
		}
		cout << "Case #"<<tt<<": "<<res << endl;
	}
} 
