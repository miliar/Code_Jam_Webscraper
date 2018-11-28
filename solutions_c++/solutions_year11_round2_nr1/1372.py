#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <vector>
#include <stdlib.h>
#include <cmath>

using namespace std;
 
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

int main(){
	//get inputs

	int ncase = 0;
	cin >> ncase;


	for(int icase = 0; icase<ncase; icase++){

		int n;
		cin >> n; 
		char re[n][n];

		for(int i = 0; i< n; i++){
			for(int j = 0; j<n; j++){
				cin >> re[i][j];
			}
		}

		double wp[n];
		double owp[n];
		double oowp[n];

		int i, j;
		int matsum[n];

		for(int i = 0; i<n; i++){
			int winsum = 0;
			matsum[i] = 0;
			for(int j = 0; j<n;j++){
				if(re[i][j] == '1'){
					winsum++;
				}
				if(re[i][j] != '.'){
					matsum[i]++;
				}
			}
			wp[i] = (double) winsum / matsum[i];
		}

		for(int i = 0; i<n; i++){
			double opsum = 0;
			int opcount = 0;
			REP(j, n){
				if(re[i][j] != '.'){
					opcount++;
					double newwp;
					if(re[i][j] == '1'){
						newwp = (wp[j]*matsum[j])/(matsum[j]-1);
					}
					else{
						newwp = (wp[j]*matsum[j]-1)/(matsum[j]-1);
					}
					opsum += newwp;
				}
			}
			owp[i] = opsum /opcount;
		}


		for(int i = 0; i<n; i++){
			double oopsum = 0;
			int opcount = 0;
			REP(j, n){
				if(re[i][j] != '.'){
					opcount++;
					oopsum += owp[j];
				}
			}
			oowp[i] = oopsum / opcount;
		}


		cout << "Case #" << icase+1 << ": " << endl; 
		REP(i,n) cout << (0.25*wp[i] + 0.5*owp[i] + 0.25 * oowp[i]) << endl;	
	}


	return 0;
}
