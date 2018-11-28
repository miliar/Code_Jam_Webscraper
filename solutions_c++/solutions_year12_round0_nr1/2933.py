#include<iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
using namespace std;

ifstream fin("A.in", ios::in);
ofstream fout("result.txt");

class Googlerese
{
public:
	map<char, char> resolve(vector<string> org, vector<string> out)
	{
		map<char, char> resolved;
		vector<bool> exist(26, false);
		for(int i = 0; i < org.size(); ++ i){
			for(int j = 0; j < org[i].length(); ++ j){
				if(org[i][j] == ' ') continue;
				resolved[org[i][j]] = out[i][j];
				exist[out[i][j]-'a'] = true;
			}
		}
		char no1 = ' ', no2 = ' ';
		for(char i ='a'; i <= 'z'; ++ i){
			if(resolved.find(i) == resolved.end()) no1 = i;
			if(!exist[i-'a']) no2 = i;
		}
		resolved[no1] = no2;			
		return resolved;
	}
};
int main()
{
	string orgs[] = {"y qee", "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string outs[] = {"a zoo", "our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
	vector<string> out(outs, outs+4), org(orgs, orgs+4);
	Googlerese g;
	map<char, char> resolved = g.resolve(org, out);

	char orig[128];
	int i = 1;
	while(fin.getline(orig, 128)){
		if(orig[0] >= '0' && orig[0] <= '9'){i = 1; continue;}
		for(int i = 0; orig[i] != '\0'; ++ i){
			if(resolved.find(orig[i]) != resolved.end()) orig[i] = resolved[orig[i]];
		}
		fout<<"Case #"<<i<<": "<<orig<<endl;
		++ i;
	}
	return 0;
}