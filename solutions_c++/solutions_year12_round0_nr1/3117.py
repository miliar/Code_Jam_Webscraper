#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int main()
{
	string dest[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
					"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string src[3] = {"our language is impossible to understand",
					"there are twenty six factorial possibilities",
					"so it is okay if you want to just give up"};
	map<char,char> mp;

	for(int i=0;i< 3;i++)
	{
		for(int j=0;j< dest[i].length();j++)
		{
			mp[dest[i][j]] = src[i][j] ;
			
		}
	}
	mp['q'] = 'z';
	mp['z'] = 'q';

	ifstream fr("A-small-attempt2.in");
	int N;
	fr>>N;
	vector<string > outstr;
	string temp;
	char c;
	int start = 0;
	string str;
	getline(fr,str);
	while(!fr.eof())
	{

		getline(fr,str);
		temp ="";
		for(int i=0;i< str.length();i++)
			//temp[i] = mp[str[i]];
			temp.push_back(mp[str[i]]);
		outstr.push_back(temp);
		
	}
	ofstream out("A-small-attempt2.out");
	int num = 1;
	for(int i=0;i< N;i++)
	{
		if(num > 1)
			out<<'\n';
		if(!outstr[i].empty())
		{
		out<<"Case #"<<num<<": "<<outstr[i];
		++num;
		}
	}


	return 0;
}