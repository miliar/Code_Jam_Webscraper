#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	char c[26];

	c[0]='y'; c[1] ='h'; c[2]='e'; c[3]= 's'; c[4]='o'; c[5]='c';
c[6]='v'; c[7]='x'; c[8]='d'; c[9]='u'; c[10]='i'; c[11]='g'; c[12]='l';
c[13]='b'; c[14]='k'; c[15]='r'; c[16]='z'; c[17]='t'; c[18]='n'; c[19]='w';
c[20]='j'; c[21]='p'; c[22]='f'; c[23]='m'; c[24]='a'; c[25]='q';

	int cases=0;
	cin >> cases;
	vector <string> muchas;
		
	for(int i=0; i<cases+1;i++){
		string s;
		getline(cin, s);
		string t (s.size(),'-');
		for(int j=0; j< s.size();j++){
			if(s[j]==' '){
				t[j]=' ';
			}
			else{
				t[j]= c[(s[j]-'a')];
			}
		}
		muchas.push_back(t);
		cerr << s << endl;
		cerr << t << endl;
	}
	
	for(int i=1; i<muchas.size();i++){
		cout << "Case #" << i << ": " << muchas[i] << endl;
	}
	return 0;
}
