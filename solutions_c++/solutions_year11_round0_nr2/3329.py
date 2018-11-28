#include <cstdlib>
#include <math.h>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
	int i, j, k, c, d, n, ncase;
	ifstream inputfile("data.in");
	ofstream outputfile("data.out");
	int casesCount;
	int nC, nD, N;
	inputfile >> casesCount;
	for(ncase = 0; ncase < casesCount; ncase++) {
		char C[200][4], D[200][3];
		char list[200];
		int nlist = 0;
		inputfile >> nC;
		for(c=0;c<nC;c++)
			inputfile >> C[c];
		inputfile >> nD;
		for(d=0;d<nD;d++)
			inputfile >> D[d];
		inputfile >> N;
		for(n=0;n<N;n++){
			char chr;
			inputfile >> chr;
			bool add = true;
			if(nlist>0)
			for(i=0;i<nC;i++){
				if(((list[nlist - 1] == C[i][0]) && 
					(chr == C[i][1]))||
					((list[nlist - 1] == C[i][1]) && 
					(chr == C[i][0]))){
						list[nlist - 1] = C[i][2];
						chr = C[i][2];
						add = false;
				}
			}
			if(nlist>0)
			for(i=0;i<nD;i++){
				for(j=0;j<nlist;j++){
					if(((list[j] == D[i][0]) && 
						(chr == D[i][1]))||
						((list[j] == D[i][1]) && 
						(chr == D[i][0]))){
						nlist = 0;
						add = false;
					}
				}
			}
			if(add)
				list[nlist++] = chr;
		}
		outputfile << "Case #" << ncase+1 << ": [";
		if(nlist>0) outputfile << list[0];
		for(j=1;j<nlist;j++){
			outputfile << ", " << list[j];
		}
		outputfile << "]" << endl;
	}
	inputfile.close();
	outputfile.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}