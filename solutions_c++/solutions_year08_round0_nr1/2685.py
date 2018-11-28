#include <iostream>
#include <fstream>
#include <string>
using namespace std;
string engine[10];
string query[100];
int sw( int s, int q, int &index, int &change );

int main( ){
	ifstream fin( "A-small-attempt4.in");
	ofstream fout( "A-small.out" );
	int n, s, q;
	char ch;
	string str;
	fin >> n;
	for ( int i = 0; i < n; i++ ){
		fin >> s;
		ch = fin.get( );
		for ( int j = 0; j < s; j++ ){
			str.clear( );
			ch = fin.get( );
			while ( ch != '\n' ){
				str.push_back( ch );
				ch = fin.get( );
			}
			engine[j] = str;
		}
		fin >> q;
		ch = fin.get( );
		for ( int j = 0; j < q; j++ ){
			str.clear( );
			ch = fin.get( );
			while ( ch != '\n' ){
				str.push_back( ch );
				ch = fin.get( );
			}
			query[j] = str;
		}

        int index = 0, change = 0;
        fout << "Case #" << i+1 << ": " << sw( s, q, index, change ) << endl;
	}
}

int sw( int s, int q, int &index, int &change ){
	int m = -1;
	for ( int i = 0; i < s; i++ ){
		int j = index;
		while ( j < q && query[j] != engine[i] )
			j++;
		if ( j > m )
			m = j;
	}
	if ( m == q ){
		return change;
	}
	else {
		index = m;
		change++;
		return sw( s, q, index, change );
	}

}
