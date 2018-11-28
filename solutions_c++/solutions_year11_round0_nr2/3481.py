/*** This code is supposed to run variable length arrays ***/


#include <iostream>
#include <fstream>
#include <cstring>
#include <list>
#include <vector>

using namespace std;


typedef struct {
	char first, second;
} opposition;

typedef struct {
	char first, second;
	char result;
} combination;

int main( int argc, char** argv )
{

	// Which file has to be processed?
	cout << "Processing " << argv[1] << endl;
	
	ifstream inputfile( argv[1], ios_base::in );
	ofstream outputfile( "outputfile", ios_base::out );
	
	// How many cases to treat
	int numcases;
	inputfile >> numcases;
	
	// Check whether this suffices in any case
	// For Magicka, suffices
	const int LINEMAX = 2001;
	
	char line[ LINEMAX ];
	
	// Skip the rest of the first line, which is empty anyway
	inputfile.getline( line, LINEMAX );
	
	
	/*** Init variables for each case ***/
	
	int num_combinations, num_oppositions, num_invokations;
	vector<combination> combinations;
	vector<opposition> oppositions;
	string invokations;
	list<char> elements;
	
	/*** variables done ***/
	
	
	for( int ll = 0; ll < numcases; ll++ )
	{
	
		cout << "Process case " << ll << endl;
		
		outputfile << "Case #" << ll+1 << ": ";
		
		/*** clean case variables and read input ***/
		
		inputfile >> num_combinations;
		
		combinations.resize(num_combinations);
		
		for( int k = 0; k < num_combinations; k++ )
		{
			string triple("");
			inputfile >> triple;
			combinations[k].first = triple.c_str()[0];
			combinations[k].second = triple.c_str()[1];
			combinations[k].result = triple.c_str()[2];
			cout << "Combination: " << combinations[k].first << combinations[k].first << endl;
		}
		
		inputfile >> num_oppositions;
		
		oppositions.resize(num_oppositions);
		
		for( int k = 0; k < num_oppositions; k++ )
		{
			string triple("");
			inputfile >> triple;
			oppositions[k].first = triple.c_str()[0];
			oppositions[k].second = triple.c_str()[1];
			cout << "Opposition: " << combinations[k].first << combinations[k].first << endl;
		}
		
		inputfile >> num_invokations;
		
		inputfile >> invokations;
		
		elements.clear();
		
		/*** COMPUTE SOLUTION ***/
		
		/*
		Idea:
			0: if no more invokations, FINISH
			1: pop element from input and append to list
			2: if list size < 2 goto 0;
			3: select last and second-to-last elements
			4: if these form an combination
				perform combination
				goto 2
			5: if these form a opposition
				perform opposition
				goto 2
		*/
		int i = 0;
		while( i < num_invokations+1 )
		{
			
			
			if( elements.size() >= 2 ){
				
				bool combined = false, opposed = false;
				
				/* Check for combinations */
				
				char el1 = elements.back();
				elements.pop_back();
				char el2 = elements.back();
				elements.push_back( el1 );
				
				for( int k = 0; (!combined) && k < combinations.size(); k++ ) {
					combination C = combinations[k];
					
					if( (el1 == C.first && el2 == C.second) || (el2 == C.first && el1 == C.second) ) {
						elements.pop_back(); elements.pop_back();
						elements.push_back( C.result );
						combined = true;
						cout << "Combine " << el1 << el2 << " to " << C.result << endl;
					}
					
				}
				
				if( combined ) continue;
				
				/* Check for oppositions */
				
				for( int k = 0; (!opposed) && k < oppositions.size(); k++ ) {
					opposition O = oppositions[k];
					bool e1 = false, e2 = false;
					for( list<char>::iterator it = elements.begin(); it != elements.end(); it++ ) {
						if( *it == O.first ) { e1 = true; }
						else if( *it == O.second ) { e2 = true; }
					}
					
					if( e1 && e2 ) {
						elements.clear();
						opposed = true;
						cout << "Cleared" << endl;
					}
				}
				
				if( opposed ) continue;
				
			}
						
			/* append from invokations*/
			
			if( i == invokations.size() ) break;
			
			elements.push_back( invokations[i] );
			i++;
			
		}
		
		
		/*** SOLUTION COMPUTED ***/
		
		if( elements.size() == 0 )
		{
			outputfile << "[]" << endl;
		} else if ( elements.size() == 1 )
		{
			outputfile << "[" << *(elements.begin()) << "]" << endl;
		} else
		{
			outputfile << "[" << *(elements.begin());
			elements.pop_front();
			for( list<char>::const_iterator it = elements.begin(); it != elements.end(); it++ )
				outputfile << ", " << *it;
			outputfile << "]" << endl;
		}
	
	}
	
	inputfile.close();
	outputfile.close();
	
	return 0;
	
}