/*-----------------------------------------*/
//Author      : Mir Riyanul Islam (Riyan)  //
//University  : AIUB                       //
//E-mail      : mir_riyan@yahoo.com        //
//Problem ID  : A                          //
//Problem Name: Speaking in Tongues        // 
//Contest     : Google Code Jam            //  
/*-----------------------------------------*/
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

#define ms 111	
	
using namespace std;

const double EPS = 1e-11;
const int INF = ( 1<<29 );
const double PI = 2 * acos( 0.0 );

int MAX( int a , int b ) { return a > b ? a : b;  }
int MIN( int a , int b ) { return a < b ? a : b;  }
void SWAP( int &a , int &b ) { int t = a; a = b; b = t; }
int GCD( int a , int b ) { while( b ) { b ^= a ^= b ^= a %= b; } return a; }

int main() {
	ifstream fin( "A-small-attempt0.in" );
	ofstream fout( "A_output.txt" );
	char ch , s[ms] , list[] = "yhesocvxduiglbkrztnwjpfmaq";
	int tc , cn = 0 , i , a;
	//fin.unsetf( ios::skipws );
	//while( !fin.eof() ) {
		fin >> tc;
		fin.getline( s , sizeof( s ) );
		//fin >> ch;
		while( tc-- ){
			//fflush(stdin);
			fin.getline( s , sizeof( s ) );
			int l = sizeof( s );
			for( i = 0 ; i < l ; i++ ) {
				if( s[i] >= 'a' &&  s[i] <= 'z' ) {
					a = s[i] - 97;
					s[i] = list[a];
				}
			}
			fout << "Case #" << ++cn << ": " << s << endl;
		}
	//}
	fin.close();
	fout.close();
	return 0;
}