#include <iostream>
#include <cstring>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
template<class T> void atov(int n,T A[],vector<T> &vi){
  vi.clear();for (int i=0;i<n;i++) vi.push_back(A[i]);
}//NOTES:atov(
template<class T> void stov(string s,vector<T> &vi){
  vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));
}
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template <typename T> inline T Gcd( T a, T b) {
  // a, b should be unnegative
  if ( b == 0) return a;
  return Gcd( b, a % b);
}


ifstream input;
ofstream output;
int d[10020];
int len[10020];
int best[10020];
void init() {

}


void Work() {
  int i,j,n,D;
  input>> n;
  memset( best, -1, sizeof(best));
  for (i = 0; i< n;++i) {
    input>> d[i] >> len[i];
    
  }
  input>>D;
  best[0] = d[0];
  
  for (i = 0; i< n;++i) {
    if ( best[i] == -1)
      break;
    j = i + 1;
    while (true) {
      if ( j >= n || d[j] - d[i] > best[i])
        break;
      int t = min ( d[j] - d[i], len[j]);
      best[j] = max( best[j], t);
      ++j;
    }
  }
  bool flag = false;
  for (i = 0; i < n; ++i) {
      if ( D - d[i] <= best[i])
      flag = true;
  }
 
  if (flag) {
  output<<"YES"<<endl;
  } else {
    output<<"NO"<<endl;
  }
}
int main() {
  
int t = 0;
  string inputfile("input.in");
  string outputfile("output.out");
  input.open(inputfile.c_str());
  output.open(outputfile.c_str());
  input>>t;
  int tcase = 0;
  init();
  while( t--) {
    ++tcase;
    output<<"Case #"<<tcase<<": "; 
    Work();
  }
}

