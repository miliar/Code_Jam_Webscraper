//Joseph Hoang
//mr.joseph.hoang@gmail.com
//google jam 2011 
//problem: Bot Trust

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

enum { ORANGE,BLUE };

//Functions
void parseInput(string file);
void printInput();
void go();
int nextOrangeMove(int i, int x);
int nextBlueMove(int i, int x);

//Globals
int num_cases;
vector<int> num_instructions;
vector<vector<int> > orange;
vector<vector<int> > blue;
vector<vector<int> > whoseTurn;
vector<int> solutions;

int main(int argc, char* argv[]) {

	if ( argc != 2 ) {
		cerr << "Usage: bot input.file" << endl;
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
	
	/*
	Example input:
	
	3
	4 O 2 B 1 B 2 O 4
	3 O 5 O 8 B 100
	2 B 2 B 1
	
	First line # of test cases
	First number on each line after = number of instructions
	O means orange robot/B means blue robot
	Number after O/B is button to push
	*/
	
	string buffer, buffer2;
	
	ifstream myfile(file.c_str());
	if (myfile.is_open()) {
		
		myfile >> buffer;
		num_cases = atoi(buffer.c_str());
		if ( num_cases == 0 ) {
			cerr << "What? No test cases?" << endl;
			exit(1);
		}
		
		//orange.resize(num_cases, vector<int>() );
		//blue.resize(num_cases, vector<int>() );
		for ( int i = 0 ; i < num_cases ; i++ ) {
		
			orange.push_back(vector<int>());
			blue.push_back(vector<int>());
			whoseTurn.push_back(vector<int>());
			myfile >> buffer;
			num_instructions.push_back(atoi(buffer.c_str()));
			
			for ( int j = 0 ; j < num_instructions[i] ; j++ ) {
				myfile >> buffer;
				if (buffer == "O") {
					myfile >> buffer;
					orange[i].push_back(atoi(buffer.c_str()));
					blue[i].push_back(-1);
					whoseTurn[i].push_back(ORANGE);
				}
				else if (buffer == "B") {
					myfile >> buffer;
					blue[i].push_back(atoi(buffer.c_str()));
					orange[i].push_back(-1);
					whoseTurn[i].push_back(BLUE);
				}
				else {
					cerr << "What? Another robot?" << endl;
					exit(1);
				}	
			}
			
		}
		myfile.close();
	}
	else {
		cerr << "Problem opening file " << file << "." << endl;
		exit(1);
	}
}

void printInput() {
	
	for( int i = 0 ; i < num_cases ; i++ ) {
		cout << num_instructions[i] << " ";
		for ( int j = 0 ; j < num_instructions[i] ; j++) {
			if ( orange[i][j] != -1 )
				cout << whoseTurn[i][j] << " " << orange[i][j] << " ";
			else if ( blue[i][j] != -1 )
				cout << whoseTurn[i][j] << " " << blue[i][j] << " ";
		}
		cout << endl;
	}
}

void go() {
	
	int t, oPos, bPos, turn, temp, temp2;
	
	for ( int i = 0 ; i < num_cases ; i++ ) {
		
		//Initialize variables for every test case
		t = 0;
		oPos = 1;
		bPos = 1;
		
		for ( int j = 0 ; j < num_instructions[i] ; j++ ) {
			
			turn = whoseTurn[i][j];
			
			if ( turn == ORANGE ) {
				//if not in position, move and press
				if ( oPos != orange[i][j] ) {
					temp = abs( oPos - orange[i][j] ) + 1; //amount of time orange used
					t += temp;
					oPos = orange[i][j];
				}
				//robot already in position
				else {
					temp = 1;
					t++;
				}
				temp2 = nextBlueMove(i,j);
				//if blue's next move exists start moving to next location
				if ( temp2 != -1 ) {
					if ( bPos != temp2 && bPos < temp2 ) { //add
						//if extra time exceeds destination, simply set new position
						if ( bPos + temp >= temp2 ) 
							bPos = temp2;
						//otherwise add orange's time to blue
						else 
							bPos += temp;
					}
					else if ( bPos != temp2 && bPos > temp2 ) { //sub
						//if extra time exceeds destination, simply set new position
						if ( bPos - temp <= temp2 ) 
							bPos = temp2;
						//otherwise add orange's time to blue
						else 
							bPos -= temp;
					}
				}
			}
			
			else if ( turn == BLUE ) {
				//if not in position, move and press
				if ( bPos != blue[i][j] ) {
					temp = abs( bPos - blue[i][j] ) + 1; //amount of time blue used
					t += temp;
					bPos = blue[i][j];
				}
				//robot already in position
				else {
					temp = 1;
					t++;
				}
				temp2 = nextOrangeMove(i,j);
				//if blue's next move exists start moving to next location
				if ( temp2 != -1 ) {
					if ( oPos != temp2 && oPos < temp2 ) { //add
						//if extra time exceeds destination, simply set new position
						if ( oPos + temp >= temp2 ) 
							oPos = temp2;
						//otherwise add orange's time to blue
						else 
							oPos += temp;
					}
					else if ( oPos != temp2 && oPos > temp2 ) { //sub
						//if extra time exceeds destination, simply set new position
						if ( oPos - temp <= temp2 ) 
							oPos = temp2;
						//otherwise add orange's time to blue
						else 
							oPos -= temp;
					}
				}
			}
		}//end instruction
		
		solutions.push_back(t);
	}//end case
}

int nextOrangeMove(int i, int x) {
	
	for ( int j = x ; j < num_instructions[i] ; j++ ) {
		if (whoseTurn[i][j] == ORANGE) {
			//cout << "orange's next move: " << i << " " << j << endl;
			return orange[i][j];
		}
	}
	return -1; //no more orange moves in this case
}

int nextBlueMove(int i, int x) {
	
	for ( int j = x ; j < num_instructions[i] ; j++ ) {
		if (whoseTurn[i][j] == BLUE) {
			//cout << "blue's's next move: " << i << " " << j << endl;
			return blue[i][j];
		}
	}
	return -1; //no more blue moves in this case
}
