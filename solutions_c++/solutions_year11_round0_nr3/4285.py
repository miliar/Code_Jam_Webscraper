#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main (int argc, char* argv[]) {

  if (argc < 2) {
    cout << "not enough arguments" << endl;
    return -1;
  }

  ifstream input(argv[1]); // open file 

  int numcases = 0;

  if (input.good()) {
    input >> numcases;

    for (int i = 1; i <= numcases; i++) {
      cout << "Case #" << i << ": ";
      int numelements = 0;
      input >> numelements;

      vector<int> candy;
      
      // fill 'candy' with elements
      for (int j = 0; j < numelements; j++) {
	int temp = 0;
	input >> temp;
	candy.push_back(temp);

      }

      // is there a solution?
      int validcheck = 0;
      for (int j = 0; j < numelements; j++) {
	validcheck ^= candy[j];
      }

      if (validcheck != 0) {
	cout << "NO" << endl;
      }  
      // begin to split
      else {
	sort (candy.begin(), candy.end());
	
	int patcandy = 0;
	int seancandy = 0;
	int seanpile = 0; // hold the solution
	for (int j = 0; j < numelements; j++) {
	  patcandy += candy[j];
	  seanpile = 0;
	  for (int k = j + 1; k < numelements; k++) {
	    seanpile += candy[k];
	  }

	  // at the end, does sean's pile equal pat's candy?
	  if (patcandy ^ seanpile == 0) {
	    cout << seanpile << endl;
	    break;
	  }
	}
	
      }

    }
    
  }

  return 0;
}
