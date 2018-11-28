#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <list>
#include <algorithm>
#include <stdio.h>
#include <string.h>

using namespace std;
#define FOR(VAR,START,STOP) for(int VAR=START;VAR<STOP;++VAR)
#define ZERO(V) memset( &V, 0, sizeof(V) )

int main()
{
	int G;
	string line;
	getline(cin, line);
	G=atoi(line.c_str());
	FOR(g,0,G)
	{
		int N;
		getline(cin, line);
		N = atoi(line.c_str() );
		// cout << "N:"<<N<<endl;
		typedef vector<int> intvect;

		intvect values;
		FOR(i,0,N)
		{
			int lastbit = 0;
			string line;
			getline(cin, line);
			// cout << "Line: " << line << endl;
			FOR(j,0,N)
			{
				if (line[j]=='1')
					lastbit = j;
			}
			// cout << lastbit << endl;
			values.push_back(lastbit);
		}
		int swaps = 0;
		FOR(i,0,N)
		{
			if (values[i] > i)
			{
				// devo intervenire, vado a prendere il primo valore <= i che segue
				int soluzione=0;
				FOR(j,i+1,N)
				{
					if (values[j] <= i)
					{
						// Trovato
						soluzione = j;
						// cout << "Sposto su " << values[j] << endl;
						break;
					}
				}
				swaps++;
				swap( values[soluzione], values[soluzione-1] );
				i = -1;
				continue;
			}
		}
		cout << "Case #" << g+1 << ": " << swaps << endl;
	}

	return 0;
}

/* vim: set shiftwidth=4:tabstop=4:autoindent:noexpandtab: */
