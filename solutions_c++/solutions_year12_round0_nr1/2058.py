//============================================================================
// Name        : CodeJam.cpp
// Author      : Daniel Rubio
// Version     : 1.0
// Copyright   : FreeWare
// Description : CodeJam 2011 - Qualification 1
//============================================================================

#include <iostream>
using namespace std;

char dixx[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char dicc[26] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
char dicr[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
	freopen("d:\\Downloads\\A-small-attempt0.in", "rt", stdin);
	freopen("d:\\Downloads\\A-small-attempt0.out", "wt", stdout);

	//declaramos variables
	int T;
	string input;

	//repeticiones
	scanf( "%d\n", &T );
	for(int r=0;r<T;r++){
		cout << "Case #" << r+1 << ": ";
		cerr << "Case #" << r+1 << ": ";

		input.clear();
		getline(cin,input);
		for(unsigned int i = 0;i<input.length();i++){
			if(input[i]!= ' '){
				input[i] = dicr[input[i]-'a'];
			}
		}

		cout << input << endl;
		cerr << input << endl;

	}
}
