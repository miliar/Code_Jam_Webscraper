
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
 
//struct mypair
//{
//  char a;
//  char b;
//  mypair(char aa,char bb):a(aa),b(bb)
//  { 
//  }
//  bool operator < ( const mypair & rhs ) const
//  {
//	  return a < rhs.a && b < rhs.b ;
//  }
//  bool operator == (  const mypair & rhs ) const
//  {
//	  return a == rhs.a && b == rhs.b ;
//  }
//};

typedef std::pair<char,char> mypair ;

int main()
{
	int   N ;
	cin >> N ; 


	for(int n = 0; n < N; ++n)
	{
		int c1 , c2 ,c3;
		cin >> c1 ;

		map<mypair,char> rule1 ;
		map<char,char>   rule2 ;

		for( int i=0 ;i < c1 ; i ++ )
		{
			string s ;
			cin >> s ;  
			rule1[ mypair(s[0],s[1] ) ] = s[2] ;
			rule1[ mypair(s[1],s[0] ) ] = s[2] ;
		}

		cin >> c2 ;

		for( int i=0 ;i < c2 ; i ++ )
		{
			string s ;
			cin >> s ;
			rule2[ s[0] ] = s[1] ,rule2[ s[1] ] = s[0] ;
		}

		cin >> c3 ;
		string text ;
		cin >> text ;
 

		vector<char> temp ; 

		char end, append ;
		for( int i=0 ;i< c3 ; i++ )
		{
			if ( 0 == temp.size() ) 
			{
				temp.push_back( text[i] ) ;
				continue ;
			}

			append = text[i] ;

			while(true)
			{
				if( temp.size() == 0 )
				{
					temp.push_back(append) ;
					break ;
				}
				end = * ( temp.end() -1 ) ;
				if ( rule1.find( mypair( end,append ) ) == rule1.end() ) 
				{
					vector<char>::iterator pos = find(temp.begin(),temp.end(), rule2[append] );
					if( pos == temp.end() )  
						temp.push_back( append ) ;
					else
						temp.clear( );
					break ;
				}
				else{
					temp.pop_back() ;
					append = rule1[  mypair( end,append ) ] ;
				}
			} 


		}
		
		if ( temp.size() == 0 ) 
		{
			cout << "Case #" << n + 1 << ": " <<  "[]" << endl;
			continue ;
		}
 
 
		cout << "Case #" << n + 1 << ": [" ;
		for(int j=0;j<temp.size()-1;j++) cout <<  temp[j] << ", " ;
		cout <<  *(temp.end()-1) << "]"<<endl ;
 
	}
	return 0;
}

