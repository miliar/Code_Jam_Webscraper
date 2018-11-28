using namespace std;

#include<iostream>
#include<fstream>
#include<map>
#include<string>

int main()
{
	ofstream fout ("tongues.out");
	ifstream fin ("tongues.in");
	int T;
	map<char, char> tr_map;
	string s1 =    "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string s1_tr = "our language is impossible to understand";
	for(int i =0; i < s1.size(); i++)
		tr_map[s1[i]]=s1_tr[i];
	s1 =    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s1_tr = "there are twenty six factorial possibilities";
	for(int i =0; i < s1.size(); i++)
		tr_map[s1[i]]=s1_tr[i];
	s1 =    "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	s1_tr = "so it is okay if you want to just give up";
	for(int i =0; i < s1.size(); i++)
		tr_map[s1[i]]=s1_tr[i];
	tr_map['q'] = 'z';
	tr_map['z'] = 'q';
	fin>>T;
	getline(fin, s1);
	for(int i=0; i < T; i++) 
	{
		string temp;
		getline(fin, temp);
		for(int j = 0; j < temp.size(); j++)
			temp[j] = tr_map[temp[j]];
		fout<< "Case #" << i+1 << ": " << temp << endl;
	}
	return 0;
}
