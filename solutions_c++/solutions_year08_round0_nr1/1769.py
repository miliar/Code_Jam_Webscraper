#include <iostream>
#include <list>
#include <string>

#define MAX_CHARS	100

using namespace std;

int main()
{
	int numCases, numSwitches, nEngines, nQry, j;
	list<string> engines, engCopy;
	cin >> numCases;

	for( int i = 1; i <= numCases; ++i )
	{
		// clear all data
		numSwitches = 0;
		engines.clear();
		engCopy.clear();

		// build the list of engines
		cin >> nEngines;
		cin.ignore();  // ignore the '\n'

		for( j = 0; j < nEngines; ++j )
		{
			char line[MAX_CHARS];
			cin.getline( line, MAX_CHARS );
			
			string eng( line );
			engines.push_back( eng );
		}

		/* as the query is read, remove the query's matching engine
		 * from list of engines, once the list is emptied, a switch is made
		 * and the list of engines reloaded, except for the last engine that
		 * was removed
		 */
		cin >> nQry;
		cin.ignore();  // ignore the '\n'

		engCopy = engines;
		for( j = 0; j < nQry; ++j )
		{
			char line[MAX_CHARS];
			cin.getline( line, MAX_CHARS );

			string qry( line );

			engCopy.remove( qry );

			if( engCopy.empty() )
			{
				engCopy = engines;
				engCopy.remove(qry);

				++numSwitches;
			}
		}

		cout << "Case #" << i << ": " << numSwitches << endl;
	}
}
