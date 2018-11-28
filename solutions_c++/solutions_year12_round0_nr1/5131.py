//ASSIGNMENT 313
#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<set>
#include<map>
#include<algorithm>
#include<cstring>
#include<iomanip>
#include<cmath>
#include<queue>

using namespace std;
map<string, int> vars;

int main(){
	map<char, char> m;
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';   
	m['f'] = 'c'; 
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';    
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';   
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r'; 
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n'; 
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';   
	m['z'] = 'q'; 
	
	
	
	int n;
	cin >> n;
	cin.ignore();
	string line;
	for(int cs=0; cs<n; cs++){
		getline(cin, line);
		cout << "Case #" << cs+1 << ": ";

		for(int i=0; i<line.size(); i++){
			if(m.find(line[i])==m.end()){
				cout << line[i];
			}
			else{
				cout << m[line[i]];
			}
		}
		cout << endl;
	}

	return 0;
}
