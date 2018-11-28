// 2601.cpp : Defines the entry point for the console application.
//

// #include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
 
using namespace std;
 
ifstream fin("H:\\2011\\t.in");
ofstream fout("H:\\2011\\t.out");
 
#define cin fin
#define cout fout
  
const int PRESS = 1 ;


int main()
{
int   N ;
cin >> N ; 
  for(int n = 0; n < N; ++n)
  {

	int step ;
	cin >> step ;
	int time_c = 0 ; 
	int bcur = 1 , ocur = 1 ;

	int last_b_t = 0 , last_o_t = 0 ;

	for ( int i= 0 ;i < step ; i ++ )
	{
		char c ;
		int  pos ;
		cin >> c >> pos ;

		if( c == 'O' ) 
		{
			int move  =  abs( pos - ocur  ); //distance
			int real_move =  last_b_t  > move  ? 0 : move - last_b_t ;
			time_c += real_move + PRESS ;
			 
			last_o_t += real_move +PRESS ;

			last_b_t = 0 ;
			ocur = pos ;
			 
		}
		else {
			int move = abs( pos - bcur ) ;
			int real_move = last_o_t > move ? 0 : move - last_o_t ;
			time_c += real_move + PRESS ;

			last_b_t += real_move +PRESS ;

			last_o_t = 0 ;
			bcur = pos ; 
		}
	}

    cout << "Case #" << n + 1 << ": " <<  time_c << endl;
  }
  return 0;
}

