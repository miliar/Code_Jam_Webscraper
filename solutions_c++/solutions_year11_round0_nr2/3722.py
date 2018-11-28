#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

string getElementList( const string& invokedElem
                     , const vector< string >& combPairs
                     , const vector< string >& oppositePairs
                     )
{
  string finalString("");
  for( unsigned k = 0; k < invokedElem.length(); ++k ) {
    if( finalString == "" ) {
      finalString += invokedElem[ k ];
      continue;
    }
    bool someFlag( false );
    for(;;) {
      char lastChar = finalString[ finalString.length() - 1 ];
      bool breakOff( true );
      for( unsigned m = 0; m < combPairs.size(); ++m ) {
        if(  ( ( lastChar == combPairs[m][0] ) && ( invokedElem[k] == combPairs[m][1] ) ) 
          || ( ( lastChar == combPairs[m][1] ) && ( invokedElem[k] == combPairs[m][0] ) ) ) {
            finalString = finalString.substr( 0, finalString.length() - 1 ) + combPairs[m][2];
            breakOff = false;
            someFlag = true;
            //break;
        }
      }//for( combPair )
      if( breakOff )
        break;
    }//for(;;)
    if( someFlag ) continue;
    //cout<<"I am here"<<endl;
    for( unsigned m = 0; m < oppositePairs.size(); ++m ) {
      char tempChar( 0 );
      if( oppositePairs[m][0] == invokedElem[k] )
        tempChar = oppositePairs[m][1];
      if( oppositePairs[m][1] == invokedElem[k] )
        tempChar = oppositePairs[m][0];
      if( tempChar ) {
        for( unsigned n = 0; n < finalString.length(); ++n ) {
          if( tempChar == finalString[n] ) {
            finalString = "";
            break;
          }
        }//for( n )
      }
      //cout<<"he he"<<endl;
      if( finalString == "" )
        break;
    }//for( oppositePairs )
    if( finalString != "" ) finalString += invokedElem[k];
  }//for( k < invokedElem )
  string final("");
  final = '[';
  for( unsigned k = 0; k < finalString.length(); ++k ) {
    final += finalString[k];
    final += ", ";
  }
  final += ']';
  if( finalString == "" )
    return "[]";
  return
    final.substr( 0, final.length() - 3 ) + ']';;
}


int main()
{
  vector< string > final;
  int numOfTestCase( 0 );
  scanf( "%d", &numOfTestCase );
  for( int i = 0; i < numOfTestCase; ++i ) {
    vector< string > combPairs;
    vector< string > oppositePairs;
    string invokedElem("");
    int numOfCombs;
    scanf( "%d", &numOfCombs );
    for( int j = 0; j < numOfCombs; ++j ) {
      string temp("");
      cin >> temp;
      combPairs.push_back( temp );
    }
    char space;
    scanf( "%c", &space );
    int numOfOpps( 0 );
    scanf( "%d", &numOfOpps );
    for( int j = 0; j < numOfOpps; ++j ) {
      string temp("");
      cin >> temp;
      oppositePairs.push_back( temp );
    }
    scanf( "%c", &space );
    int junk( 0 );
    scanf( "%d", &junk );
    cin >> invokedElem;
    string invoke = getElementList( invokedElem, combPairs, oppositePairs );
    final.push_back( invoke );
  }//for( numOfTestCases )
  for( int i = 0; i < numOfTestCase; ++i ) {
    cout<<"Case #"<<i+1<<": "<<final[i]<<endl;
  }
  return 0;
}




