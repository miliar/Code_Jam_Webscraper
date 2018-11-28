#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
	char buffer[256];
	int x;
	
	if (argc != 2){
		cout << "No input file (usage: blah.exe <input file>)" << endl;
		return 1;
	}

	ifstream input(argv[1]);
	ofstream output("output.txt");
	
	if (input.fail() || output.fail()){
		cout << "Error: Files couldn't be opened" << endl;
		system("PAUSE");
		return 1;
	}
	
	input.getline(buffer, 255);
	int numLines = atoi(buffer);
	
	for (int iLine = 0; iLine < numLines; iLine++){
		input.getline(buffer, 255);
		unsigned int n, k;
		for (int i = 0; i < 255; i++){
			if (buffer[i] == ' '){
				buffer[i] = '\0';
				i++;
				while (buffer[i] == ' '){
					i++;
				}
				n = atoi(buffer);
				k = atoi(&buffer[i]);
				break;
			}
		}
		
		output << "Case #" << iLine+1 << ": ";
		int desiredSwitchMask = ((1 << (n))-1);
		if ((desiredSwitchMask & k) == desiredSwitchMask){
			output << "ON" << endl;
		} else {
			output << "OFF" << endl;
		}
	}
	
    return EXIT_SUCCESS;
}
