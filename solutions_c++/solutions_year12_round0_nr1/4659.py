#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;
int main()
{
	map<char,char> k;
	string in="ejp mysljylc kd kxveddknmc re jsicpdrysi"
			 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
			 "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string ou="our language is impossible to understand"
			 "there are twenty six factorial possibilities"
			 "so it is okay if you want to just give up";
	for(int i=0;i<in.size();i++)
		k[in[i]] = ou[i];
	k['y'] = 'a';
	k['e'] = 'o';
	k['q'] = 'z';
	k[' '] = ' ';
	k['z'] = 'q';
	for(unsigned i='a';i<='z';i++)
		cout << k[i] << "\n";
	int n=0;
	ifstream cin("a.in");
	ofstream cout("a.out");
	cin >> n;
	string line;
	getline (cin,line);
	for(unsigned i=1;i<=n;i++)
	{
		getline (cin,line);
		cout << "Case #"<<i << ": ";
		for(unsigned j=0;j<line.size();j++)
			cout << k[line[j]];
		cout << "\n";
	}
	return 0;
}