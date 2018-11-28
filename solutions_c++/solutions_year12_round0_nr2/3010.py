#include <iostream>
#include <fstream>

using namespace std;


void Readata(){

	ifstream fin("Input.txt");
	int T;
	fin >> T;
	int i;
	for ( i = 0 ; i < T ; i++ ) {
		int N;
		fin >> N;
		int S;
		fin >> S;
		int P;
		fin >> P;
		int j ;
		int Count1=0;
		int Count2=0;

		//cout << " Start " << endl;
		for ( j = 0 ; j < N ; j++ ){
			int A; 
			fin >> A;
			int	M1=-1;
			int	M2=-1;
			int C = 0;
			if ( A == 0 ) { if ( P <= 0 ) Count2++; } 
			if ( A == 1 ) { if ( P <= 1 ) Count2++; }
			if ( A == 30 ) { Count2++; }
			if ( A == 29 ) { Count2++;}
			if ( ( A > 1 ) && (A < 29) ){
			
				int x = A % 3 ;
				if ( x == 0 ) {
					M1=A/3;
					M2=M1+1;
				} 
				if ( x == 1 ) {
				
					M1=(A/3)+1;
					M2=M1;
				}

				if ( x == 2 ) {

					M1=(A/3)+1;
					M2=M1+1;
				}

			if ( M2 >= P ) C++;
			if ( M1 >= P ) C++;

			//cout << A << " " << M1 << " " << M2 << endl;

			if ( C == 2 ) Count2++;
			if ( C == 1 ) Count1++;
		}

		}

		if ( S < Count1 ) Count1=S;
		Count1+=Count2;
		cout << "Case #" << i+1 << ": " << Count1 << endl; 
		
	}
}

int main()
{	
	Readata();
	return 0;
}
