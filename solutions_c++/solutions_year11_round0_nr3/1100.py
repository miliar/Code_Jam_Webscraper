#include <iostream>
#include <fstream>
#include <string>
#include <math>
using namespace std;

#define MAX_N 1000
#define MAX_C 1000000

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	if(!fin){
		cout << "Cannot open the file.\n";
		return 1;
	}

	int T;
	fin >> T; 
//	cout << "T:" << T << endl;
	
	
	for(int i=0;i<T;i++){
		long N;
		long C[MAX_N];
		fin >> N;
		for(int j=0;j<N;j++ ) fin >> C[j];
		
		// if be separeted?
		bool cflg;
		long xorC=0;
		for(int j=0;j<N;j++ ) xorC ^= C[j];
		if( xorC==0 ) cflg=true; else cflg=false;

		// split
		long sumC=0;
		long minC=MAX_C+1;
		long ans;
		if(cflg==true){
			for(int j=0;j<N;j++ ){
				sumC += C[j];
				if(C[j] < minC) minC = C[j];
			}
			ans = sumC-minC;
		}

		if(cflg==true)	fout << "Case #" << i+1 << ": " << ans << endl;
		else			fout << "Case #" << i+1 << ": NO" << endl;

	}

	fin.close();
	fout.close();
}



