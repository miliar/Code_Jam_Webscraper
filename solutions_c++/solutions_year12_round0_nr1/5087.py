#include <iostream>
#include <fstream>

using namespace std;

char* trainGooglerese( ) 
{
  int numChars = ('z' - 'a')+1;
  cout << numChars << endl;
  char* out = new char[numChars];

  for( int i=0; i<numChars; i++ )
    out[i] = 0;

  out['z'-'a'] = 'q'; out['q'-'a'] = 'z';

  ifstream inData( "train.in" );
  ifstream outData( "train.out" );

  int T, t, pos;
  string line, line2;
  inData >> T;
  t = 0;
  getline( inData, line );

  while( t < T ){
    t++;
    getline( inData, line );
    cout << "line: " << line << endl;
    getline( outData, line2 );
    cout << "line2: " << line2 << endl;
    
    for( int i=0; i< line.size(); i++ ){
      if ( line[i] != ' ' ){
	pos = line[i]-'a';
	out[pos] = line2[i];
      }
    }
  }

  inData.close();
  outData.close();

  return out;
}

int main( )
{
  char* mapping = trainGooglerese();

  for( int i=0; i <= ('z' - 'a'); i++ )
    cout << (char)('a' + i) << " -> " << mapping[i] << endl; 

  ifstream inData;
  ofstream outData;

  inData.open( "A-small.in" );
  outData.open( "A-small.out" );

  int T; string line;

  inData >> T;
  getline( inData, line );
  for( int t=0; t<T; t++ ){
    getline( inData, line );
    outData << "Case #" << (t+1) << ": ";

    for( int i=0; i<line.size(); i++ ){
      if ( line[i] == ' ' )
	outData << ' ';
      else 
	outData << mapping[line[i]-'a'];
    }
    outData << endl;
  }

  inData.close();
  outData.close();
  delete[] mapping;
  return 0;
}
