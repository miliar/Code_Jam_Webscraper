#include <iomanip.h>
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <math>
using namespace std;

#define MAX_N 101

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
	char sch[MAX_N][MAX_N];

	
	for(int i=0;i<T;i++){
		
		int N;
		fin >> N;
		for(int j=0;j<N;j++){
			for(int k=0;k<N;k++){
				fin >> sch[j][k];
			}
		}
		float WP[MAX_N];
		float OWP[MAX_N];
		float OOWP[MAX_N];
		float RPI[MAX_N];
		int NG[MAX_N]; // the number of games
		int WG[MAX_N]; // the number of won games


		

		for(int j=0;j<N;j++){
			int ng=0;
			int wg=0;
			for(int k=0;k<N;k++){
				if(sch[j][k]=='1'){
					wg++;
					ng++;
				}else if(sch[j][k]=='0'){
					ng++;
				}
			}
			NG[j] = ng;
			WG[j] = wg;
			WP[j] = (float)wg/ng;
		}

		for(int j=0;j<N;j++){
			float swp=0.0;
			for(int k=0;k<N;k++){
				if(sch[j][k]=='1'){
					swp += (float)WG[k]/(NG[k]-1);
				}else if(sch[j][k]=='0'){
					swp += (float)(WG[k]-1)/(NG[k]-1);
				}
			}
			OWP[j] = swp/NG[j];
		}

		for(int j=0;j<N;j++){
			float sowp=0.0;
			for(int k=0;k<N;k++){
				if(sch[j][k]=='0' || sch[j][k]=='1'){
					sowp += OWP[k];
				}
			}
			OOWP[j] = sowp/NG[j];
		}

		for(int j=0;j<N;j++){
			//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
			RPI[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
		}

		fout << "Case #" << i+1 << ": " << endl;
		for(int j=0;j<N;j++){
//			cout << NG[j] << "," << WG[j] << ": " << WP[j] << "," << OWP[j] << "," << OOWP[j] <<  endl;
			fout << RPI[j] <<  endl;
		}
	}


	fin.close();
	fout.close();
}
