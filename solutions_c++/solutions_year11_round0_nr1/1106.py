#include <iostream>
#include <fstream>
#include <string>
#include <math>
using namespace std;

#define MAX_N 100

void QSort(long x[ ], int left, int right);

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	if(!fin){
		cout << "Cannot open the file.\n";
		return 1;
	}

	int T;
	fin >> T; 
//	cout << "T:" << T << endl;
	
	
	for(int i=0;i<T;i++){
		long N;
		fin >> N;
//		cout << "N:" << N << endl;

		long O[MAX_N]; // O's botton positions
		long B[MAX_N]; // B's botton postions
		long numO = 0; // # O's botton
		long numB = 0; // # B's botton
		long Pn[MAX_N];	// botton positions
		long Pk[MAX_N]; // robot colors. 0:o, 1:B

		// input data
		for( int j=0;j<N;j++ ){
			char rc;
			fin >> rc;
			fin >> Pn[j];
			if( rc=='O' ) {
				Pk[j] = 0;
				O[numO++] = Pn[j];
			}else{
				Pk[j] = 1;
				B[numB++] = Pn[j];
			}
		}
		
		long posO=1; // O's position
		long posB=1; // B's position
		long idxO=0; // O[] idx
		long idxB=0; // B[] idx
		long idxP=0; // Pk[],Pk[] idx
		long time=0;
	
		while( idxP<N ){
			if(Pk[idxP]==0){
				long pt;	// proccing time
				pt = abs(posO - Pn[idxP++]) + 1;
				posO = O[idxO++];
				posB = (pt>abs(posB-B[idxB]))?B[idxB]:((posB<B[idxB])?posB+pt:posB-pt);
				time += pt;
			}else{
				long pt;	// proccing time
				pt = abs(posB - Pn[idxP++]) + 1;
				posB = B[idxB++];
				posO = (pt>abs(posO-O[idxO]))?O[idxO]:((posO<O[idxO])?posO+pt:posO-pt);
				time += pt;
			}
//			cout << "O:" << posO << ", " << "B:" << posB << ", " << "Time:" << time << endl;
		}

//		cout << time << endl;
		fout << "Case #" << i+1 << ": " << time << endl;
	}

	fin.close();
	fout.close();
}



