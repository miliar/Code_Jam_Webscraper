#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <string>

using namespace std;

#define VI			vector<int>
#define VVI			vector<VI>

#define MCC			map<char,char>

MCC G;

void getLang(){
	ifstream fin("file.txt");
	int N;
	vector<string> v1,v2;
	string str="a";
	
	while(fin >> str && str!="#")
		v1.push_back(str);
	while(fin >> str)
		v2.push_back(str);

	G['y'] = 'a';
	G['e'] = 'o';
	G['q'] = 'z';
	G['z'] = 'q';
	for(int i=0 ; i<v1.size() ; i++)
		for(int j=0 ; j<v1[i].size() ; j++)
			G[v1[i][j]] = v2[i][j];
}

int main(){
	getLang();

	int N;
	string str;
	ifstream cin("input.txt");
	ofstream cout("a.txt");

	cin >> N;
	getline(cin,str);
	for(int cnt=1 ; cnt<=N ; cnt++){
		getline(cin,str);
		for(int i=0 ; i<str.size() ; i++)
			if(str[i] != ' ')
				str[i] = G[str[i]];
		cout <<"Case #"<<cnt<<": "<<str<<endl;
	}
}