//speaking in tongues solution by Aaron Dimet

#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;



int main(){
	char foo[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char bar[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
	
	string line;
	getline(cin, line);
	int tests = atoi(line.c_str());
	cerr << "Tests = " << tests << endl;

	for(int cases = 0; cases < tests; cases++){
		string output;
		getline(cin, line);	
		for(int i = 0; i< line.length(); i++){
			char letter = line[i]; 
			int j;
			if(letter != ' '){
				for(j = 0; j <26; j++){
					if(letter == foo[j]){
						break;
						}
					}
				letter = bar[j];
				}
			output += letter;
			}
		cout << "Case #" << cases+1 << ": " << output << endl;
		}

	return 0;
	}
	 	

	
