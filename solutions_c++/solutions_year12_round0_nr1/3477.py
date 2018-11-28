#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(int argc, char ** argv){
    ifstream inFile;
    ofstream outFile;

    int numberOfInput;
    int count, count2;

    string lineBuffer;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    if(!inFile.is_open()){
	return EXIT_FAILURE;
    }

    //char array[]    = { 'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u',   \
	'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r',   \
	    'j', 'g', 't', 'h', 'a', 'q'};
    char array[]    = { 'y', 'h', 'e', 's', 'o',    \
	'c', 'v', 'x', 'd', 'u',    \
	    'i', 'g', 'l', 'b', 'k',	\
	    'r', 'z', 't', 'n', 'w',	\
	    'j', 'p', 'f', 'm', 'a',	\
	    'q' };

    inFile >> numberOfInput;

    getline(inFile, lineBuffer);

    for(count = 0 ; numberOfInput > count ; count++){
	getline(inFile, lineBuffer);

	outFile << "Case #" << count+1 << ": ";

	for(count2 = 0 ; lineBuffer.size() > count2 ; count2++){
	    if(lineBuffer[count2] == ' '){
		outFile << ' ';
	    }else{
		outFile << array[lineBuffer[count2] - 97];
	    }
	}

	outFile << endl;
    }

    outFile.close();
    inFile.close();

    return EXIT_SUCCESS;
}
