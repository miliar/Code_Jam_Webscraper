#include<iostream>

using namespace std;

char m[] = "yhesocvxduiglbkrztnwjpfmaq";

string decode( string code );

int main(){
  
  int T;
  cin >> T;
  
  string line;
  getline( cin, line );
  
  for( int i=0; i<T; ++i ){
    getline( cin, line );
    cout << "Case #" << i+1 << ": " << decode( line ) << endl;
  }
  
}

string decode( string code ){
  string result( code.size(), ' ' );
  for( int i=0; i<code.size(); ++i ){
    if( code[i] != ' ' )
      result[i] = m[code[i]-'a'];
    else
      result[i] = ' ';
  }
  return result;
}