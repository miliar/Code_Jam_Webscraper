#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <string>

using namespace std;
map<char, char> temp ;


int main(){
	freopen("a.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	temp['q'] = 'z';
	temp['w'] = 'f';
	temp['e'] = 'o';
	temp['r'] = 't';
	temp['t'] = 'w';
	temp['y'] = 'a';
	temp['u'] = 'j';
	temp['i'] = 'd';
	temp['o'] = 'k';
	temp['p'] = 'r';
	temp['a'] = 'y';
	temp['s'] = 'n';
	temp['d'] = 's';
	temp['f'] = 'c';
	temp['g'] = 'v';
	temp['h'] = 'x';
	temp['j'] = 'u';
	temp['k'] = 'i';
	temp['l'] = 'g';
	temp['z'] = 'q';
	temp['x'] = 'm';
	temp['c'] = 'e';
	temp['v'] = 'p';
	temp['b'] = 'h';
	temp['n'] = 'b';
	temp['m'] = 'l';
	int n;
	cin>>n;
	string word;
	getline(cin, word);
	for(int i = 0; i < n; i++){
		//cin>>word;
		getline(cin, word);
		cout<<"Case #"<<(i+1)<<": ";
		for(int j = 0; j < word.length(); j++){
			if(word[j] == ' ')
				cout<<word[j];
			else
				cout<<temp[word[j]];
		}
		cout<<endl;
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}