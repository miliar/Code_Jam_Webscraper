#include <stdio.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

int main() {
  int T, orig,novo,mindif,rpta;
  string tmp,sorig;
  cin >> T;
  for( int k=1; k<=T; k++ ) {
    cin >> tmp;
    sscanf(tmp.data(),"%d",&orig);
    rpta = orig*10;
    tmp = tmp+"0";

    sort( tmp.begin(), tmp.end() );
    while( next_permutation( tmp.begin(), tmp.end() ) ) {
      sscanf(tmp.data(),"%d",&novo);
      if( novo>orig && novo<rpta ) {
        mindif=(novo-orig);
	rpta = novo;
      }
    }
    cout<< "Case #"<<k<<": "<<rpta<<endl;
  }
  return 0;
}
