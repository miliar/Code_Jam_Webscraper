#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<string>
#include<iterator>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
typedef unsigned long long ull;
unsigned long long solve(string x){
	string base = x;
	map<char,int>table;
	for(int i=0;i<x.size();++i){
		if(!table.count(x[i])){
			int id = table.size() <= 1 ? table.size()^1 : table.size();
			table.insert(make_pair(x[i],id));
		}
	}
	unsigned long long result = 0;
	int radix = table.size() == 1 ? 2 : table.size();
	for(int i=0;i<x.size();++i){
		result = result * radix + table[x[i]];
	}
	return result;
}
int main(){
	int k;
	string line;
	getline(cin,line);
	stringstream(line) >> k;
	for(int i=1;i<=k;++i){
		getline(cin,line);
		cout << "Case #"<<i<<": ";
		cout << solve(line);
		cout << endl;
	}
}
