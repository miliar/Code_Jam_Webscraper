#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

int main()
{
	ifstream in("large.in");
	ofstream out("large.out");

	int index[200];

	string c1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string c2 = "our language is impossible to understand";
	for (int i = 0; i < c1.length(); i++)
	{
		index[c1[i]] = c2[i];
	}

	c1  = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	c2 = "there are twenty six factorial possibilities";
	for (int i = 0; i < c1.length(); i++)
	{
		index[c1[i]] = c2[i];
	}

	c1  = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	c2 = "so it is okay if you want to just give up";
	for (int i = 0; i < c1.length(); i++)
	{
		index[c1[i]] = c2[i];
	}

	index['z'] = 'q';
	index['q'] = 'z';

	int T;
	in>>T;

	getline(in, c1);

	for ( int i = 1; i <= T; i++)
	{
		string a1;
		getline(in, a1);
		string a2(a1);
		for (int j = 0 ; j < a1.length(); j++)
		{
			a2[j] = index[a1[j]];
		}

		out<<"Case #"<<i<<": "<<a2<<endl;
	}
}