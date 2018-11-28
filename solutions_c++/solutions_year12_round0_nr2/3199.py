#include <iostream>
#include <string>
#include <fstream>
//#include <sstream>

using namespace std;

int main()
{
	ofstream fout("A.out");
	ifstream fin("A.in");

	int T, cc = 1;

	fin >> T;

	while(T--){
		int N, S, P;		
		int count = 0;

		fin >> N >> S >> P;
		for(int i = 0; i < N; i++){
			int Tj, div, mod;

			fin >> Tj;
			div = Tj / 3;
			mod = Tj % 3;

			if( div >= P ){ count++; continue; }

			if( div == 0 ){
				if( P == 1 ){
					switch( mod ){
					case 0 : continue;
					case 1 : S--;
					case 2 : count++; continue;
					}
				}
				if( P == 2 ){
					switch( mod ){
					case 0 : 
					case 1 : continue;
					case 2 : S--; count++; continue;
					}
				}
			}

			if( div == P-1 ){
				switch( mod ){
				case 0 : S--;
				case 1 : 
				case 2 : count++; continue;
				}
			}

			if( div == P-2 ){
				switch( mod ){
				case 0 : 
				case 1 : continue;
				case 2 : S--; count++; continue;
				}
			}
		}
		if( S < 0 )	count += S;
		fout << "Case #" << cc++ << ": " << count << endl;
	}

	return 0;
}








/*
count++; continue; 

if(S){
if( div >= P ){ count++; continue; }
else if( div == P-1 ){ count++; continue; }
else if( div == P-2 ){ S--; count++; continue; }
}
else{
}
*/