#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;


int main()
{
	//a zoo -> y qee
	//ejp mysljylc kd kxveddknmc re jsicpdrysi -> our language is impossible to understand
	//rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd -> there are twenty six factorial possibilities
	//de kr kd eoya kw aej tysr re ujdr lkgc jv -> so it is okay if you want to just give up

	char mappings[26];
	int i,j,N;
	string s;

	string in[4] = {"a zoo","ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string out[4] = {"y qee","our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
	

	for(i=0;i<4;i++)
	{
		for(j=0;j<in[i].length();j++)
			if(in[i][j]!=' ')
				mappings[in[i][j]-97] = out[i][j];
	}
	mappings[16] = 'z';
	
	
	cin >> N;
	for(i=0;i<N+1;i++)
	{	
		getline(cin,s);
		if(i!=0)
		{
		for(j=0;j<s.length();j++)
		{
			if(s[j]!=' ')
				s[j] = mappings[s[j]-97];
		}
		cout<<"Case #"<<i<<": "<<s<<endl;
		}
	}		
	
}	
