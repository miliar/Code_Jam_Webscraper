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
	cout << T << endl;
	
	
	for(int i=0;i<T;i++){
		long N, K;
		fin >> N >> K;

		long ALLON;
		ALLON = (long)pow(2,N);

		if((K+1) % ALLON != 0){
			fout << "Case #" <<i+1 << ": OFF"  << endl;
		}else{
			fout << "Case #" <<i+1 << ": ON"  << endl;
		}
	}

	fin.close();
	fout.close();
}



