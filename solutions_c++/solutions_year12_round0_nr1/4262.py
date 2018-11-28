#include <iostream>
#include <string>
using namespace std;

char s[26];

string f(string str){
string r="";
for(int i =0;i<str.length();i++){
	r+=s[str[i]];
}
return r;
}

int main(){
	s[' '] = ' ';
	s['e'] = 'o'; //o
	s['j'] = 'u'; //u
	s['p'] = 'r'; //r
	s['m'] = 'l'; //l
	s['y'] = 'a'; //a
	s['s'] = 'n'; //n
	s['l'] = 'g'; //g
	s['c'] = 'e'; //e
	s['k'] = 'i'; //i
	s['d'] = 's'; //s
	s['x'] = 'm'; //m
	s['v'] = 'p'; //p
	s['n'] = 'b'; //b
	s['r'] = 't'; //t
	s['i'] = 'd'; //d
	s['b'] = 'h'; //h
	s['f'] = 'c'; //c
	s['w'] = 'f'; //f
	s['u'] = 'j'; //j
	s['o'] = 'k'; //k
	s['g'] = 'v'; //v
	s['t'] = 'w'; //w
	s['h'] = 'x'; //x
	s['a'] = 'y'; //y
	s['q'] = 'z'; //z
	s['z'] = 'q'; //q
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	for(int i=1;i<=t;i++){
		//string s;
		getline(cin,s);
		cout<<"Case #"<<i<<": "<<f(s)<<endl;
	}
	return 0;
}