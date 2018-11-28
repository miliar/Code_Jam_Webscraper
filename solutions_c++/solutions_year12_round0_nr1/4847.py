#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
#include <algorithm>

using namespace std;

int main() {

  ifstream in("A-small.in");
  ofstream out("A-small.out");

  int T;
  in>>T;

  string G,S;
  getline(in,G);
  
  for (int cases = 1; cases <= T; cases++) {
    const string alphG = "ynficwlbkuomxsevzpdrjgthaq";
    const string alphS = "abcdefghijklmnopqrstuvwxyz";
    
    //   in>>G;
    getline(in,G);
    S = G;

    for (int i = 0; i<G.size(); i++) {
      size_t found = alphG.find(G[i]);
      if (found != string::npos) {
	S[i] = alphS[found];
      }
    }

    out<<"Case #"<<cases<<": ";    
    out<<S<<"\n";
 
  }

  in.close();
  out.close();
}
