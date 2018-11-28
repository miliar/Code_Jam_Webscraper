#include <iostream>
#include <ctype.h>

using namespace std;

char lgooglerese[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
//char translate[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

int main(){
	int num, cont = 0;
	int band = 0;
	char letter;
	int letra;
	cin >> num;
	char garbage;
	cin.get(garbage);
	while ( cont < num && cin.get(letter) ){
		if ( band == 0 ){
			cout << "Case #" << cont + 1 << ": ";
			band = 1;
		}
		if( letter > 96 && letter < 123 ){
			cout << lgooglerese[(int)letter - 97];
		}else{
			if( letter == ' ' ){
				cout << " ";
			}else{
				if( cont + 1 != 30 )
					cout << letter;	
				cont++;
				band = 0;
			}
		}
	}
	return 0;
}
