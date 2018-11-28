#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	ifstream filein("data.in");
	ofstream fileout("data.out");
	int T,i,j,k,length;
	char G[120],g;
	char tran[27]="yhesocvxduiglbkrztnwjpfmaq";

	filein >> T;
	filein.ignore();
	filein.ignore();
	for (i=1; i<=T; i++) {

		fileout << "Case #" << i << ": ";


		filein.getline(G,101);
		
		length=strlen(G);
		for (j=0;j<length;j++){
			g = G[j];
			if (g==' ') {
				fileout << ' ';
			} else {
				fileout << tran[g-'a'];
			}
		}

		if (i<T) fileout << endl;
	}



	return 0;
}