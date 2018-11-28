/*
 * GOOGLE CODE JAM QUALIFICATION ROUND 2011
 * Problem A: Bot Trust
 *
 * @author: Paola Cucurullo Moreira
 *          paolacucurullo@gmail.com
 *
 */

#include "Problem.h"

//#define DEBUG

// Auxiliary function that solves a case
int solve_case (case_t c) {

	// Trash auxiliary variables
	unsigned i, j;
	int found = 0;
	int completed;
	// Current positions of the robots
	int pos_orange = 1;
	int pos_blue = 1;
	// Next objective positions of the robots
	int next_orange, next_blue;
	// Movement vectors of each robot
	vector<int> mov_orange, mov_blue;
	// Clears the vectors to start afresh
	mov_orange.clear();
	mov_blue.clear();

	for (i = 0; i < c.movements.size(); i++){
		#ifdef DEBUG
		cout << "Movements[" << i << "] = " << c.movements[i].who << ", " << c.movements[i].which << endl;
		#endif
	}

	// Processes all movements
	#ifdef DEBUG
	cout << "---->   Entering solve case. num mov = " << c.movements.size() << endl;
	#endif
	for (i = 0; i < c.movements.size(); i++) {
		completed = 0;
		#ifdef DEBUG
		cout << "Movements[" << i << "] = " << c.movements[i].who << ", " << c.movements[i].which << endl;
		#endif
		while (!completed) {
			if (c.movements[i].who == ORANGE) { //ORANGE
				next_orange = c.movements[i].which;
				#ifdef DEBUG
				cout << "Next_orange = " << next_orange << endl;
				#endif
				for (j = i+1; j < c.movements.size(); j++) {
					if (c.movements[j].who == BLUE) {
						found = j;
						next_blue = c.movements[j].which;
						#ifdef DEBUG
						cout << "Blue found = " << found << ", next_blue = " << next_blue << endl;
						#endif
						break;
					}
				}
				if (next_orange == pos_orange) {
					mov_orange.push_back(PRESS);
					completed++;
					#ifdef DEBUG
					cout << "Orange presses button " << next_orange << endl;
					#endif
				} else if (next_orange > pos_orange) {
					mov_orange.push_back(FORWARD);
					pos_orange++;
					#ifdef DEBUG
					cout << "Orange moves forward " << pos_orange << endl;
					#endif
				} else {
					mov_orange.push_back(BACK);
					pos_orange--;
					#ifdef DEBUG
					cout << "Orange moves back " << pos_orange << endl;
					#endif
				}
				if (!found) {
					mov_blue.push_back(NONE);
					#ifdef DEBUG
					cout << "Blue has no more movements, so he stays put" << endl;
					#endif
				} else if (next_blue == pos_blue) {
					mov_blue.push_back(NONE);
					#ifdef DEBUG
					cout << "Blue is already in position, and waiting for his turn" << endl;
					#endif
				} else if (next_blue > pos_blue) {
					mov_blue.push_back(FORWARD);
					pos_blue++;
					#ifdef DEBUG
					cout << "Blue moves forward " << pos_blue << endl;
					#endif
				} else {
					mov_blue.push_back(BACK);
					pos_blue--;
					#ifdef DEBUG
					cout << "Blue moves backward " << pos_blue << endl;
					#endif
				}
			} else { // BLUE
				next_blue = c.movements[i].which;
				#ifdef DEBUG
				cout << "Next_blue = " << next_blue << endl;
				#endif
				for (j = i+1; j < c.movements.size(); j++) {
					if (c.movements[j].who == ORANGE) {
						found = j;
						next_orange = c.movements[j].which;
						#ifdef DEBUG
						cout << "Orange found = " << found << ", next_orange = " << next_orange<< endl;
						#endif
						break;
					}
				}
				if (next_blue == pos_blue) {
					mov_blue.push_back (PRESS);
					completed++;
					#ifdef DEBUG
					cout << "Blue presses button " << next_blue << endl;
					#endif
				} else if (next_blue > pos_blue) {
					mov_blue.push_back (FORWARD);
					pos_blue++;
					#ifdef DEBUG
					cout << "Blue moves forward " << pos_blue << endl;
					#endif
				} else {
					mov_blue.push_back (BACK);
					pos_blue--;
					#ifdef DEBUG
					cout << "Blue moves back " << pos_blue << endl;
					#endif
				}
				if (!found) {
					mov_orange.push_back(NONE);
					#ifdef DEBUG
					cout << "Orange has no more movements, so he stays put" << endl;
					#endif
				} else if (next_orange == pos_orange) {
					mov_orange.push_back (NONE);
					#ifdef DEBUG
					cout << "Orange is already in position, and waiting for his turn" << endl;
					#endif
				} else if (next_orange > pos_orange) {
					mov_orange.push_back (FORWARD);
					pos_orange++;
					#ifdef DEBUG
					cout << "Orange moves forward " << pos_orange << endl;
					#endif
				} else {
					mov_orange.push_back (BACK);
					pos_orange--;
					#ifdef DEBUG
					cout << "Orange moves back " << pos_orange << endl;
					#endif
				}
			}
			#ifdef DEBUG
			cout << "\npos_orange = " << pos_orange << ", pos_blue = " << pos_blue << endl;
			cout << "next_orange = " << next_orange << ", next_blue = " << next_blue << "\n" << endl;
			#endif
		}
	}
	return (int) mov_orange.size ();
}

// Constructor
Problem::Problem (int num_cases, vector<case_t> cases) {
	this->number_of_cases = num_cases;
	this-> cases = cases;
}

// Destructor
Problem::~Problem () {}

// Solves the problem. Returns the number of movements necessary
vector<int> Problem::solve () {
	#ifdef DEBUG
	cout << "---->   Entering solve" << endl;
	#endif
	unsigned i;
	vector<int> v;

	// Recorre los casos uno a uno
	for (i = 0; i < cases.size(); i++) {
		v.push_back(solve_case (cases[i]));
	}

	return v;
}
