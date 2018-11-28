#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
#include <algorithm>

using namespace std;

const int DMAX = 5000;

int main() {

  ifstream in("A-small-attempt0.in");
  ofstream out("A-small.out");

  int L,D,N;
  in>>L>>D>>N;
  
  string s;
  getline(in,s);

  string w[DMAX];
  for (int i = 0; i<D; i++) {
    getline(in,w[i]);
  }

  for (int X = 1; X <= N; X++) {
    int K = 0;
    getline(in,s);
    
    for (int i = 0; i<D; i++) {
      
      string scopy = s;
      bool ok = true;
      
      // for (int j = 0; j<L; j++) {
      int j = 0;
      while (ok && (scopy != "")) {
	
	int beg = 0, en = 1;
	
        if (scopy.find("(") != string::npos) {
	  beg = scopy.find("(");
	  en = scopy.find(")")+1;
	}
	string t(scopy,beg,en);
	
	// determine the inclusion
	if (t.find(w[i][j]) == string::npos)
	  ok = false;
	
	
	if (scopy.find(")") != string::npos)
	  scopy.replace(0,scopy.find(")")+1,"");
	else
	  scopy.replace(0,1,"");
	
	//cout<<t<<endl;
	j++;
      }
      
      if (ok) K++;
    }
    
    out<<"Case #"<<X<<": "<<K<<endl;
  }

  in.close();
  out.close();
}
