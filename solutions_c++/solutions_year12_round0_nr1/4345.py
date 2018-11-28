#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

main(){
	int T;
	string n;
	getline(cin, n);
	T = atoi(&n[0]);
	int count = 0;
	while(true){
		count++;
		if(count > T)	break;
		string G;
		getline(cin, G);
		string S;
		for(int i = 0; i < G.size(); i++){
			switch(G[i]){
				case 'y': S += 'a';
					break;
				case 'n': S += 'b';
					break;
				case 'f': S += 'c';
					break;
				case 'i': S += 'd';
					break;
				case 'c': S += 'e';
					break;
				case 'w': S += 'f';
					break;
				case 'l': S += 'g';
					break;
				case 'b': S += 'h';
					break;
				case 'k': S += 'i';
					break;
				case 'u': S += 'j';
					break;
				case 'o': S += 'k';
					break;
				case 'm': S += 'l';
					break;
				case 'x': S += 'm';
					break;
				case 's': S += 'n';
					break;
				case 'e': S += 'o';
					break;
				case 'v': S += 'p';
					break;
				case 'z': S += 'q';
					break;
				case 'p': S += 'r';
					break;
				case 'd': S += 's';
					break;
				case 'r': S += 't';
					break;
				case 'j': S += 'u';
					break;
				case 'g': S += 'v';
					break;
				case 't': S += 'w';
					break;
				case 'h': S += 'x';
					break;
				case 'a': S += 'y';
					break;
				case 'q': S += 'z';
					break;
				default: S += ' ';
			}
		}
		cout << "Case #" << count << ": " << S << endl;
	}
	return 0;
}
