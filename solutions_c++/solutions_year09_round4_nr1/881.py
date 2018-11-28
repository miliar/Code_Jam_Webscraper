#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main (int argc, char * const argv[]) {
    cout << "Input file name: ";
	string filename;
	getline(cin, filename);
	
	cout << "Output file name: ";
	string outFileName;
	getline(cin, outFileName);
	
	ofstream out;
	out.open(outFileName.c_str());
	
	ifstream in;
	in.open(filename.c_str());
	
	if(in.fail()) {
		cout << "File not found" << endl;
		exit(1);
	}
	
	string params;
	getline(in, params);
	stringstream paramsStream;
	paramsStream << params;
	
	int T;
	
	paramsStream >> T;
	
	for(int i = 0; i < T; i++) {
		out << "Case #" << i + 1 << ": ";
		string size;
		getline(in, size);
		stringstream sizeStream;
		sizeStream << size;
		
		int N;
		sizeStream >> N;
		
		vector<int> rows;
		
		for(int j = 0; j < N; j++) {
			string thisRow;
			getline(in, thisRow);
			rows.push_back(thisRow.rfind('1'));
		}
		
		int swaps = 0;
		
		for(int row = 0; row < N; row++) {
			int goodRow = row;
			while(row < rows[goodRow]) {
				goodRow++;
			}
			for(int iRow = goodRow; iRow > row; iRow--) {
				swap(rows[iRow], rows[iRow - 1]);
				swaps++;
			}
		}
		
		
		out << swaps << endl;
	}
	
	cout << "Done!";
	string dummy;
	getline(cin, dummy);
    return 0;
}
