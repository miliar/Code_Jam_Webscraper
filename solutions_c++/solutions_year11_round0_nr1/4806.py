/*
 *  robots.cpp
 *  
 *
 *  Created by Wedzerai Muyengwa on 5/7/11.
 *  Copyright 2011 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <deque>
#include <iterator>
#include <map>

using namespace std;

int getMinTime(deque<int>& O_buttons, deque<int>& B_buttons, map<int, char>& sequence);

int main(int argc, char *argv[])
{
	deque<int> O_buttons;
	deque<int> B_buttons;
	map<int, char> sequence; 
	int numTestcases, numButtons;
	
	/* get and open the input file */
	char *filename = argv[1];
	ifstream input(filename);
	ofstream output("output.txt");
	
	//input >> numTestcases;
	string line;
	int firstline = 0;
	int lineNum = 1;
	while (getline(input, line)) {			
		stringstream myStream;
		myStream << line;
		if (firstline==0) {
			myStream >> numTestcases;
			firstline ++;
			continue;
		}

		myStream >> numButtons;
		for (int i=0; i < numButtons; ++i ) {
			char robot;
			int button;
			myStream >> robot >> button;
			if (robot == 'O'){
				O_buttons.push_back(button);
				sequence[i+1] = 'O';
			}	
			else if (robot == 'B'){
				B_buttons.push_back(button);
				sequence[i+1] = 'B';
			}
		}
		
		
		cout << "Buttons to be pressed by O: " ;
		copy(O_buttons.begin(), O_buttons.end(), ostream_iterator<int>(cout, " "));
		cout << "\nButtons to be pressed by B : " ;
		copy(B_buttons.begin(), B_buttons.end(), ostream_iterator<int>(cout, " "));
		cout << endl;
		
		
		int min_time = getMinTime(O_buttons, B_buttons, sequence);
		
		
		cout << "Number of steps taken is " << min_time << endl;
		output << "Case #" << lineNum << ": " << min_time << endl;
		lineNum ++;
		
		O_buttons.clear();
		B_buttons.clear();
		sequence.clear();
	}
	
	
	//vector<string> lines;
	//copy(istream_iterator<string>(input), istream_iterator<string>(), back_inserter(lines));
	
	//copy(lines.begin(), lines.end(), ostream_iterator<string>(cout, "\n"));
	return 0;
}

int getMinTime(deque<int>& O_buttons, deque<int>& B_buttons, map<int, char>& sequence)
{
	int b_curr = 1, b_next = B_buttons[0], o_curr = 1, o_next = O_buttons[0];
	char next = sequence[1];
	int step = 0;
	int sequenceItr = 1;
	int sequenceSize = sequence.size();
	for (map<int, char>::iterator itr = sequence.begin(); itr != sequence.end(); ++itr)
		cout << itr->first << " : " << itr->second << endl;
	cout << "O Buttons : ";
	for (deque<int>::iterator itr= O_buttons.begin(); itr != O_buttons.end(); ++itr)
		cout << *itr << " ";
	cout << "\n\nB Buttons : ";
	for (deque<int>::iterator itr= B_buttons.begin(); itr != B_buttons.end(); ++itr)
		cout << *itr << " ";
	cout << endl << endl;; 
	do {
		switch (next) {
			case 'O':
				if (o_curr == o_next) { // press button so O remains in place
					O_buttons.pop_front();
					o_next = O_buttons.front();// sequence[sequenceItr];
					sequenceItr ++;
					next = sequence[sequenceItr];
					cout << "O press button \t" << o_curr << "\t";
				}
				else if (o_curr < o_next) {
					o_curr++;
					cout << "O moves one step forward\t" ;
				}
				else {
					o_curr--;
					cout << "O moves one step backward\t" ;
				}
				if (b_curr < b_next) {
						b_curr++;
					cout << "B moves one step forward" << endl;
				}
				else if (b_curr > b_next){
					b_curr-- ;
					cout << "B moves one step backward\t" << endl ;
				}

				break;
			case 'B':
				if (o_curr < o_next) {
					o_curr++;
					cout << "O moves one step forward\t" ;
				}
				else if (o_curr > o_next){
					o_curr-- ;
					cout << "O moves one step backward\t" ;
				}
				
				
				if (b_curr == b_next) {
					B_buttons.pop_front();
					b_next = B_buttons.front();// sequence[sequenceItr];
					sequenceItr ++;
					next = sequence[sequenceItr];
					cout << "B press button \t" << b_curr << endl;
				}
				else if (b_curr < b_next) {
					b_curr++;
					cout << "B moves one step forward\t" << endl ;
				}
				else if (b_curr > b_next) {
					b_curr--;
					cout << "B moves one step backward\t" << endl  ;
				}
				
				
				break;
		}
		step++;
		//cout << "Iteration: " << step << endl;
	} while( sequenceItr < sequenceSize+1);
	 
	return step;

}

























