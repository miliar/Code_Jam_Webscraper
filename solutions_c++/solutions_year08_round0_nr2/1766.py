#include <iostream>
#include <list>

#define MAX_CHARS	100

using namespace std;

int getTime()
{
     int time, min;
     
     cin >> time;
     time *= 100;
     
     cin.ignore();  // ignore ':'
     cin >> min;
     
     time += min;
     
     return time;
}

/* 
 * Run through departures. If a train is not ready before departure,
 * increment the return value.
 */
int solve( list<int> &departs, list<int> &rdyTimes )
{
    int retVal = 0;
    
    while( !rdyTimes.empty() && !departs.empty() )
    {
         // not ready
         if( rdyTimes.front() > departs.front() )
             ++retVal;
         else
             rdyTimes.pop_front();

         departs.pop_front();
    }
    
    retVal += departs.size();
    
    return retVal;
}   
    
int main()
{
	int nCases, turnaround, nA, nB, ansA, ansB, j;
	list<int> departA, departB, rdyA, rdyB;
	
	cin >> nCases;

	for( int i = 1; i <= nCases; ++i )
	{
		// clear data
		ansA = ansB = 0;
		departA.clear();
		departB.clear();
		rdyA.clear();
		rdyB.clear();
		
		// read the turnaround time, NA, NB
		cin >> turnaround;
		cin >> nA;
		cin >> nB;
		
		// build the lists of A departure times and B "ready" times
		for( j = 0; j < nA; ++j )
		{
             departA.push_back( getTime() );
             rdyB.push_back( getTime() + turnaround );
        }
        
        // build the lists of B departure times and A "ready" times
        for( j = 0; j < nB; ++j )
        {
             departB.push_back( getTime() );
             rdyA.push_back( getTime() + turnaround );
        }
        
        departA.sort();
        departB.sort();
        rdyA.sort();
        rdyB.sort();
        
        ansA = solve( departA, rdyA );
        ansB = solve( departB, rdyB );
        
		cout << "Case #" << i << ": " << ansA << " " << ansB << endl;
	}
}
