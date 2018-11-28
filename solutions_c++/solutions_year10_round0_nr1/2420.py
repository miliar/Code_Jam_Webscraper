//============================================================================


//============================================================================

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>

using namespace std;



int main() {

	ifstream inData;
	ofstream outData;
	
	//char  fileName[256];

	//cin.getline(fileName,256);
	outData.open("outputFile");
	inData.open("inputFile");
//	inData.open(fileName);
	if(!inData){
		cerr << "error input file error"<<endl;
		exit(1);
	}
	int nLines;

	inData >> nLines;


	int count =1;
	while(!inData.eof() && nLines !=0 ){
	
		//int NumOfNodes;
		//int Klick;
		int NumOfNodes;
		long long int Klick;

		inData >> NumOfNodes;
		inData >> Klick;

		long double temp = pow(2.0,NumOfNodes);

		if((Klick+1)%((long int)temp) == 0){
			outData << "Case #"<< count << ": ON"<<endl;
		}else{
			outData << "Case #"<< count << ": OFF"<<endl;
		}
		count++;
		nLines--;
		

	}

	inData.close();
	outData.close();

	system("PAUSE");
	return 0;
}

