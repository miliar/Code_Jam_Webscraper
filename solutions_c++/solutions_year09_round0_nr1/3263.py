// Codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <list>
#include <set>

using namespace std;


int alienLanguageProblem ( ifstream *file, ofstream *outputfile ) {
int lower_case_chars, number_of_words, number_of_cases;
int result = 0;
	*file >> lower_case_chars;
	*file >> number_of_words;
	*file >> number_of_cases;
	char line[10000];
	file->getline( line, 1000, '\n' );
	typedef map<int, int> MyMap;
		map<char,MyMap> case_map;

	std::set<string> words;
	for ( int i = 0; i < number_of_words; i++ ) {
		file->getline( line, 10000, '\n' );
		words.insert (line);
	}
	for ( int j = 0; j < number_of_cases; j++ ) {

		
		file->getline ( line, 10000, '\n' );
		for ( int k = 0, letter = 0; line[k] != '\0'; k++ ) {
			if ( line[k] == '(') {

				while ( line[k] != ')') {
					(case_map[line[k]])[letter] = 0;
//					printf ( " %c %d %d", line[k], letter , (case_map[line[k]]).count(letter));
//					printf ( " %c %d" , line[k], letter );
					k++;
				}
//				getchar();
				letter++;
			}
			else {
				(case_map[line[k]])[letter] = 0;
				//	printf ( " %c %d" , line[k], letter );
//				getchar();
				letter++;

			}
//			printf ("\n");
		}

	set<string>::iterator it = words.begin();
	
	while ( it != words.end() ) {
		int some_counter = 0;
		char *c_word = new char[ (*it).size() +1 ];
		strcpy ( c_word, (*it).c_str() );
		bool word_exist = true;
		for ( int i = 0; c_word[i] != '\0'; i++ ) {
			if ( case_map.count(c_word[i]) == 0 ) {
				word_exist = false;
				break;
			} else if ( case_map[c_word[i]].count(i) == 0 ) {
				word_exist = false;
				break;
			}
		}
		if ( word_exist ) result++;
		
		it++;
		delete c_word;
	}

	*outputfile << "Case #" << j+1 << ": " << result << endl;
//		printf ("Case #%d: %d\n", j + 1, result);
		case_map.clear();
		result = 0;
	}
//	printf ( "%d" , result );
	getchar();
	return 0;
}





int main(int argc, char* argv[])
{
	ofstream outputfile ("C:\\Documents\ and\ Settings\\neeraj.surana\\Desktop\\output.txt");
	ifstream myfile ("C:\\Documents\ and\ Settings\\neeraj.surana\\Desktop\\A-small.in");
	  if (myfile.is_open() && outputfile.is_open())
	  {	
		  alienLanguageProblem ( &myfile, &outputfile );
	  }
	outputfile.close();
	myfile.close();
	return 0;
}


