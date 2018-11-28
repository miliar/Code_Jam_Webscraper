#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
using namespace std;

#define FOR(i,a) for (int (i)=0;(i)<(a);++(i))
#define FORR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define sz(a) int((a).size()) 
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end() 
#define iter(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)


main(){
	ofstream fout ("A-small-attempt0.out");
	ifstream fin ("A-small-attempt0.in");

	
	string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	map<char,char> mapping;
	FOR(i,sz(a)){
		mapping[a[i]]=b[i];
	}
	mapping['z']='q';
	mapping['q']='z';
	
	int T;
	fin>>T;
	char endline_eater[256];
	fin.getline (endline_eater,256);
	FOR(num,T){
		char input_ch[256];
		fin.getline (input_ch,256);
		string input = string(input_ch);
		string out=input;
		FOR(i,sz(input)){
			out[i]=mapping[input[i]];
		}
		fout<<"Case #"<<num+1<<": "<<out<<endl;
	}
	fout.close();
}
