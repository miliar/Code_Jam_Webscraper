#include <iostream>
#include <fstream>
#include <list>
#include <map>
#include <string>

using namespace std;

int charToInt(char c) {
	switch (c)
	{
		case 'Q':
			return 1;
		case 'W':
			return 2;
		case 'E':
			return 3;
		case 'R':
			return 4;
		case 'A':
			return 5;
		case 'S':
			return 6;
		case 'D':
			return 7;
		case 'F':
			return 8;
		default:
			cout << "----------WTF?????----------" << endl;
	}
	return 0;
}

int main()
{
	int t;
	ifstream inf("inputB.txt");
	ofstream outf("outputB.txt");
	inf >> t;
	list<char> l;
	map<string, char> create;
	list<string> del;
	
	for (int i = 1; i <= t; i++) {
		int met[9] = {0};
		l.clear();
		create.clear();
		del.clear();
		int cr_count;
		inf >> cr_count;
		for (int j = 0; j < cr_count; j++) {
			string str ,str2;
			inf >> str;
			str2 = string("") + str[0] + str[1];
			create[str2] = str[2];
			str2 = string("") + str[1] + str[0];
			create[str2] = str[2];
		}
		int del_count;
		inf >> del_count;
		for (int j = 0; j < del_count; j++) {
			string str;
			inf >> str;
			del.push_back(str);
			
		}
		int len;
		string str;
		inf >> len;
		inf >> str;

		for (int j = 0; j < len; j++) {
			char c = str[j];
			if (l.size() > 0) {
				if (create.find(string("") + l.back()+c) != create.end()) {
					char last = l.back();
					met[charToInt(last)]--;
					l.pop_back();
					l.push_back(create[string("")+last+c]);
				} else {
					met[charToInt(c)]++;
					bool f = false;
					for (list<string>::iterator it = del.begin(); it != del.end(); ++it) {
						if (met[charToInt((*it)[0])] && met[charToInt((*it)[1])])
							f = true;
					}
					if (f) {
						l.clear();
						memset(met, 0, sizeof(met));
					} else {
						l.push_back(c);
						
					}
				}
			} else {
				l.push_back(c);
				met[charToInt(c)]++;
			}
		}
		
		cout << l.size() << "   ";
		for (list<char>::iterator it = l.begin(); it != l.end(); ++it)
			cout << *it << " ";
		cout << endl;
		outf<< "Case #" << i<< ": [";
		int k = 1;
		for (list<char>::iterator it = l.begin(); it != l.end() && k!=l.size(); ++it) {
			k++;
			outf << *it << ", ";
		}
		if (l.size() != 0)
			outf << l.back();
		outf << "]" << endl;
	}
	inf.close();
	outf.close();
	return 0;
}