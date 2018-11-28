#include<iostream>
#include<fstream>
#include<sstream>
#include<string>

using namespace std;

int main(){
	int num=0;
	string temp;
	char letter;
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.in");
        outFile.open("output.out");
        if(!inFile){
                cerr << "Unable to DIE";
        }
        inFile >> num;
	getline(inFile,temp);
	for(int i=0; i<num; i++){
		cout << "Getting line" << "\n";
		getline(inFile,temp);
		cout << temp[0] << "\n";
		cout << "Case #" << (i+1) << ": ";
		outFile << "Case #" << (i+1) << ": ";
		for(int j=0; temp[j]!=0; j++){
			letter = temp[j];
			switch (letter){
				case 'a':
					cout << "y";
					outFile << "y";
					break;
				case 'b':
                                        cout << "h";
                                        outFile << "h";
                                        break;
				case 'c':
                                        cout << "e";
                                        outFile << "e";
                                        break;
				case 'd':
                                        cout << "s";
                                        outFile << "s";
                                        break;
				case 'e':
                                        cout << "o";
                                        outFile << "o";
                                        break;
				case 'f':
                                        cout << "c";
                                        outFile << "c";
                                        break;
				case 'g':
                                        cout << "v";
                                        outFile << "v";
                                        break;
				case 'h':
                                        cout << "x";
                                        outFile << "x";
                                        break;
				case 'i':
                                        cout << "d";
                                        outFile << "d";
                                        break;
				case 'j':
                                        cout << "u";
                                        outFile << "u";
                                        break;
				case 'k':
                                        cout << "i";
                                        outFile << "i";
                                        break;
				case 'l':
                                        cout << "g";
                                        outFile << "g";
                                        break;
				case 'm':
                                        cout << "l";
                                        outFile << "l";
                                        break;
				case 'n':
                                        cout << "b";
                                        outFile << "b";
                                        break;
				case 'o':
                                        cout << "k";
                                        outFile << "k";
                                        break;
				case 'p':
                                        cout << "r";
                                        outFile << "r";
                                        break;
				case 'q':
                                        cout << "z";
                                        outFile << "z";
                                        break;
				case 'r':
                                        cout << "t";
                                        outFile << "t";
                                        break;
				case 's':
                                        cout << "n";
                                        outFile << "n";
                                        break;
				case 't':
                                        cout << "w";
                                        outFile << "w";
                                        break;
				case 'u':
                                        cout << "j";
                                        outFile << "j";
                                        break;
				case 'v':
                                        cout << "p";
                                        outFile << "p";
                                        break;
				case 'w':
                                        cout << "f";
                                        outFile << "f";
                                        break;
				case 'x':
                                        cout << "m";
                                        outFile << "m";
                                        break;
				case 'y':
                                        cout << "a";
                                        outFile << "a";
                                        break;
				case 'z':
                                        cout << "q";
                                        outFile << "q";
                                        break;
				case ' ':
                                        cout << " ";
                                        outFile << " ";
                                        break;
			}
		}
		cout << "\n";
		outFile << "\n";
	}

	inFile.close();
	outFile.close();
	return 1;
}
