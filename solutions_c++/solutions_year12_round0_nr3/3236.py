#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
	ofstream fout("A.out");
	ifstream fin("A.in");

	int T, cc = 1;
	
	fin >> T;

	while(T--){				
		int A, B;
		fin >> A >> B;
		
		int count = 0;
		int carry = 0;
		
		if( A < 12) A = 12;

		int var = A;
		while( var /= 10 ) carry++;
		
		for(int i = A; i <= B; i++){


			var = i;
			for(int j = 0; j < carry; j++){
				int temp = var % 10;
				var /= 10;
				var += temp * pow(10.0, carry);
				/*
				if( var == i ) continue;
				if( A <= var && var <= B ) count++;
				*/
				if( i < var && var <= B) count++;
			}
		}
		
		//count /= 2;
		
		
			
		fout << "Case #" << cc++ << ": " << count << endl;
	}
		/*
	while(T--){		
		stringstream sstr;
		string iStr, BStr;
		int A, B;
		fin >> A >> B;
		sstr << B;
		BStr = sstr.str();
		
	
		int count = 0;
		if( A < 12) A = 12;

		
			count++;
			
		fout << "Case #" << cc++ << ": " << count << endl;
	}
	*/
	return 0;
}