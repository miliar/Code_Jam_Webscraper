#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <map>
using namespace std;
map<string,bool> existing;
int sol = 0;
void dodaj(string s, int dod) {
//     cout << s << endl;
    string tmp, path;
    stringstream ss(s);
    getline(ss,tmp,'/');
    while(getline(ss, tmp, '/')) {
	path += "/";
	path += tmp;
	if(existing[path] == false) {
	    existing[path] = true;
	    sol += dod;
// 	    if(dod = 1)
// 		cout << "dodaje " << path << endl;
	}
    }
}
int main() {
    ios_base::sync_with_stdio(0);
    int z;
    cin >> z;
    for(int i=1; i<=z; i++) {
	int ilea, ileb;
	sol = 0;
	existing.clear();
	cin >> ilea >> ileb;
	cin.ignore();
	while(ilea--) {
	    string s;
	    getline(cin,s);
	    dodaj(s,0);
	}
	while(ileb--) {
	    string s;
	    getline(cin,s);
	    dodaj(s,1);
	}
	cout << "Case #" << i << ": " << sol << endl;
    }
    return 0;
}