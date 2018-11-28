#include <cstdio>
#include <string>
#include <sstream>
#include <iostream>
#include <map>

using namespace std;

map<char,char> tr;
typedef map<char,char>::iterator MapIt;

void init()
{
	string a[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string b[] = {"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};

	for(int i=0;i<3;++i) {
		for(int j=0;j < a[i].size(); ++j) {
			if (a[i][j] != b[i][j]) { tr[a[i][j]] = b[i][j]; }
		}
	}
	tr['z']='q';
	tr['q']='z';

	/*
	for(map<char,char>::iterator it = tr.begin(); it != tr.end(); ++it) 
	{
		cout << it->first << "-" << it->second << endl;
	}
	*/
}

void printTr(string in)
{
	for(int i=0;i < in.size();++i) {
		MapIt it = tr.find(in[i]);
		if (it == tr.end()) {
			cout << in[i];
		} 
		else {
			cout << it->second;
		}
	}
	cout << endl;
}

int main()
{
	init();

	int cases;
	string in;
	//cin >> cases;
	getline(cin, in);
	istringstream(in) >> cases;
	for(int i=1;i <= cases;++i) {
		in.resize(200);
		getline(cin, in);
		cout << "Case #" << i <<": ";
		printTr(in);
	}
}
