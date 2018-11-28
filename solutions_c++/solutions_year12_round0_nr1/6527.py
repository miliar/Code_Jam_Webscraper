// ToungSpeaking.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
	map<char, char> translate;
	string s[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities", "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"};
	for(char i = 'a'; i <= 'z'; ++i)
	{
		translate[i] = 0;
	}
	translate['q'] = 'z';
	translate['z'] = 'q';
	for(int i = 0 ; i < 6 ; i+=2)
	{
		string line;
		string translated;
		line=s[i];//cin >> line;
		translated=s[i+1];//cin >> translate;
		for(int x = 0; x < line.length(); ++x)
		{
			translate[line[x]] = translated[x];
		}
	}
	ifstream r("test.txt");
	ofstream o("bla.txt");
	int cases;
	r >> cases;
	string bla;
	getline(r, bla);
	for(int i = 0 ; i < cases; ++i)
	{
		string line;
		getline(r, line);
		o << "Case #" << (i+1) << ": ";
		for(int x = 0 ; x < line.length() ; ++x)
			o << translate[line[x]];
		o << endl;
	}
	r.close();
	o.close();
	return 0;
}

