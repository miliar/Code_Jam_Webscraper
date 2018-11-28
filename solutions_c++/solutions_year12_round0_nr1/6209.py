#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define forLoop(i,n) for((i)=0;(i)<(int)(n);(i)++)

string translate(string toTranslate){
	int x;
	string a,b,result ="";
	char temp;
	
	map<string,string> m;
	m.insert(pair<string,string>("a","y"));
	m.insert(pair<string,string>("b","h"));
	m.insert(pair<string,string>("c","e"));
	m.insert(pair<string,string>("d","s"));
	m.insert(pair<string,string>("e","o"));
	m.insert(pair<string,string>("f","c"));
	m.insert(pair<string,string>("g","v"));
	m.insert(pair<string,string>("h","x"));
	m.insert(pair<string,string>("i","d"));
	m.insert(pair<string,string>("j","u"));
	m.insert(pair<string,string>("k","i"));
	m.insert(pair<string,string>("l","g"));
	m.insert(pair<string,string>("m","l"));
	m.insert(pair<string,string>("n","b"));
	m.insert(pair<string,string>("o","k"));
	m.insert(pair<string,string>("p","r"));
	m.insert(pair<string,string>("q","z"));
	m.insert(pair<string,string>("r","t"));
	m.insert(pair<string,string>("s","n"));
	m.insert(pair<string,string>("t","w"));
	m.insert(pair<string,string>("u","j"));
	m.insert(pair<string,string>("v","p"));
	m.insert(pair<string,string>("w","f"));
	m.insert(pair<string,string>("x","m"));
	m.insert(pair<string,string>("y","a"));
	m.insert(pair<string,string>("z","q"));

	forLoop(x,toTranslate.length()){
		a = toTranslate.substr(x,1);
		if(a.compare(" ") != 0){
			b = m.find(a)->second;
		}else{
			b = " ";
		}
		result.append(b);
	}
	return result;
}

/*
	Running Testcases
*/
int main(void){
	string s;
	int x,T;

	ifstream test;
	test.open("A-small-attempt1.in");

	getline(test,s);
	T = atoi(s.c_str());

	ofstream outFile;
	outFile.open("output.txt");

	forLoop(x,T){
		printf("Case #%d: ",x+1);
		getline(test,s);
		outFile << translate(s);
		outFile << endl;
	}
	outFile.close();
	test.close();
	return 0;
}