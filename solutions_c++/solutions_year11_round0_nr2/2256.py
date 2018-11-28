#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define DEBUG 0

const int MAX_C = 36;
const int MAX_D = 28;
const int MAX_N = 100;

int invocationList[ MAX_N ];
int currentList[ MAX_N ];

const int NUMCHAR = 26;


int combo[NUMCHAR][NUMCHAR];
bool isACombo[NUMCHAR][NUMCHAR];
bool areOpponents[NUMCHAR][NUMCHAR];

inline int c2i( char c )
  {
    return static_cast<int>( c - 'A' ); 
  }

inline char i2c( int i )
  {
    return static_cast<char>( i + static_cast<int>( 'A' ) );
  }

int main()
{
    ifstream fin( "input.txt" );
    ofstream fout( "output.txt" );
    int T;
    fin >> T;
    for ( int t=0; t<T; t++ )
      {
        // inizializzazione
        for ( int i=0; i<NUMCHAR; i++ )
          for ( int j=0; j<NUMCHAR; j++ )
            isACombo[i][j] = areOpponents[i][j] = false;
              
      
        int C, D, N;
        char c1,c2, cr;
        fin >> C;
        for ( int i=0; i<C; i++ )
          {
            fin >> c1 >> c2 >> cr;
            isACombo[ c2i( c1 ) ][ c2i( c2 ) ] = isACombo[ c2i( c2 ) ][ c2i( c1 ) ] = true;
            combo[ c2i( c1 ) ][ c2i( c2 ) ] = combo[ c2i( c2 ) ][ c2i( c1 ) ] = c2i( cr );
          }
        fin >> D;
        for ( int i=0; i<D; i++ )
          {
            fin >> c1 >> c2;
            areOpponents[ c2i( c1 ) ][ c2i( c2 ) ] = areOpponents[ c2i( c2 ) ][ c2i( c1 ) ] = true;
          }
        fin >> N;
        for ( int i=0; i<N; i++ )
          {
            fin >> c1;
            invocationList[i] = c2i( c1 );
          }
        if ( DEBUG )
          {
            cout << "Combos list: ";
            for ( int i=0; i<NUMCHAR-1; i++ )
              for ( int j=i; j<NUMCHAR; j++ )
                if ( isACombo[i][j] )
                  cout << i2c( i ) << i2c( j ) << i2c( combo[i][j] ) << " ";
            cout << "\n";
            cout << "Opponents list: ";
            for ( int i=0; i<NUMCHAR-1; i++ )
              for ( int j=i+1; j<NUMCHAR; j++ )
                if ( areOpponents[i][j] )
                  cout << i2c( i ) << i2c( j ) << " ";
            cout << "\n";
            cout << "Invocations list: ";
            for ( int i=0; i<N; i++ ) cout << i2c( invocationList[i] );
            cout << "\n";
          }
          
        int index = -1;
        for ( int i=0; i<N; i++ )
          {
            currentList[++index] = invocationList[i];
            
            if ( DEBUG ) { cout << "PRIMA: "; for ( int j=0; j<=index; j++ ) cout << i2c( currentList[j] ); cout << "\n"; }
            
            bool comboApplied = false;
            // si applica la regola di combinazione, se possibile
            while ( index > 0 && isACombo[ currentList[index] ][ currentList[index-1] ] )
              {
                currentList[ index - 1 ] = combo[ currentList[index] ][ currentList[index-1] ];
                index--; // ora index punta all'ultimo elemento della lista
                comboApplied = true;
              }
            if ( index > 0 && !comboApplied )
              {
                for ( int j=0; j<index; j++ )
                  if ( areOpponents[ currentList[index] ][ currentList[j] ] )   // se ci sono due elementi avversari svuota la lista
                    {
                      index = -1;
                      break;
                    }
              }
            if ( DEBUG ) { cout << "DOPO: "; for ( int j=0; j<=index; j++ ) cout << i2c( currentList[j] ); cout << "\n"; }
          }
        
        if ( DEBUG ) system( "PAUSE" );
        
        fout << "Case #" << t+1 << ": ["; 
        for ( int j=0; j<=index-1; j++ ) fout << i2c( currentList[j] ) << ", ";
        if ( index != -1 )
          fout << i2c( currentList[index] ); 
        fout << "]\n";
      } 
  
  fin.close();
  fout.close();
  if ( DEBUG ) system( "PAUSE" );
}
