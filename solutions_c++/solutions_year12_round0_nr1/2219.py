#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
using namespace std;

int main()
{
	freopen("language.in","r",stdin);
	freopen("language.out","w",stdout);

	stringstream stream;
	string tests, alphabet("ynficwlbkuomxsevzpdrjgthaq "), alphabetb("abcdefghijklmnopqrstuvwxyz ");
	int test;
	getline (cin,tests);
	stream << tests;
	stream >> test;
	for (int i=1; i<=test; i++)
	{
		string google;
		getline (cin,google);
		for (int k=0; k<google.length(); k++)
		{
			for (int y=0; y<27; y++)
			{
				if (google[k]==alphabet[y]) {google[k]=alphabetb[y]; break;}
			}	
		}
		cout<<"Case #"<<i<<": "<<google<< endl;
	}
	return 0;
}
