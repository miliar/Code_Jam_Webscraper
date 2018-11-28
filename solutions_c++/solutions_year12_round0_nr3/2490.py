
#include <stdio.h>
#include <iostream>
#include <istream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;


int main(int argc, char **argv)
{
	/* I am too lazy for dynamic memory allocation here... */
	char DummyFileNameBuffer[255]; 
	/* Filename provided in input */
	char *pInputFileName = NULL;
	
	
	/******************************/
	/* Check input parameters     */
	/******************************/
	
	
	if (argc <= 1) { 
		
		/* No input parameters - read filename from std-in */
	
		cout << "No filename provided in input - please specify: ";
		cin >> DummyFileNameBuffer;
				
		pInputFileName = (char*) DummyFileNameBuffer;
		
	} else {
		
		/* Filename provided with input parameters */
		
		pInputFileName = (char*) argv[1];
	}
	

	/******************************/
	/* Open file                  */
	/******************************/
	

	ifstream currentLineStream;
	currentLineStream.open(pInputFileName);
	
	if ( ! currentLineStream.is_open()) {
		cout << "Unable to open file " << pInputFileName << " ... exit\n";
		return 1;
	}
	

	/******************************/
	/* Now Process Test Cases     */
	/******************************/

	unsigned int curTestCase;
	unsigned int totalNbTestCases;
	
	currentLineStream >> totalNbTestCases;
	
	for(curTestCase = 0; curTestCase < totalNbTestCases; curTestCase++) {
		
		/* Read next test case */
		
		unsigned int recycledPairs = 0;
		
		unsigned int A, B, n, permutated_n, last_digits_of_n;
		unsigned int exp, remove_pow, add_pow, nb_decimals;
		
		vector<unsigned int> previousPermutations;
		
		currentLineStream >> A;
		currentLineStream >> B;
		
		for (n = A; n < B; n++) {
			
			nb_decimals = (unsigned int) floor(log10(n));
			
			previousPermutations.clear();
			previousPermutations.reserve(nb_decimals);
			
			remove_pow = 10;
			add_pow    = pow(10, nb_decimals);
			
			/* create permutations of n */
			for(exp = 1; exp <= nb_decimals; exp++) {
				
				/* get last exp digits of n */
				last_digits_of_n = n % remove_pow;
				/* move digits to the beginning */
				permutated_n = (n / remove_pow) + (last_digits_of_n * add_pow );
				
				if (permutated_n > n && permutated_n <= B) {
															
					if (find (previousPermutations.begin(), previousPermutations.end(), permutated_n) ==  previousPermutations.end()) { ;
					
						previousPermutations.push_back(permutated_n);

						recycledPairs++;
					} 
				}
				
				//cout << n << ", last digits: " << last_digits_of_n << ", permutated n: " << permutated_n << endl;
				
				add_pow /= 10;
				remove_pow *= 10;
			}
		}
						
		cout << "Case #" << (curTestCase+1) << ": " << recycledPairs << endl; 
	}
	
	currentLineStream.close();
		
	return 0;
}
