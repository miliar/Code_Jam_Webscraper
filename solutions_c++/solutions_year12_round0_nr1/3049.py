#include<iostream>
#include<string>
#include<fstream>
using namespace std;
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
*/
int main(){
	
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int t;
	cin>>t;
	
	char gtoe[26];
	gtoe['a' -'a'] = 'y';
	gtoe['b' -'a'] = 'h';
	gtoe['c' -'a'] = 'e';
	gtoe['d' -'a'] = 's';
	gtoe['e' -'a'] = 'o';
	gtoe['f' -'a'] = 'c';
	gtoe['g' -'a'] = 'v';
	gtoe['h' -'a'] = 'x';
	gtoe['i' -'a'] = 'd';
	gtoe['j' -'a'] = 'u';
	gtoe['k' -'a'] = 'i';
	gtoe['l' -'a'] = 'g';
	gtoe['m' -'a'] = 'l';
	gtoe['n' -'a'] = 'b';
	gtoe['o' -'a'] = 'k';
	gtoe['p' -'a'] = 'r';
	gtoe['q' -'a'] = 'z';
	gtoe['r' -'a'] = 't';
	gtoe['s' -'a'] = 'n';
	gtoe['t' -'a'] = 'w';
	gtoe['u' -'a'] = 'j';
	gtoe['v' -'a'] = 'p';
	gtoe['w' -'a'] = 'f';
	gtoe['x' -'a'] = 'm';
	gtoe['y' -'a'] = 'a';
	gtoe['z' -'a'] = 'q';

	string tmp;
	getline(cin, tmp);
	for(int test=1; test<=t; test++){
		string s;
		getline(cin, s);
		for(int i=0; i<s.size(); i++){
			if(s[i]==' ')
				continue;
			s[i] = gtoe[s[i]-'a'];
		}
		cout<<"Case #"<<test<<": "<<s<<endl;
	}
	return 0;
}
