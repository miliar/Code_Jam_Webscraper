#include <iostream>
#include <map>
#include <string>
#include <cstdlib>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	string from = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	string to =   "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

	map<char, char> mp;
	mp['q'] = 'z';
	mp['z'] = 'q';
	for(int i=0;i<from.size();i++)
		mp[from[i]] = to[i];
		
	/*
	for(char c='a';c<='z';c++) {
		cout << c << " -> " << mp[c] << endl;
	}*/
	
	string line;
	int T;
	cin >> T;
	cin.ignore();
	for(int t=1;t<=T;t++) {
		getline(cin, line);
		for(int i=0;i<line.size();i++) {
			line[i] = mp[line[i]];
		}
		cout << "Case #" << t << ": " << line << endl;
	}
	
	return 0;
}
