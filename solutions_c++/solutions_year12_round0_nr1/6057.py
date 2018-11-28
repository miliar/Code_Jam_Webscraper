//============================================================================
// Name        : Codejam_Speaking_Tonges.cpp
// Author      : sanjay kumar
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string.h>

char charmap[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

#define MAX 2000
using namespace std;

int main() {
	ifstream fin("small.in");
	ofstream fout("small.out");
	int T;
	string str;
	getline(fin,str);
	T = atoi(str.c_str());

	int count = 1;
	while( count <= T ){
		string s1;
		getline(fin, s1);
		fout<<"Case #"<<count<<": ";
		for(int i=0;i<s1.length();++i ){
			if( s1[i] == ' ')
				fout<<' ';
			else
				fout<<charmap[s1[i]-'a'];
		}
		fout<<"\n";
		//fin>>C;fin>>L;
		//cout<<s1<<endl;
		count+=1;
	}

	return 0;
}
