/*Speaking in Tongues*/

#include "scanner.h"
#include "strutils.h"
#include "genlib.h"
#include "simpio.h"
#include "vector.h"
#include <iostream>
#include <fstream>

/*Function prototypes */

int IntegerGetter(ifstream & infile);
int SolveTestCase(ifstream & infile);
void AddNextLetter(Vector<string> & solution, Vector<string> & eleminvoked, int i, Vector<Vector<string>> & basecombos, Vector<Vector<string>> & opposers, string & outputstr);
Vector<string> FindOutput(Vector<Vector<string>> & basecombos, Vector<Vector<string>> & opposers, Vector<string> & eleminvoked);

/*Main program*/

int main() {
	ifstream infile;
	ofstream outfile;
	infile.open("C:\\Users\\Alborz\\Desktop\\toungetest6.txt");
	if(infile.fail()){
		cout << "Didn't work" << endl;
	} else {
		cout << "Opened" << endl;
	}
	outfile.open("C:\\Users\\Alborz\\Desktop\\Codejamtest.txt");
	if(outfile.fail()){
		cout << "Didn't work" << endl;
	} else {
		cout << "Opened" << endl;
	}

	int numcases = IntegerGetter(infile);

	
	for(int i = 0; i < numcases; i++){
		int solution = SolveTestCase(infile);
		outfile << "Case #" << i + 1 << ": " <<  solution << endl;
	}


	return 0;
}

int IntegerGetter(ifstream & infile) {
	string str;
	getline(infile, str);
	int num = StringToInteger(str);
	return num;
}

int SolveTestCase(ifstream & infile) {
	int num_googlers, num_surp, best_score, current_tot_pts, solution, can_be;
	double test;
	string str;
	Scanner scanner;
	getline(infile, str);
	scanner.setSpaceOption(Scanner::IgnoreSpaces);
	scanner.setInput(str);
	
	string num_string = scanner.nextToken();	
	num_googlers = StringToInteger(num_string);

	string surp_string = scanner.nextToken();
	num_surp = StringToInteger(surp_string);

	string best_string = scanner.nextToken();
	best_score = StringToInteger(best_string);


	can_be = 0;
	solution = 0;

	for(int i = 0; i < num_googlers; i++) {
		str = scanner.nextToken();
		current_tot_pts = StringToInteger(str);
		test = (current_tot_pts - best_score) / 2.0;  
		if(current_tot_pts <= best_score) {
			if( current_tot_pts < best_score) {
				continue;
			} else {
				if(current_tot_pts > 2) {
					continue;
				} else if (current_tot_pts < 2) {
					solution++;
					continue;
				} else {
					if(num_surp > 0) {
						num_surp--;
						solution++;
						continue;
					}
				}
			}
		}
		if( test >= (best_score - 1) && test > 0) {
			can_be++;
			solution++;
		} else if( test >= (best_score - 1) && test <= 0) {
			solution++;
		} else if (test <  (best_score - 1) && test >= (best_score - 2) ) {
			num_surp--;
			if(num_surp >= 0) solution++; 
		} else if (test < (best_score - 2) ) {
			continue;
		}
	}


	//if(num_surp > 0) {
		//if(num_surp <= can_be) {
		//	return solution;
		//} else {
		//	return 0;
		//}
	//} 
	return solution;
}