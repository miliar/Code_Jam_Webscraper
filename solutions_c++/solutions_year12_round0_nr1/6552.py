#include <string>
#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt1.in");
ofstream fout("A-small-attempt1.out");
int main()
{
	string in[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
			"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
			"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string out[3] = {"our language is impossible to understand",
			"there are twenty six factorial possibilities",
			"so it is okay if you want to just give up"};
	char mapping[26];
	for(int i = 0; i < 3; i++)
	{
		int len = in[i].length();
		for(int j = 0; j < len; j++)
		{
			mapping[in[i][j]-'a'] = out[i][j];
		}
	}
	mapping['z'-'a'] = 'q';
	mapping['q' - 'a'] = 'z';
	int num;
	fin>>num;
	string str;
	getline(fin, str);
	for(int i = 0; i < num; i++)
	{
		getline(fin, str);
		int len = str.length();
		for(int j = 0; j < len; j++)
		{
			if(str[j]>'z'||str[j]<'a')
				continue;
			str[j] = mapping[str[j] - 'a'];
		}
		fout<<"Case #"<<i+1<<": "<<str<<endl;
	}
	return 0;
}
