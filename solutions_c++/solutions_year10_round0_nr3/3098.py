// codeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using std::cout;
using std::cin;	
using std::endl;


int calculate( int rounds, int capasity, int* que, int que_size){
	int sum = 0, i = 0, on_board, start;
	for ( int current = 0; current < rounds; current++){
		on_board = 0;
		start = i;
		do {
			if ( (que[i] + on_board) <= capasity )
				on_board+=que[i];
			else
				break;
			i++;
			i = i % que_size;
		} while ( i != start );
		sum += on_board;
	}
	return sum;
}
 

int _tmain(int argc, _TCHAR* argv[])
{
	int T,R,k,N;
	int* g;
	cin>>T;
	for(int i = 0; i < T; i++) 
	{
		cin>>R>>k>>N;
		g = new int[N];
		for( int j = 0; j<N; j++)
			cin>>g[j];
		cout<<"Case #"<<(1+i)<<": "<< calculate( R, k, g, N)<<endl; 
		delete g;
	}
	return 0;
}

