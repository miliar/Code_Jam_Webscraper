#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main (){
	ofstream out;
	out.open("out");	

	int n;
	cin >> n;
	string c;
	getline(cin,c);
	
	for(int i=0; i<n; ++i){
		string s;
		getline (cin,s);
		for(int j=0; j< s.length(); ++j){
			switch (s[j]){
				case 'a': s[j] = 'y'; break;
				case 'b': s[j] = 'h'; break;
				case 'c': s[j] = 'e'; break;
				case 'd': s[j] = 's'; break;
				case 'e': s[j] = 'o'; break;
				case 'f': s[j] = 'c'; break;
				case 'g': s[j] = 'v'; break;
				case 'h': s[j] = 'x'; break;
				case 'i': s[j] = 'd'; break;
				case 'j': s[j] = 'u'; break;
				case 'k': s[j] = 'i'; break;
				case 'l': s[j] = 'g'; break;
				case 'm': s[j] = 'l'; break;
				case 'n': s[j] = 'b'; break;
				case 'o': s[j] = 'k'; break;
				case 'p': s[j] = 'r'; break;
				case 'q': s[j] = 'z'; break;
				case 'r': s[j] = 't'; break;
				case 's': s[j] = 'n'; break;
				case 't': s[j] = 'w'; break;
				case 'u': s[j] = 'j'; break;
				case 'v': s[j] = 'p'; break;
				case 'w': s[j] = 'f'; break;
				case 'x': s[j] = 'm'; break;
				case 'y': s[j] = 'a'; break;
				case 'z': s[j] = 'q'; break;
			}
		}

		out << "Case #" << i+1 << ": " << s << endl;
	} 
	
	out.close();
	return 0;
}

 
