using namespace std;

#include <iostream>
#include <string>
#include <map>
#include <list>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <bitset>

#define ulong unsigned long

using namespace std; 

void main_A( istream &in, ostream &out )
{
	int numCases, i;
	in >> numCases; 
	string s; 
	getline( in, s );

	list< int > buttonTargets[2];
	int			  botPos[2]; 
	int			  targetIdx[2]; 
	list< int > nextToPush; 

	for( i = 0; i < numCases; ++i )
	{
		int nButtons, ii, tmp, bidx; 
		string bot; 
		in >> nButtons; 
	
		buttonTargets[0].clear();
		buttonTargets[1].clear();
		botPos[0] = botPos[1]  = 1;
		targetIdx[0] = targetIdx[1] = 0; 
		nextToPush.clear(); 
		for( ii = 0; ii < nButtons; ++ii ){
			in >> bot; 
			in >> tmp; 
			bidx = ( bot[ 0 ] == 'O' )? 0 : 1; 	
			nextToPush.push_back(bidx);
			buttonTargets[bidx].push_back( tmp ); 						
		}
		
		int seconds, bnext, bother; 
		seconds = 0;
		bnext = *nextToPush.begin();;
		bother = ( bnext )? 0 : 1; 

		while( nextToPush.size() )
		{
			++seconds;
			if( buttonTargets[ bother ].size() > 0 ){
				if( botPos[ bother ] < *(buttonTargets[ bother ].begin()) ){
					botPos[ bother ]++; 
				}
				if( botPos[ bother ] > *(buttonTargets[ bother ].begin()) ){
					botPos[ bother ]--; 
				}
			}

			if( botPos[ bnext ] < *(buttonTargets[ bnext ].begin()) ){
				botPos[ bnext ]++; 
			}else if( botPos[ bnext ] > *(buttonTargets[ bnext ].begin()) ){
				botPos[ bnext ]--; 
			}else{
				// push the button
				buttonTargets[ bnext ].pop_front();
				nextToPush.pop_front();
				if( nextToPush.size() > 0 ){
					bnext = *(nextToPush.begin());
					bother = ( bnext )? 0 : 1; 
				}
			}
		}

		out << "Case #" << (i+1) << ": " << seconds << endl; 
		getline( in , s ); // get the carry return 
	}
	return;
}
