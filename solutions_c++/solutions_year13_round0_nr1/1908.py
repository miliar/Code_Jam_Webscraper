#include<iostream>
#include<map>
#include<fstream>
#include<string>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;
	
	string inputString,col0String,col1String,col2String,col3String,diag1String,diag2String;
	char inputCharArray[4][4];
	bool gameRemaining=false;
	bool moveOn = false;
	
	int intTestCases=0,leng=0;
	outputFile.open(argv[2]);
	
	//Build a Map
	map<string,char> myMap;
	myMap["XXXX"]='X';
	myMap["XXXT"]='X';
	myMap["XXTX"]='X';
	myMap["XTXX"]='X';
	myMap["TXXX"]='X';
	myMap["OOOO"]='O';
	myMap["OOOT"]='O';
	myMap["OOTO"]='O';
	myMap["OTOO"]='O';
	myMap["TOOO"]='O';
	
	file.open(argv[1]);

	//Read integers..
	if(!file.eof())
	{
		file >> intTestCases;
		getline(file, inputString);
	
		for(int i=0; i<intTestCases; ++i){
			for (int j=0; j<4; ++j) {
				getline(file, inputString);
				
				if (moveOn) {
					continue;
				}
				
				if (inputString != "" && myMap[inputString]) {
					moveOn=true;
					if (i!=0) {
						outputFile << "\nCase #" << i+1 << ": " << myMap[inputString] << " won";
					}
					else {
						outputFile << "Case #" << i+1 << ": " << myMap[inputString] << " won";
					}

					
				}
				
				col0String += inputString[0];
				col1String += inputString[1];
				col2String += inputString[2];
				col3String += inputString[3];
				diag1String += inputString[j];
				diag2String = inputString[3-j] + diag2String;
				
				for (int k=0; k<4; ++k) {
					if (inputString[k] == '.') {
						gameRemaining = true;
						break;
					}
				}
				
				
			}
			
			if(!moveOn){
				if (myMap[col0String]) {
					if (i!=0) {
						outputFile << "\nCase #" << i+1 << ": " << myMap[col0String] << " won";
					}else{
						outputFile << "Case #" << i+1 << ": " << myMap[col0String] << " won";
					}
					goto label;
				}

				if (myMap[col1String]) {
					if (i!=0) {
						outputFile << "\nCase #" << i+1 << ": " << myMap[col1String] << " won";
					}else {
						outputFile << "Case #" << i+1 << ": " << myMap[col1String] << " won";
					}

					
					goto label;
				}

				if (myMap[col2String]) {
					if (i!=0) {
						outputFile << "\nCase #" << i+1 << ": " << myMap[col2String] << " won";
					}else {
						outputFile << "Case #" << i+1 << ": " << myMap[col2String] << " won";
					}

					goto label;
				}

				if (myMap[col3String]) {
					if (i!=0) {
						outputFile << "\nCase #" << i+1 << ": " << myMap[col3String] << " won";
					}else {
						outputFile << "Case #" << i+1 << ": " << myMap[col3String] << " won";
					}

					goto label;
				}
				
				if (myMap[diag1String]) {
					if (i!=0) {
						outputFile << "\nCase #" << i+1 << ": " << myMap[diag1String] << " won";
					}else {
						outputFile << "Case #" << i+1 << ": " << myMap[diag1String] << " won";
					}

					goto label;
				}

				if (myMap[diag2String]) {
					if (i!=0) {
						outputFile << "\nCase #" << i+1 << ": " << myMap[diag2String] << " won";
					}else {
						outputFile << "Case #" << i+1 << ": " << myMap[diag2String] << " won";
					}
					goto label;
				}			
				
				if (gameRemaining) {
					if (i!=0) {					
						outputFile << "\nCase #" << i+1 << ": " << "Game has not completed";
					}else{
						outputFile << "Case #" << i+1 << ": " << "Game has not completed";
					}
				}else {
					if (i!=0) {
						outputFile << "\nCase #" << i+1 << ": " << "Draw";
					}else {
						outputFile << "Case #" << i+1 << ": " << "Draw";
					}

				}
			}

		label:	
			//outputFile << "Case #" << i+1 << ": ";
		
			//for (int i=0; i<leng; ++i) {
			//	outputFile << myMap[inputString[i]];
			//}
			
			//outputFile << endl;
		
			inputString="";
			col0String="";
			col1String="";
			col2String="";
			col3String="";
			diag1String="";
			diag2String="";
			
			gameRemaining = false;
			moveOn=false;
			if(!file.eof()){
				getline(file, inputString);
			}
			
		}
	
	
	}
	

	outputFile.close();
	file.close();
	
	return 0;

}

