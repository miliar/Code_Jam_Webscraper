#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;



int GCD(int a, int b)
{
    while( 1 )
    {
      a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

     if( b == 0 )
		return a;
    }
}

int LCM(int a, int b) {
	//cout << "LCM of " << a << " And " << b << " is ";
	//cout << (a/(GCD(a,b)))*b << endl;
	if(a == 0) return 0;
	if(b == 0) return 0;
	return (a/(GCD(a,b)))*b;

}

int main() {
	
	int T,N,L,H;
	int notes[10100];
	int list[10100];
	cin >> T;
	
	for(int c = 1; c <= T; c++) {
	
		cin >> N >> L >> H;
		
		for(int i = 0; i < N; i++) {
			cin >> notes[i];
		}
		
		bool found;
		for(int i = L; i <= H; i++) {
			found = 1;
			
			//cout << i << ") ";
			for(int j = 0; j < N; j++) {
				//cout << i%notes[j] << "," << notes[j] % i << " ";
				if(i%notes[j] != 0 && notes[j] % i != 0)
					found = 0;
			}
			//cout << endl;
			if(found) {
				cout << "Case #" << c << ": " << i << endl;
				break;
			}
		}
		if(!found)
			cout << "Case #" << c << ": NO" << endl;
	


	}

return 0;
}
