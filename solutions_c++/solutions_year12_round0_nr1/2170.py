#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	int cases(0);
	cin >> cases;
	map<char, char> characters;
	string a  = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string ab = "our language is impossible to understand";
	string b  = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string bb = "there are twenty six factorial possibilities";
	string c  = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string cb = "so it is okay if you want to just give up";

	characters['q'] = 'z';
	characters['z'] = 'q';
	for(int i=0; i<b.size(); i++)
	{
		if(i<a.size())
			characters[a[i]] = ab[i];
		characters[b[i]] = bb[i];
		if(i<c.size())
			characters[c[i]] = cb[i];
	}
	cin.ignore();
	for(int iterations=0; iterations<cases; iterations++)
	{
		string sentence;
		
		getline(cin, sentence);
		for(int i=0; i<sentence.size(); i++)
			sentence[i] = characters[sentence[i]];
		cout << "Case #" << iterations+1 << ": " << sentence << endl;
	}
	return 0;
}
