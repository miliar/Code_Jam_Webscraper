/*
 * main.cpp
 *
 *  Created on: 2012.04.14.
 *      Author: Peti
 */


#include<iostream>
#include<sstream>
#include<fstream>

using namespace std;

int main(){
	ifstream inp("be.txt");
	ifstream abcf("abc.txt");
	ofstream op("Output.txt");
	stringstream ss;
	string s;
	string s1;
	char abc[26];
	int i,j,sorok;
	for(i=0;i<26;i++){
		getline(abcf,s);
		abc[s[1]-97]=s[0];
	}
	for(i=0;i<26;i++){
		cout<<i<<' '<<abc[i]<<'\n';
	}
	getline(inp,s);
	ss<<s;
	ss>>sorok;
	//cout<<sorok<<"\n";
	for(i=0;i<sorok;i++){
		getline(inp,s);
		cout<<s<<"\n";
		op<<"Case #"<<i+1<<": ";
		for(j=0;j<int(s.length());j++){
			if(s[j]!=32){
				op.put(abc[s[j]-97]);
				cout<<abc[s[j]-97];
			}else{
				op.put(' ');
				cout<<' ';
			}
		}
		cout<<'\n';
		op.put('\n');
	}

	inp.close();
	abcf.close();
	op.close();
}

