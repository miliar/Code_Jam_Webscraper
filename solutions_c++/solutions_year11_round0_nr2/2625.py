#include <iostream>
#include <fstream>
#include <stack>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main( int argc, char *argv[] ) {

  ifstream in(argv[1]);
  
  int t;
  int i,j;


  in >> t;


  for( i = 0; i < t; i++ ) {
    map<char,char> prod[100];
    bool oppo[100][100]={0};
    stack<char> elements;

    int c;
    in >> c;
    // Two base -> non base
    for( j = 0; j < c; j++ ) {
      char base1,base2,nonbase;
      in >> base1;
      in >> base2;
      in >> nonbase;
      prod[base1].insert( pair<char,char>(base2,nonbase) );
      prod[base2].insert( pair<char,char>(base1,nonbase) );
    }

    int d;
    in >> d;
    // Two base elements that are opposed
    for( j = 0; j < d; j++ ) {
      char a,b;
      in >> a;
      in >> b;
      oppo[a][b] = true;
      oppo[b][a] = true;
    }
    
    int n;
    in >> n;
    // single string containing n characters - the series of base elements
    for( j = 0; j < n; j++ ) {
      char curChar;
      in >> curChar;
      
      elements.push(curChar);

      // reduce if possible
      for( ;; ) {
	char last,secondLast;
	last = elements.top();
	elements.pop();
	if( !elements.empty() ) secondLast = elements.top();
	else {
	  elements.push( last );
       break;
	}

	if( prod[secondLast].count(last) > 0 ) { // production exists
	  elements.pop(); //pop that secondlast element too
	  elements.push( (prod[secondLast])[last] );
	} else {
	  elements.push(last);
       break;
	}


      }

      // see if need to clear (naive)
      char elem[100];
      int cnt=0,k,l;
      for( ;; ) {
	if( elements.empty() ) break;
	elem[cnt] = elements.top();
	elements.pop();
	cnt++;
      }
      
      bool flag = false;
      for( k = cnt-1; k >= 0; k-- ) {
	for( l = k-1; l >= 0 ; l-- ) {
	  if( oppo[elem[k]][elem[l]] ) { // need to clear
	    while( !elements.empty() ) elements.pop();
	    flag = true;
	    break;
	  }
	}
	if( flag ) break;
	elements.push( elem[k] );
     }
    }

    string output;

    if( !elements.empty() ) {
      output += elements.top();
      elements.pop();
    }
    for( ;; )  {
      if( elements.empty() ) {
	output+= "]";
	break;
      }
      output = ", " + output;
      output = elements.top() + output;
      elements.pop();
    }

    cout << "Case #" << i+1 << ": [" << output << endl;
  }


}
