/*
 * cj10q1b.cpp
 *
 *  Created on: Mar 19, 2012
 *      Author: rickyjeremiah
 */

#include <iostream>
#include <string>

using namespace std;
int main(){
	int n;
	string s;
	cin>>n;
	getline(cin,s);
	for(int a=1; a<=n; a++){
		getline(cin,s);
		cout <<"Case #"<< a <<": ";
		for(int i = 0 ; i< s.length() ; i++){
			if(s[i] == ' '){
				cout << " ";
			}
			else{
				switch(s[i]){
					case 'y': cout <<'a';break;
					case 'n': cout <<'b';break;
					case 'f': cout <<'c';break;
					case 'i': cout <<'d';break;
					case 'c': cout <<'e';break;
					case 'w': cout <<'f';break;
					case 'l': cout <<'g';break;
					case 'b': cout <<'h';break;
					case 'k': cout <<'i';break;
					case 'u': cout <<'j';break;
					case 'o': cout <<'k';break;
					case 'm': cout <<'l';break;
					case 'x': cout <<'m';break;
					case 's': cout <<'n';break;
					case 'e': cout <<'o';break;
					case 'v': cout <<'p';break;
					case 'z': cout <<'q';break;
					case 'p': cout <<'r';break;
					case 'd': cout <<'s';break;
					case 'r': cout <<'t';break;
					case 'j': cout <<'u';break;
					case 'g': cout <<'v';break;
					case 't': cout <<'w';break;
					case 'h': cout <<'x';break;
					case 'a': cout <<'y';break;
					case 'q': cout <<'z';break;
				}
			}
		}
		cout << endl;
	}
	return 0;
}


