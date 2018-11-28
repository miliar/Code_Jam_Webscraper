// a11.cpp : Defines the entry point for the console application.
// 

//#include "stdafx.h"

 #include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
 
using namespace std;
 
ifstream fin("d:\\2011\\t.in");
ofstream fout("d:\\2011\\t.out");
 
#define cin fin
#define cout fout

const int max_t = 10;

bool func(int tN,int tP, int aP )
{
	bool 	ret = false ;
	for( int n = 1 ;n <= tN ; ++ n )
		{
			int m = ( n * tP ) % 100 ;
			if ( m != 0 ) 
				continue;
			else 
				return true ;
			//for( int a = m ; ; a ++ )
			//{
			//	if ( (a*100) mod aP == 0 )
			//		{
			//		ret = true ;
			//		break;
			//		}
			//}
		}

	return ret ;

}

int _tmain(int argc, _TCHAR* argv[])
{  

//int nb = 8 % 3 ;
	int   N ;
	cin >> N ; 
  for(int n = 0; n < N; ++n)
  { 
	bool ret = false;
    int tN, tP, aP;
	cin >> tN >> tP >> aP ;
	if ( tP == aP ) 
		{
		ret = true ;
		}
	else if ( tP < 100 && aP == 100 )
		{
		ret = false;
		}
	else if ( aP == 0 && tP >0 )
		{
		ret = false ;
		}

	else 
		{
			ret = func( tN,tP,aP );
		}

	string s =   ret?"Possible":"Broken";
	cout << "Case #" << n + 1  << ": " << s   << endl;
  }
  return 0;


}

