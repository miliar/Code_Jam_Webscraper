#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <map>

using namespace std;

string exin[] = {
					"yeqz", 
					"ejp mysljylc kd kxveddknmc re jsicpdrysi",
					"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

string exout[] = {
					"aozq",
					"our language is impossible to understand",
					"there are twenty six factorial possibilities",
					"so it is okay if you want to just give up"};


int main()
{
	map<char, char> m;
	for(int i=0; i<4; i++) {
		for(int j=0; j<exin[i].length(); j++) {
			m.insert(make_pair(exin[i][j],exout[i][j]));
		}
	}

	//map<char,char>::iterator it;
	//for (it=m.begin(); it!=m.end(); it++)
	//	cout << (*it).first << " => " << (*it).second << endl;

	int T, N;
	string G;
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");	
	in>>T;
	getline(in, G);
	for(int t=0; t<T; t++) {
		getline(in, G);
		for(int i=0; i<G.length(); i++)
			G[i] = m[G[i]];
		//cout << "Case #" << (t+1) << ": " << G << endl;
		out << "Case #" << (t+1) << ": " << G << endl;
	}
	in.close();
	out.close();
	return 0;
}

