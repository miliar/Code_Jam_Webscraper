#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>

using namespace std;

int main (int argc, char * const argv[]) {
	
	ifstream input(argv[1], ifstream::in);
	
	int testsNb;
	input >> testsNb;
	
	ofstream outfile(argv[2]);
	
	cout << "Testing " << testsNb << " cases..." << endl;
	
	int cases = 0;
	while (cases < testsNb) {
		int rows, cols;
		input >> rows;
		input >> cols;
		int local_count = 0;
		char ** pic = NULL;
		pic = new char *[rows];
		for (int i = 0; i < rows; i++)
			pic[i] = new char[cols]; 
		while (local_count < rows) {
			string current;
			input >> current;
			for (int i = 0; i < cols; i++) {
				char tmp = (current.c_str()[i]);
				pic[local_count][i] = tmp;
			}
			
			local_count++;
		}
		cases++;
		
		//Compute
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {
				cout << pic[i][j];
			}
			cout << endl;
		}
		
		
		bool impossible = false;
		for (int i = 0; i < rows && !impossible; i++) {
			for (int j = 0; j < cols && !impossible; j++) {
				if (pic[i][j] == '#') {
					//Check size
					if (j < cols - 1 && i < rows - 1 && pic[i][j+1] == '#' && pic[i+1][j] == '#' && pic[i][j+1] == '#') {
						pic[i][j] = '/';
						pic[i+1][j+1] = '/';
						pic[i][j+1] = '\\';
						pic[i+1][j]= '\\';
					}
					else {
						impossible = true;
						break;
					}

				}
			}
		}
		outfile << "Case #" << cases << ":" << endl;
		if (impossible)
			outfile << "Impossible" << endl;
		else {
			for (int i = 0; i < rows; i++) {
				for (int j = 0; j < cols; j++)
					outfile << pic[i][j];
				outfile << endl;
			}
		}

		
	}
		
	input.close();
	outfile.close();
    return 0;
	
}