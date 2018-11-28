#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
using namespace std;
#define N 61

//ifstream fin("a.in");
//#define cin fin

int symN;
map<char,int> val;

int main(){
	int T;
	cin>>T;
	long long sec;
	string s;
	for(int x = 1; x <= T; x ++){
		symN = 0;
		val.clear();
		cin>>s;
		for(int i = 0; i < s.size(); i ++){
			if(val.find(s[i])==val.end()){
				if(symN < 2)
					val.insert(make_pair(s[i],1-symN));
				else
					val.insert(make_pair(s[i],symN));
				symN ++;
			}
		}
		sec = val[s[0]];
		if(symN == 1)
			symN = 2;
		for(int i = 1; i < s.size(); i ++){
			sec = sec * symN + val[s[i]];
		}
		cout<<"Case #"<<x<<": "<<sec<<endl;
	}
	return 0;
}
