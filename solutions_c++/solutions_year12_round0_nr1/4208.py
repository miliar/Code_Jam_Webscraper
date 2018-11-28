#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <iostream>
using namespace std;

int main() {
	string s1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qeez";
	string s2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zooq";
	vector<int> v(28,0);
	map<char,char> mapa;

	for (int i=0; i<(int)s1.length();i++) {
		if (s1[i]!=' ' && v[s1[i]-'a'] == 0) {mapa[s1[i]]=s2[i]; v[s1[i]-'a']=1;}
	}
	mapa[' ']=' ';

	ifstream file;
	file.open("Asmall.in");
	ofstream out;
	out.open("output.dat");
	int nmax;
	file>>nmax;
	string str;
	string sol;
	getline(file,str);
	str.clear();

	for (int i=0; i<nmax; i++) {
		getline(file,str);
		for (int j=0; j<(int)str.length();j++) {
			sol.push_back(mapa[str[j]]);
		}
		out<<"Case #"<<i+1<<": "<<sol<<"\n";
		sol.clear();
		str.clear();
	}
	file.close();
	out.close();

	return 0;
}