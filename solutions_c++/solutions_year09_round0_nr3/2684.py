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

long welcome_count;
char welcome_string[20];

void countWelcome ( int index, char *line ) {
	if ( index == 18 ) {
		for ( int i = 0; line[i] != '\0'; i++ ) {
			if ( line[i] == 'm' ) {
				welcome_count++;
				welcome_count %= 10000;
			}
		}
		return;
	}
	for ( int i = 0; line[i] != '\0'; i++ ) {
		if ( welcome_string[index] == line[i] ) countWelcome ( index + 1, &line[i+1] );
	}
	

}

int welcomeToCodeJamProblem ( ifstream *file, ofstream *outputfile ) {

	strcpy ( welcome_string, "welcome to code jam" );
	welcome_count = 0;

	int number_of_cases = 0;
	*file >> number_of_cases;
	char line[500];
	file->getline( line, 500, '\n' );
	for ( int i = 0; i < number_of_cases; i++ ) {
		file->getline( line, 500, '\n' );
		countWelcome ( 0, line );
		welcome_count %= 10000;
		*outputfile << "Case #" << i+1 << ": " << (welcome_count%10000)/1000 << (welcome_count%1000)/100 << (welcome_count%100)/10 << welcome_count%10 << endl;
		welcome_count = 0;
	}
return 0;
}




int main(int argc, char* argv[])
{
	ofstream outputfile ("C:\\Documents\ and\ Settings\\neeraj.surana\\Desktop\\output.txt");
	ifstream myfile ("C:\\Documents\ and\ Settings\\neeraj.surana\\Desktop\\A-small.in");
	  if (myfile.is_open() && outputfile.is_open())
	  {	
		  welcomeToCodeJamProblem ( &myfile, &outputfile );
	  }
	outputfile.close();
	myfile.close();
	return 0;
}


