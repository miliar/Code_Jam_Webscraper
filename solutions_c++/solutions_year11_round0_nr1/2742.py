#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main() {

  ifstream in("A-large.in");

  int t,n;
  int i,j;
  char colour;
  int button;

  int currentBlue, currentOrange;
  char currentColour;

  in >> t;
  for( i = 0; i < t; i++ ) {

    int seconds = 0;
    queue<int> blue, orange;
    queue< pair<char,int> > everything;
    in >> n;

    for( j = 0; j < n; j++ ) {
      in >> colour;
      in >> button;
      if( colour == 'O' ) orange.push(button);
      else blue.push(button);
      everything.push( pair<char,int>(colour,button) );
    }
    
    currentBlue = 1;
    currentOrange = 1;

    // process input now
    while( !everything.empty() ) {
      currentColour = everything.front().first;

      if( currentColour == 'O' ) {
	if( currentOrange == orange.front() ) { // orange push button
	  everything.pop();
	  orange.pop();
	} else { // else orange move
	  if( currentOrange < orange.front() ) currentOrange++;
	  else currentOrange--;
	}
	
	if( currentBlue != blue.front() ) { // blue should get ready for its next push
	  if( currentBlue < blue.front() ) currentBlue++;
	  else currentBlue--;
	}
      } else {
	if( currentBlue == blue.front() ) { // blue push button
	  everything.pop();
	  blue.pop();
	} else { // else blue move
	  if( currentBlue < blue.front() ) currentBlue++;
	  else currentBlue--;
	}
	
	if( currentOrange != orange.front() ) { // orange should get ready for its next push
	  if( currentOrange < orange.front() ) currentOrange++;
	  else currentOrange--;
	}
      } // if

      seconds++;
    } //while

    cout << "Case #" << i+1 << ": " << seconds << endl;
  }
}
