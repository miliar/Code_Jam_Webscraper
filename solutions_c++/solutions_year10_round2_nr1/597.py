#include <iostream>
#include <fstream>
#include <set>
#include <string>
using namespace std;

set<string> mapa;


void add(string s){
	int i;
	int len = s.length();
	string slovo("");
	for (i=0; i<len; i++) {
		if(s[i] == '/'){
			if(slovo.length() > 0){
				mapa.insert(slovo);
			}
		}
		slovo.push_back(s[i]);
	}
	
	if(slovo.length() > 0){
		mapa.insert(slovo);
	}
		
}

int main (int argc, char * const argv[]) {
	
	int tests,test;
	
	int n, m, i;
	string s;
	ifstream in("A.in");
	ofstream out("A-out.txt");
	
	in >> tests;
	for (test = 0; test < tests; test++) {
		in >> n >> m;
		mapa.clear();
		for (i=0; i<n; i++) {
			in >> s;
			add(s);
		}
		for (i=0; i<m; i++) {
			in >> s;
			add(s);
		}
		out << "Case #" << test + 1 << ": " << mapa.size() - n << endl;
		cout << "Case #" << test + 1 << ": " << mapa.size() - n << endl;
	}
	
	cin >> n;
	
	return 0;
}
