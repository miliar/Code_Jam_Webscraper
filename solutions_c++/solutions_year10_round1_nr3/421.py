#include<string>
#include<iostream>
using namespace std;

int T, a1, a2, b1, b2;

string makeSeq( int n1, int n2 ){
  if( n1 == 0 || n2 == 0 ){
    return "";
  }
  int small = ( n1 < n2 ? n1 : n2 );
  int big = ( n1 > n2 ? n1 : n2 );
  int next = big / small;
  string th;
  if ( next > 1 ){
    th = "m";
  } else {
    th = "s";
  }
  th.append( makeSeq( small, big%small ) );
  return th;
}

string makeHighLevSeq( string seq ){
  int i=0;
  int last = seq.length()-1;
  string ret = "";
  bool ejectable = false;
  while( i <= last ){
    //cout << i << endl;
    if( seq[i] == 'm' ){
      ejectable = true;
      i += 1;
    } else if( i+1 <= last && seq[i] == 's' && seq[i+1] == 's' ){
      i += 2;
    } else { // just a single s
      if( ejectable ){
	// can forego the dominant position in this subseq
	ret.append( "e" );
      } else {
	// cannot
	ret.append( "f" );
      }
      ejectable = false;
      i++;
    }
  }
  return ret;
}

bool canWin( string seq ){
  int seen = 0;
  for( int i=0; i<(int)seq.size(); i++ ){
    if( seq[i] == 'f' ){
      seen ++;
    }
    if( seq[i] == 'e' ){
      return( seen % 2 == 0 );
    }
  }
  return seen%2 == 0;
}

int main(){
  cin >> T;
  for( int t=1; t<=T; t++ ){
    cin >> a1 >> a2 >> b1 >> b2;
    //string s = makeSeq( a1, b1 );
    //cout << s << endl;
    //cout << makeHighLevSeq( s ) << endl;
    int wins = 0;
    for( int a=a1; a<=a2; a++ ){
      for( int b=b1; b<=b2; b++ ){
	if( canWin( makeHighLevSeq( makeSeq( a, b ) ) ) ){
	  wins++;
	}
      }
    }
    cout << "Case #" << t << ": " << wins << endl; 
    // cout << canWin( makeHighLevSeq( makeSeq( 11, 2 ) ) );
  }

}
