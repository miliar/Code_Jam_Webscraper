#include <iostream>
#include <string>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <assert.h>
#include <list>
#include <set>
#include <vector>
#include <limits>
#include <map>

//Saving the Universe
//The assembly line scheduling from intro. to algorithms by Cormen et. al.
using namespace std;


class Node{

public:

	int cost;
	Node *previous;
	int searchEngine;
	int numQueries;

	Node(){
		
		searchEngine = -1;
		numQueries = 0;
		cost = 0;
		previous = 0;
	}

};


class Problem{
private:

public:

	vector<string> queries;
	vector<string> searchEngines;

	//nodes[i,j] represents the shortest path to search engine j after i queries
	map< pair<int,int>, Node > nodes;

	Problem(){
	}
	
	void solve(){

		for( int i = 0; i < (int)searchEngines.size(); ++i ){
			nodes[ make_pair<int,int>( 0,i ) ].searchEngine = i;
		}

		for( int i = 0; i < (int)queries.size(); ++i ){
			for( int j = 0; j < (int) searchEngines.size(); ++j ){

				//default cheapest to i+1,j is from i,j
				//(unless it's prohibited)
				if( queries[i] == searchEngines[j] ){
					nodes[ make_pair<int,int>( i+1,j ) ].cost = queries.size()+1;
				}else{
					nodes[ make_pair<int,int>( i+1,j ) ].numQueries = i+1;
					nodes[ make_pair<int,int>( i+1,j ) ].searchEngine = j;

					nodes[ make_pair<int,int>( i+1,j ) ].cost = nodes[ make_pair<int,int>( i,j ) ].cost;
					nodes[ make_pair<int,int>( i+1,j ) ].previous = &nodes[ make_pair<int,int>( i,j ) ];
					
					//relax path if possible
					int minCost = nodes[ make_pair<int,int>( i+1,j ) ].cost;
					for( int k = 0; k < (int) searchEngines.size(); ++k ){
						if( j == k ){
							continue;
						}
						if( nodes[ make_pair<int,int>( i,k ) ].cost+1 < minCost ){
							minCost = nodes[ make_pair<int,int>( i,k ) ].cost+1;
							nodes[ make_pair<int,int>( i+1,j ) ].cost = minCost;
							nodes[ make_pair<int,int>( i+1,j ) ].previous = &nodes[ make_pair<int,int>( i,k ) ];
						}
					}
				}
			}
		}
	}

	string PrintSolution( int problemNumber ){
		int minCost = queries.size()+1;
		for( int i = 0; i < (int)searchEngines.size(); ++i ){
			if( nodes[make_pair<int,int>( queries.size(), i )].cost < minCost ){
				minCost = nodes[make_pair<int,int>( queries.size(), i )].cost;
			}
		}
		
		stringstream ss;
		ss << "Case #" << problemNumber << ": " << minCost;
		return ss.str();
	}

	static Problem ReadProblem( std::istream &in ){
		
		Problem p;
		char buf[110];

		int numEngines;
		in >> numEngines;
		in.getline( buf, 109 ); //eat the newline

		for( int i = 0; i < numEngines; ++i ){
			in.getline( buf, 109 );

			string engineName( buf );
			p.searchEngines.push_back( engineName );
		}
		
		int numQueries;
		in >> numQueries;
		in.getline( buf, 109 ); //eat the newline

		for( int i = 0; i < numQueries; ++i ){
			in.getline( buf, 109 );

			string query( buf );
			p.queries.push_back( query );
		}
		
		return p;
	}

};


int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif

	int numProblems;
	std::cin >> numProblems;

	for( int i = 0; i < numProblems; ++i){
		Problem p( Problem::ReadProblem( std::cin ) );

		p.solve();

		std::cout << p.PrintSolution(i+1) << std::endl;
	}

	return 0;
}

