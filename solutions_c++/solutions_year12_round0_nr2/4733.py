#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
#include <algorithm>

using namespace std;

int main() {

  
  ifstream in("B-large.in");
  ofstream out("B-large.out");
  
  int T,N,S,p;
  int t[101];
  in>>T;

  
    for (int cases = 1; cases <= T; cases++) {
    
    in>>N>>S>>p;
    for (int i = 0; i<N; i++)
      in>>t[i];
    

    int k = 0;
    for (int i = 0; i<N; i++) {
    
      if (p>=2)
	if (S>0)
	  if (3*p-4<=t[i] && t[i]<3*p-2) {
	    k++;
	    S--;
	  }

      if (t[i]>= 3*p-2)
	k++;
    }

    out<<"Case #"<<cases<<": ";    
    out<<k<<"\n";
    
  }

  in.close();
  out.close();
}
