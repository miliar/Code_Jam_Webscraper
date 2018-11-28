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
int next(int value){
	stringstream ss;ss<<value;
	string s = "0" + ss.str();
	std::next_permutation(s.begin(),s.end());
	return strtol(s.c_str(),0,10);
}
int main(){
	int k;
	string line;
	getline(cin,line);
	stringstream(line) >> k;
	for(int i=1;i<=k;++i){
		getline(cin,line);
		stringstream ss(line);
		int n;ss>>n;
		cout << "Case #"<<i<<": ";
		cout << next(n);
		cout << endl;
	}
}
