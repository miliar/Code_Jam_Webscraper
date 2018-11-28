//Joseph Hoang
//mr.joseph.hoang@gmail.com
//google jam 2011 
//problem: FreeCell

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

//Functions
void parseInput(string file);
void printInput();
void go();

//Globals
int num_cases;
vector<int> n;
vector<int> pd;
vector<int> pg;
vector<string> solutions;

int main(int argc, char* argv[]) {

	if ( argc != 2 ) {
		cerr << "Usage: ./free input.file" << endl;
		return 1;
	}
	
	parseInput(argv[1]);
//	printInput();
	go();

	for ( unsigned int i = 0 ; i < solutions.size() ; i++ ) {
		cout << "Case #"<< i + 1 << ": " << solutions[i] << endl;
	}

	return 0;
}

void parseInput(string file) {
	
	string buffer;//buffer2;
	
	ifstream myfile(file.c_str());
	if (myfile.is_open()) {
		
		myfile >> buffer;
		num_cases = atoi(buffer.c_str());
		if ( num_cases == 0 ) {
			cerr << "What? No test cases?" << endl;
			exit(1);
		}
		
		for ( int i = 0 ; i < num_cases ; i++ ) {
			myfile >> buffer;
			n.push_back(atoi(buffer.c_str()));
			myfile >> buffer;
			pd.push_back(atoi(buffer.c_str()));
			myfile >> buffer;
			pg.push_back(atoi(buffer.c_str()));
		}
		myfile.close();
	}
	else {
		cerr << "Problem opening file " << file << "." << endl;
		exit(1);
	}
}

void printInput() {
	
	cout << num_cases << endl;
	for( int i = 0 ; i < num_cases ; i++ ) {
		cout << n[i] << " " << pd[i] << " " << pg[i] << endl;
	}
}

void go() {
	
	for ( int i = 0 ; i < num_cases ; i++ ) {
		
		bool flag = false;
		for ( int j = n[i] ; j > 0 ; j-- ) {
			
			//int tmp = pd[i] % j;
			double tmp = (pd[i]/100.0) * j;
			
			if ( (pg[i] == 100 && pd[i] != 100) || (pg[i] == 0 && pd[i] != 0) ) {
				solutions.push_back("Broken");
				flag = true;
				break;
			}
			if ( floor(tmp) == tmp ) {
				solutions.push_back("Possible");
				flag = true;
				break;
			}
		}
		
		if ( !flag )
			solutions.push_back("Broken");
	}//end case
}
