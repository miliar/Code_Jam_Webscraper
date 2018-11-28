#include<iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
using namespace std;

// Problem C
ifstream fin("C.in");
ofstream fout("C.out");

void add1(string& a)
{
	int i = a.length()-1;
	while(i >= 0){
		if(a[i] == '9') a[i] = '0';
		else {++ a[i]; break;}
		-- i;
	}
}

int main()
{
	int testcases = 0;
	set<string> cand;
	fin >> testcases;
	for(int i = 1; i <= testcases; ++ i){
		string a, b;
		fin >> a>> b;
		int ans = 0;
		while(a < b){
			cand.clear();
			for(int j = 1; j < a.length(); ++ j){
				if(a[j] < a[0])  continue;
				string temp = a.substr(j)+a.substr(0, j);
				if(temp > a && temp <= b) cand.insert(temp);
			}
			ans += cand.size();
			add1(a);
		}
		fout<<"Case #"<<i<<": "<<ans<<endl;
	}//while
	return 0;
}

/*
//Problem B
ifstream fin("B.in");
ofstream fout("B.out");


int main()
{
	int uns[11], sur[11];
	uns[0] = sur[0] = 0;
	uns[1] = sur[1] = 1;
	for(int i = 2; i <= 10; ++ i){
		uns[i] = i+2*(i-1);
		sur[i] = i+2*(i-2);
	}

	int testcases = 0, N, p, s, t;
	fin >> testcases;
	for(int i = 1; i <= testcases; ++ i){
		fin >> N >> s>> p;
		int ans = 0;
		for(int j = 0; j < N; ++ j){
			fin>>t;
			if(t >= uns[p]) ++ ans;
			else if(t >= sur[p] && s > 0){ ++ ans; --s;}
		}
		fout<<"Case #"<<i<<": "<<ans<<endl;
	}
}*/

/*
//Problem A.
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
}*/