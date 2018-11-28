#include <iostream>
#include <fstream>
using namespace std;


int main(){
	int nCase,iCase;
	char combineRule[36][3],elimRule[36][2],list[100],cRead;
	int elimCount[36][2];
	int nCombine,nElim,iCombine,iElim,nRead,iRead,iPos,elimFlag,combineFlag,jPos,test;

	ifstream infile("input.dat");
	ofstream outfile("output.dat");

	infile >> nCase;
	for(iCase = 0; iCase < nCase; iCase++){
		infile >> nCombine;
		for(iCombine =0; iCombine < nCombine; iCombine++){
			infile >> combineRule[iCombine][0] >> combineRule[iCombine][1] >> combineRule[iCombine][2];
		}
		infile >> nElim;
		for(iElim =0; iElim < nElim; iElim++){
			infile >> elimRule[iElim][0] >> elimRule[iElim][1];
			elimCount[iElim][0] = 0;
			elimCount[iElim][1] = 0;
		}

		infile >> nRead;
		iPos = 0;
		for (iRead=0;iRead<nRead;iRead++){
			infile >> cRead;
			combineFlag=0;
			elimFlag = 0;
			if (iCase == 75){
				test = 0;
			}
			if (iPos != 0){
				for(iCombine =0; iCombine < nCombine; iCombine++){
					if (cRead == combineRule[iCombine][0]) {
						if (list[iPos-1] == combineRule[iCombine][1]){
							combineFlag++;
							for(iElim =0; iElim < nElim; iElim++){
								if (list[iPos-1] == elimRule[iElim][0]){
									elimCount[iElim][0]--;
								}
								if (list[iPos-1] == elimRule[iElim][1]){
									elimCount[iElim][1]--;
								}
							}
							list[iPos-1] = combineRule[iCombine][2];
							for(iElim =0; iElim < nElim; iElim++){

								if ( (list[iPos-1] == elimRule[iElim][0]) && list[iPos-2]==(elimRule[iElim][1]) )  elimFlag++;
								if ( (list[iPos-1] == elimRule[iElim][1]) && list[iPos-2]==(elimRule[iElim][0]) )  elimFlag++;
							}
									
						}
					}
					else if (cRead == combineRule[iCombine][1]) {
						if (list[iPos-1] == combineRule[iCombine][0]){
							combineFlag++;
							for(iElim =0; iElim < nElim; iElim++){
								if (list[iPos-1] == elimRule[iElim][0]){
									elimCount[iElim][0]--;
								}
								if (list[iPos-1] == elimRule[iElim][1]){
									elimCount[iElim][1]--;
								}
							}
							list[iPos-1] = combineRule[iCombine][2];
							for(iElim =0; iElim < nElim; iElim++){
								if ( (list[iPos-1] == elimRule[iElim][0]) && list[iPos-2]==(elimRule[iElim][1]) ) elimFlag++;
								if ( (list[iPos-1] == elimRule[iElim][1]) && list[iPos-2]==(elimRule[iElim][0]) ) elimFlag++;
							}
						}
					}
				}
				for(iElim =0; iElim < nElim; iElim++){
					if( list[iPos-1] == elimRule[iElim][0] ) {
						elimCount[iElim][0]++;
						if (elimRule[iElim][0] == elimRule[iElim][1]) elimCount[iElim][1]++;
					}
					if( list[iPos-1] == elimRule[iElim][1] ) {
						elimCount[iElim][1]++;
						if (elimRule[iElim][0] == elimRule[iElim][1]) elimCount[iElim][0]++;
					}
				}
			}
			if (combineFlag == 0){
				for(iElim =0; iElim < nElim; iElim++){
					if (cRead == elimRule[iElim][0]) {
						if (elimCount[iElim][1] > 0) {
							elimFlag++;
						}
						else{
							elimCount[iElim][0]++;
							if (elimRule[iElim][0] == elimRule[iElim][1]) elimCount[iElim][1]++;
						}
					}
					if (cRead == elimRule[iElim][1]) {
						if (elimCount[iElim][0] > 0) {
							elimFlag++;
						}
						else{
							elimCount[iElim][1]++;
							if (elimRule[iElim][0] == elimRule[iElim][1]) elimCount[iElim][0]++;
						}
					}
				}
			}

			if (elimFlag > 0) {
				iPos=0;
				elimFlag = 0;
				for(iElim=0; iElim<nElim;iElim++){
					elimCount[iElim][0] = 0;
					elimCount[iElim][1] = 0;
				}
			}
			else if (combineFlag == 0){
				list[iPos] = cRead;
				iPos++;
			}
		}
		outfile << "Case #" << iCase+1 << ": [";
		for(jPos=0;jPos<iPos;jPos++){
			outfile<< list[jPos];
			if (jPos < iPos - 1){
				outfile << ", ";
			}
		}
		outfile << "]" << endl;
	}
		system("pause");
	return 0;
}