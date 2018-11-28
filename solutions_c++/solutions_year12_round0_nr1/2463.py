#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstring>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;

char mapping[26];

void addChar(char a, char b)
{
	if(a==' ') return;
	char &m = mapping[a-'a'];
	if(m == '@')
		m = b;
	else
		if( m != b )
			cout<<"shoot"<<endl;
	return;
}

ifstream fin("A-small-attempt0.in");
#define cin fin
ofstream fout("A-small-attempt0.out");
#define cout fout

int main()
{
	for(int i=0; i<26; i++)
		mapping[i] = '@';
	string G[] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string S[] = {
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"};

	mapping['q' - 'a'] = 'z';
	mapping['z' - 'a'] = 'q';

	for(int i=0; i<3; i++)
		for(int j=0; j<G[i].size(); j++)
			addChar(G[i][j], S[i][j]);

	//for(int i=0; i<26; i++)
	//	cout<<(char)('a'+i) << " : " << mapping[i] <<endl;

	int tc;
	cin>>tc;
	string line; getline(cin, line);
	for(int t=0; t<tc; t++)
	{
		getline(cin, line);
		cout<<"Case #"<< t+1 <<": ";
		for(int i=0; i<line.size(); i++)
			if(line[i]==' ')
				cout<<" ";
			else
				cout<<mapping[line[i]-'a'];
		cout<<endl;
	}

	return 0;
}