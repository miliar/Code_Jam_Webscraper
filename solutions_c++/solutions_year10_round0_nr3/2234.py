#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>

//#define DEBUG


using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++)


int equalsQueue( queue<int> q1, queue<int> q2)
{
	int size = ( q1.size() < q2.size() ? q1.size() : q2.size() );

	return 0;
}

void printQueue( queue<int> q )
{
	cout << "Queue: ";
	while( !q.empty() ){
		int v = q.front();
		q.pop();
		cout << v << " ";
	}
}


int main(int argc, char** argv)
{
	//freopen("test.in", "r", stdin );
	//freopen("test.out", "w", stdout );
	freopen("C-small-attempt1.in", "r", stdin );
	freopen("C-small-attempt1.out", "w", stdout );
	//freopen("A-large.in", "r", stdin );
	//freopen("A-large.out", "w", stdout );

	int T;
	string line;

	cin >> T;
	getline(cin, line, '\n');
	for( int iT=0; iT < T; iT++){
		int R, k,N;
		queue<int> q;
		queue<int> qR0;
		int cycle = 0;
		vector<int> costs;

		cin >> R >> k >> N;

#ifdef DEBUG
		printf( "iT:%d R:%d k:%d N:%d\n", iT, R, k, N);
#endif //DEBUG

		for( int iN = 0; iN < N; iN++){
			int v;
			cin >> v;
			q.push(v);
		}

		//printQueue( q );

		int iR = 0;
		for(iR = 0;iR < R;iR++){
#ifdef DEBUG
			printf( "Round #%d: ", iR );
			printQueue( q );
#endif //DEBUG

			int knapsack = 0;
			for( int i = 0; i < (int)(q.size()) ;i++ ){
				int v = q.front();

				if( knapsack + v > k ){
					break;
				}

				knapsack += v;
				q.pop();
				q.push( v );
			}


			// Store cost
			if( iR == 0 ){
				costs.push_back( knapsack );
			}else{
				costs.push_back( costs.back() + knapsack );
			}

#ifdef DEBUG
			printf( "Cost: %d\n", costs.back() );
#endif //DEBUG

			// Store #1
			if( iR == 0 ){
				qR0 = q;
			}else{
				if( qR0 == q ){

#ifdef DEBUG
					printf( "Round ##: ");
					printQueue( q );
					printf( "\n");
#endif //DEBUG
					break;
				}
			}
		}
		if( iR < R ){
			cycle = iR;
		}else{
			cycle = iR - 1;
		}

#ifdef DEBUG
		printf( "Cycle: %d\n", cycle);
#endif //DEBUG

		// Cal cost
		int cost = 0;

		int multi = ( cycle != 0 ? (R - 1) / cycle : 0 );
		int remainder = ( cycle != 0 ? (R - 1) % cycle : (R - 1) );
		int unit = ( cycle != 0 ? costs[cycle] - costs[0] : 0);
		cost = costs[0] + unit * multi;
		if( remainder > 0 ){
			cost+= costs[remainder] - costs[0];
		}
#ifdef DEBUG
		printf( "0: %d multi: %d reminder: %d unit:%d\n", costs[0], multi, remainder, unit );
#endif //DEBUG
		printf( "Case #%d: %d\n", iT + 1, cost );


#ifdef DEBUG
		printf( "\n\n\n");
#endif //DEBUG
		//printQueue( q );
		//int v = q.front();
		//
		//q.pop();
		//q.push( v );

		//printQueue( q );
		//printQueue( qR0 );

	}


}