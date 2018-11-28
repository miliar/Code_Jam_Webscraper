#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>
#include <cstdio>

using namespace std;

int main(){		
	
	int T;
	cin >> T;
	string s;
	for (int i = 1 ; i <= T ; i++){		
		cin >> s;
		char* c = (char*) s.c_str();	
		if (next_permutation (c,c+s.size())){
			string temp(c);
			cout << "Case #" << i << ": " << temp << endl;
			//printf("Case #%d: %s\n", i, c);	
		}
		else {
			cout << "Case #" << i << ": ";
			int zeroes = 1;
			for (int j = 0; j < s.size(); j++){
				if (c[j] != '0'){
					cout << c[j];
					break;
				}
				else zeroes++;
			}
			for (int j = 0; j < zeroes; j++)
				cout << '0';
			for (int j = zeroes ; j < s.size() ; j++) cout << c[j];
			cout << endl;				
		}						
	}	
 
	return 0;
}