#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]){

	ifstream inFile;
	ofstream outFile;
	outFile.open("out.txt");
	inFile.open(argv[1]);
	if (inFile.good()){//do everything here
		string table = "yhesocvxduiglbkrztnwjpfmaq";
		string text;
		int cases;
		inFile >> cases;
		inFile.ignore();
		for (int i = 0; i < cases; i++){
			outFile << "Case #" << (i+1) << ": " ;
			getline(inFile, text);
			for (int j = 0; j < text.length(); j++){//decode the ciphertext
				if (text[j]==' '){
					outFile << " ";
				}else{
					outFile << table[((text[j])-97)];
				}
			}
			outFile << endl;
		}

	}else{
		cout << "File could not be opened. " << endl;
	}

	return 0;
}
