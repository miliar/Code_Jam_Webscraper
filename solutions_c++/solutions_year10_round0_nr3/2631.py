#include <iostream>
#include <fstream>
#include <string>
#include <math>
using namespace std;

void QSort(long x[ ], int left, int right);

int main()
{
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");

	if(!fin){
		cout << "Cannot open the file.\n";
		return 1;
	}

	int T;
	fin >> T; 
	cout << T << endl;
	
	
	for(int i=0;i<T;i++){
		long R, k, N;
		fin >> R >> k >> N;

		long g[1000];
		for(int j=0;j<N;j++){
			fin >> g[j];
		}

		long bg;
		bg = 0;		
		long P[1000];
		int FG[1000];
		int NFG;
		NFG = 0;
		int TER[1000];
		for(int j=0;j<1000;j++) TER[j] = 0;	

		long NB;
		NB = 0;
		long MNY;
		MNY = 0;
		long RP;

		while(1){

			if(NB == R){ //finished
				break;
			}

			for(int j=0;j<NFG;j++){ //repeat point
				if(FG[j] == bg){
					RP = j;
					break;
				}
			}

			NB++;
			FG[NFG]=bg;
			NFG++;
			long REM;
			REM = k;
			long TEuro;
			TEuro = 0;
			long rn;
			rn = 0;

			while(1){
				if(REM < g[bg]) break;
				if(rn >= N) break;
				TEuro += g[bg];
				MNY += g[bg];
				REM -= g[bg];
				bg++;
				bg = bg%N;
				rn++;
			}
			
			for(int j=0;j<NFG;j++){
				TER[j] += TEuro;
				P[j] += 1;
			}
			
		}

		if(NFG>0 && NB<R){
			MNY +=  ((R-NB)/P[RP])*TER[RP];
			NB += ((R-NB)/P[RP])*P[RP];
		}

		//cout << "PREOK" << endl;
		//cout << "MNY:NB:bg " << MNY << ", " << NB << ", " << bg << endl; 

		while(NB<R){
			NB++;
			long REM;
			REM = k;
			long rn;
			rn = 0;
			while(1){
				if(REM < g[bg]) break;
				if(rn >= N) break;
				MNY += g[bg];
				REM -= g[bg];
				bg = (++bg)%N;
				rn++;
			}
		}

		fout << "Case #" <<i+1 << ": "  << MNY << endl;
	}

	fin.close();
	fout.close();
}



