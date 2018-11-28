#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

map<char, char> table; 

int main(){
	ifstream cypher, plaintext;
	cypher.open("speaking.in");
	plaintext.open("speaking.out");
	
	//freopen("speaking.in", "r", stdin);
	
	int n;
	string s, t;
	cypher >> n;
	getline(cypher,s);
	
	table['q'] = 'z';
	table['z'] = 'q';
	table[' '] = ' ';
	for(int i = 0; i < n; i++){
		getline(cypher,s);
		getline(plaintext,t);
		//cout << s <<endl <<t << endl;;
		for(int j = 0; j < s.length(); j++)
			table[s[j]] = t[j];
		}
	/*
	for(int i = 'a'; i <= 'z'; i++)
		cout << table[i] << " ";
	*/
	scanf("%d\n", &n);
	for(int i = 0; i < n; i++){
		printf("Case #%d: ", i+1);
		getline (cin,s);
		for(int j = 0; j < s.length(); j++)
			cout << table[s[j]];
		cout << endl;	
		}
		
	return 0;
	}
