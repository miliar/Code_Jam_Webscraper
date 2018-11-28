#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <valarray>
#include <algorithm>
#include <map>
#include <time.h>
#include <bitset>
using namespace std;


int main()
{

  vector<long long> pows(32);
  pows[0] = 1;
  for (int i=1; i<pows.size(); i++){
    pows[i] = pows[i-1]*2;
  }
  ifstream in("A-large.in");
  
  ofstream out("A-large.out");
  int T = 0;
  int N = 0;
  long long K = 0;
  in>>T;
  for (int t = 0; t<T; t++){
    
    in>>N;
    in>>K;
    bool hasCurrent = ((K-(pows[N]-2)-1) % pows[N] == 0);
    if (hasCurrent){
      out<<"Case #"<<t+1<<": ON"<<endl;
    }
    else{
      out<<"Case #"<<t+1<<": OFF"<<endl;
    }

  }
  in.close();
  out.close();
  return 0;
}
