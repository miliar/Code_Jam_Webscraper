 
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

typedef unsigned long long myulonglong ;
int main()
{
int   N ;
cin >> N ; 
  for(int n = 0; n < N; ++n)
  {

	int  k ;
	cin >> k ;

	int min = 1000000 ;
	int summary = 0 ;
	int eofV = 0 ;
	vector<myulonglong> mv ;
	mv.resize(k);
	for( int i = 0; i< k ; i ++ )
	{
		cin >> mv[i] ;
		eofV ^=  mv[i] ;
		//
		summary +=  mv[i] ;
		if ( mv[i] > 0 && mv[i] < min )
			min = mv[i] ;
	}

	if ( eofV != 0 || k == 1 )
	{
		 cout << "Case #" << n + 1 << ": " <<  "NO" << endl;
		 continue ;
	}

	myulonglong endv = summary - min ;  
    cout << "Case #" << n + 1 << ": " <<  endv << endl;
  }
  return 0;
}

