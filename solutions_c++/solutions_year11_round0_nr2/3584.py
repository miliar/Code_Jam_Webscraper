//Joseph Hoang
//mr.joseph.hoang@gmail.com
//google jam 2011 
//problem: Magicka

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
using namespace std;

//Functions
void parseInput(string file);
void printInput();
void go();

//Globals
int num_cases;
vector<int> num_combines;
vector<map<string,string> > combines;
vector<int> num_opposed;
vector<set<string> > opposed;
vector<int> input_length;
vector<string> inputs;
vector<string> solutions;

int main(int argc, char* argv[]) {

	if ( argc != 2 ) {
		cerr << "Usage: magic input.file" << endl;
		return 1;
	}
	
	parseInput(argv[1]);
//	printInput();
	go();

	for ( unsigned int i = 0 ; i < solutions.size() ; i++ ) {
		cout << "Case #"<< i + 1 << ": [";
		for ( unsigned int j = 0 ; j < solutions[i].length() ; j++ ) {
			cout << solutions[i][j];
			if ( j != solutions[i].length() - 1 )
			 	cout << ", ";
		}
		cout << "]";
		//if ( i != solutions.size() - 1)
			cout << endl;
	}

	return 0;
}

void parseInput(string file) {
	
	/*
	Example input:
	
	Input 

	5
	0 0 2 EA
	1 QRI 0 4 RRQR
	1 QFT 1 QF 7 FAQFDFQ
	1 EEZ 1 QE 7 QEEEERA
	0 1 QW 2 QW
	
	First line # of test cases
	First number on each line after = number of combination sets
	Each set of 3 characters after that number represent the 2 elements
	 	that combine into the 3rd (ex. QR/RQ turns into I)
	Second number is number of pair of characters that represent opposing
		elements (if they are both present, destroy all elements in list)
	Third number is length of input string (read in left to right one by one)
	*/
	
	string buffer,tmp, tmp2;
	
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
			num_combines.push_back(atoi(buffer.c_str()));
			combines.push_back(map<string,string>());
			//makes a map of all combinations with
			//key = element1/element2 , value = element3
			for ( int j = 0 ; j < num_combines[i] ; j++ ) {
				buffer = "";
				myfile >> buffer;

				tmp = buffer.substr(0,2);
				tmp2 = buffer.substr(2,1);
				//cout << i << " " << tmp << " " << tmp2 << endl;
				//cout << "case " << i << ": " << tmp << " " << tmp2;
				combines[i].insert(pair<string,string>(tmp,tmp2));
				tmp = buffer.substr(1,1) + buffer.substr(0,1);
				//cout << "case " << i << ": " << tmp << " " << tmp2;
				combines[i].insert(pair<string,string>(tmp,tmp2));
			}
			
			myfile >> buffer;
			num_opposed.push_back(atoi(buffer.c_str()));
			opposed.push_back(set<string>());
			//makes a set of all opposing pairs
			for ( int j = 0 ; j < num_opposed[i] ; j++ ) {
				myfile >> buffer;
				tmp = buffer.substr(0,2);
				tmp2 = buffer.substr(1,1) + buffer.substr(0,1);
				opposed[i].insert(tmp);
				opposed[i].insert(tmp2);
			}
			
			myfile >> buffer;
			input_length.push_back(atoi(buffer.c_str()));
			
			myfile >> buffer;
			inputs.push_back(buffer);
		}
		myfile.close();
	}
	else {
		cerr << "Problem opening file " << file << "." << endl;
		exit(1);
	}
}

void printInput() {
	
	for ( int i = 0 ; i < num_cases ; i++ ) {
		cout << num_combines[i] << " ";
		for ( int j = 0 ; j < num_combines[i] ; j++ ) {
			//cout << combines[i][j] << " ";
		}
		cout << num_opposed[i] << " ";
		for ( int j = 0 ; j < num_opposed[i] ; j++ ) {
			//cout << opposed[i][j] << " ";
		}
		cout << input_length[i] << " ";
		cout << inputs[i] << endl;
	}
}

void go() {
	
	string list,input, tmp, tmp2; 
	bool flag = false;
	
	for ( int i = 0 ; i < num_cases ; i++ ) {
		
		list = "";
		input = inputs[i];
		char t;
		for ( int j = 0 ; j < input.length() ; j++ ) {
			
			if ( list.length() == 0 ) {
				list = input.substr(j,1);
				continue;
			}

			list += input.substr(j,1);
			//check combinations (last 2 characters only)
			tmp = list.substr(list.length() - 1,1) + list.substr(list.length() - 2,1);
			//cout << tmp << endl;
			if ( combines[i].find(tmp) != combines[i].end() ) {
				//match is found. combination exists
				list = list.substr(0, list.length() - 2) + combines[i][tmp];
				//cout << "combi found " << i << " " << j << " " << list << " " << tmp << " " << combines[i][tmp] << endl;
				continue;
			}
			
			//check oppositions (check against all characters)
			for ( unsigned int k = 0 ; k < list.length() ; k++ ) {
				
				tmp = list.substr(list.length() - 1,1) + list.substr(k,1);
				if ( opposed[i].find(tmp) != opposed[i].end() ) {
					//opposing pair found
					//cout << "oppose found " << i << " " << j << " " << list << " " << tmp << endl;
					list = "";
					break;
				}
			}
		}
		/*for ( map<string,string>::iterator it = combines[i].begin() ; it != combines[i].end() ; it++ ) {
			cout << i << " " << it->first << " " << it->second << endl;
		}
		for ( set<string>::iterator it = opposed[i].begin() ; it != opposed[i].end() ; it++ ) {
			cout << i << " " << *it << endl;
		}*/
		
		solutions.push_back(list);
		//cout << list << endl;
	}
}
