#include <iostream>
#include <istream>
#include <sstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <map>

using namespace std;



void translate(string s, map<char,char> letter){
	string s2 = "";
	int len = s.length();
	for(int i=0;i<len;i++){
		s2 += letter[s[i]];
	}
	cout << s2 << endl;
}

int main(void){
	
	map<char,char> letter;
	letter[' ']=' ';
	letter['y']='a';
	letter['n']='b';
	letter['f']='c';
	letter['i']='d';
	letter['c']='e';
	letter['w']='f';
	letter['l']='g';
	letter['b']='h';
	letter['k']='i';
	letter['u']='j';
	letter['o']='k';
	letter['m']='l';
	letter['x']='m';
	letter['s']='n';
	letter['e']='o';
	letter['v']='p';
	letter['z']='q';
	letter['p']='r';
	letter['d']='s';
	letter['r']='t';
	letter['j']='u';
	letter['g']='v';
	letter['t']='w';
	letter['h']='x';
	letter['a']='y';
	letter['q']='z';
	
	int n=1;
	string input;
	string s;
	cin >> input;cin.get();
	stringstream myStream(input);
    myStream >> n;
	for (int testCase = 1; testCase <= n; testCase++) {
		printf("Case #%d: ",testCase);
		getline(cin,s);
		translate(s,letter);
	}
	return 0;
}
