#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

int main () {

freopen("As.in", "r", stdin); //for small input
freopen("As.out", "w", stdout);

//freopen("Al.in, "r", stdin); //for large input
//freopen("Al.out, "r", stdout);

int T;
map<char, char> mapping;
string l1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string l1t = "our language is impossible to understand";
string l2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string l2t = "there are twenty six factorial possibilities";
string l3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
string l3t = "so it is okay if you want to just give up";
mapping['y'] = 'a';
mapping['e'] = 'o';
mapping['z'] = 'q';
mapping['q'] = 'z';
for (int i = 0; i < l1.size(); ++i) {
	if (l1.at(i) == ' ') continue;
	mapping[l1.at(i)] = l1t.at(i);
	}
for (int i = 0; i < l2.size(); ++i) {
	if(l2.at(i) == ' ') continue;
	mapping[l2.at(i)] = l2t.at(i);
	}
for (int i = 0; i < l3.size(); ++i) {
	if (l3.at(i) == ' ') continue;
	mapping[l3.at(i)] = l3t.at(i);
}
cin >> T;
string p;
getline (cin, p);
for (int t = 1; t <= T; ++t) {
	cout << "Case #" << t << ": ";
	string G;
	getline (cin, G);
	for (int i = 0; i < G.size(); ++ i) {
		if (G.at(i) == ' ') cout << ' ';
			else cout << mapping[G.at(i)];
	}
	cout << endl;
}
	
return 0;
}
