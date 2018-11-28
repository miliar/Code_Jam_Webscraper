#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("map.txt");
	ifstream fi("input.txt");
	ofstream fout ("output.txt");
	map<char,char> a;
	a[' ']=' ';
	char ch1,ch2;
	while (fin>>ch1>>ch2) a[ch1]=ch2;


	int n;
	fi>>n;
	string mystr;
	getline(fi,mystr);
	for (int i = 1 ; i <= n ; i++)
	{
	    getline(fi,mystr);
	    fout<<"Case #"<<i<<": ";
	    for (int j = 0 ; j < mystr.length(); j++) fout<<a[mystr[j]];
	    fout<<endl;
	}
	fout.close();
	return 0;
}
