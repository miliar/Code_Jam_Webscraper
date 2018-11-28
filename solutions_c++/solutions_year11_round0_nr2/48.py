//#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include <map>
using namespace std;
ifstream cin("B-large.in");
ofstream cout("B-large.out");
int main(){
int T;
cin >> T;
for (int i=1; i<=T; i++) {
map<pair<char,char>,char> zmap;
map<pair<char,char>,int> opp;
int C;
cin >> C;
for (int j=0; j<C; j++) {
string mx;
cin >> mx;
zmap[make_pair(mx[0],mx[1])] = mx[2];
zmap[make_pair(mx[1],mx[0])] = mx[2];
}
int D;
cin >> D;
for (int j=0; j<D; j++) {
string mx;
cin >> mx;
opp[make_pair(mx[0],mx[1])] = 1;
opp[make_pair(mx[1],mx[0])] = 1;
}
int N;
cin >> N;
string inp;
cin >> inp;
vector<char> zvec;
for (int j=0; j<(int)inp.length(); j++) {
	char input = inp[j];
	if (zvec.size() == 0) { zvec.push_back(input); continue; }
	//check combination
	if (zmap.find(make_pair(zvec[zvec.size()-1],input)) != zmap.end()) { zvec[zvec.size()-1] = zmap[make_pair(zvec[zvec.size()-1],input)]; continue; }
	//check nullification
	bool nullified = false;
	for (int k=0; k<zvec.size(); k++) {
		if (opp.find(make_pair(zvec[k],input)) != opp.end()) { zvec.clear(); nullified = true; break; }
	}
	if (!nullified) zvec.push_back(input);
}
cout << "Case #"<<i<<": [";
if (zvec.size() > 0) {
for (int j=0; j<zvec.size()-1; j++) {
	cout << zvec[j] <<", ";
}
cout << zvec[zvec.size()-1];
}
cout << "]" << endl;
}
return 0;
}
