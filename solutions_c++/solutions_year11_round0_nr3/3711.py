/*
 * GOOGLE CODE JAM QUALIFICATION ROUND 2011
 * Problem C: Candy Splitting
 *
 * @author: Paola Cucurullo Moreira
 *          paolacucurullo@gmail.com
 *
 */

#include "Problem.h"

//#define DEBUG

// Auxiliary function that solves a case
int solve_case (case_t c) {

	#ifdef DEBUG
	cout << "---->   Entering solve_case" << endl;
	#endif

	// Trash variables
	int acumulator = 0;
	int solution = 0;
	unsigned i;

	// Orders the vector
	sort (c.values.begin(), c.values.begin() + c.values.size());

	// Checks if there is a solution to the problem
	for (i = 0; i < c.values.size(); i++) {
		acumulator = acumulator ^ c.values[i];
	}
	if (acumulator != 0) {
		#ifdef DEBUG
		cout << "There is no solution" << endl;
		#endif
	} else {
		for (i = 1; i < c.values.size (); i++){
			solution = solution + c.values[i];
		}
		#ifdef DEBUG
		cout << "The solution is " << solution << endl;
		#endif
	}
	return solution;
}

// Constructor
Problem::Problem (int num_cases, vector<case_t> cases) {
	this->number_of_cases = num_cases;
	this-> cases = cases;
}

// Destructor
Problem::~Problem () {}

// Solves the problem. Returns the solutions to all cases
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
