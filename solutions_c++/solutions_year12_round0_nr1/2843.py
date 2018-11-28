#include <iostream>
#include <map>
#include <fstream>
#include <cstring>
#include <string>
using namespace std;

map<char, int> myMap;
void init()
{
	string pre_str = "zyeqejp mysljylc kd kxveddknmc re jsicpdrysi"
					"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
					"de kr kd eoya kw aej tysr re ujdr lkgc jv";

	string cur_str = "qaozour language is impossible to understand"
					"there are twenty six factorial possibilities"
					"so it is okay if you want to just give up";
	myMap['z'] = 0;
	for(string::size_type i = 0; i < pre_str.size(); i++)
	{
		if(isalpha(pre_str[i]) && !myMap[pre_str[i]])
		{
			myMap[pre_str[i]] = cur_str[i] - pre_str[i];
		}
	}
	/*map<char, int>::iterator iter = myMap.begin();

	for(iter = myMap.begin(); iter != myMap.end(); iter++)
	{
		cout << iter->first << " " << iter->second << endl;
	}*/
}

int main(void)
{
	int cas, cas_c = 1;
	init();
	ifstream fin("A-small-attempt1.in");
	ofstream fout("A-small-attempt1.out");
	fin >> cas;
	fin.ignore();
	while(cas--)
	{
		string str;
		getline(fin, str);
		fout << "Case #" << cas_c++ << ": ";
		/*fout << str << "   :";*/
		for(string::size_type i = 0; i < str.size(); i++)
		{
			if(isspace(str[i]))
				fout << str[i];
			else if(isalpha(str[i]))
				fout << (char)(str[i] + myMap[str[i]]);
		}
		fout << endl;
	}
	return 0;
}