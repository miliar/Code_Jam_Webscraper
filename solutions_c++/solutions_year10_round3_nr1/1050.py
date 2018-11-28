#include <iostream>
#include <fstream>
#include <string>
#include <math>
using namespace std;

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

	for(int i=0;i<T;i++){
		int N;
		fin >> N;
//		cout << "N: " << N << endl;
	
		double A[1000], B[1000];
		for(int j=0;j<N;j++){
			fin >> A[j] >> B[j];
//			cout << "A: " << A[j] << ", B: " << B[j] << endl;
		}

		long y;
		y = 0;

		for(int j=0; j<N; j++)
			for(int k=j+1; k<N; k++)
				if( (A[j]-A[k])*(B[j]-B[k])<0 ) y++;

		fout << "Case #" <<i+1 << ": "  << y << endl;
//		cout << "Case #" <<i+1 << ": "  << y << endl;
	}

	fin.close();
	fout.close();
}



