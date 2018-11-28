
#include <iostream>

using namespace std;

char googlese[] = 
{'y', 'h', 'e', 's', 'o',
 'c', 'v', 'x', 'd', 'u',
 'i', 'g', 'l', 'b', 'k',
 'r', 'z', 't', 'n', 'w',
 'j', 'p', 'f', 'm', 'a',
 'q'};


int main (){
	 
	 
	//cerr << "Hello Google" << endl;
	
	int T;
	char s[200];
	// read no test cases
	cin >> T;	
	cin.getline(s, 200);
	for (int i=1; i<= T ; i++){
		//read s;
		cin.getline(s, 200);
		
		for (int k = 0; k<200; k++){
			int x = s[k] - 'a';
			if ( x >= 0 && x <= 25){
				s[k] = googlese[x];
			}
		}
		cout << "Case #" << i << ": " << s << endl;

	}//case T 
	

	return 0;
}
