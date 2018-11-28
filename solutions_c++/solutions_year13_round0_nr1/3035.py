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

void init() {

}

bool win(char ch, const vector<string>& chess) {
  // Check row
  int s = 0;
  for (int i = 0; i < chess.size(); ++i) {
    s = 0;
    for (int j = 0; j< chess[0].size(); ++j) {
      s += (chess[i][j] == ch) ||(chess[i][j] == 'T');
    }
    if (s == 4) return true;
  }
  
  for (int i = 0; i < chess[0].size(); ++i) {
    s = 0;
    for (int j = 0; j< chess.size(); ++j) {
      s += (chess[j][i] == ch) ||(chess[j][i] == 'T');
    }
    if (s == 4) return true;
  }
  s = 0;
  for (int i = 0; i< chess[0].size(); ++i) {
    s += (chess[i][i] == ch) || (chess[i][i] == 'T');
  }
  if (s == 4) {
    return true;
  }
  s = 0;
  for (int i = 0; i< chess.size(); ++i) {
    s += (chess[i][chess.size()-1-i] == ch)
         || (chess[i][chess.size()-1-i] == 'T');
  }
  if (s == 4) {
    return true;
  }
  return false; 
}
                                                
bool unfinished(const vector<string>&chess) {
  for (int i = 0; i< chess.size(); ++i) {
    for (int j = 0; j < chess[0].size(); ++j) {
      if (chess[i][j] == '.') {
        return true;
      }
    }
  }
  return false;
}


void Work() {

  vector <string> chess;
  string tmp;
  chess.clear();
  for (int i = 0; i< 4; ++i) {
    getline(input, tmp);
    if (tmp.size() == 0) {
      getline(input, tmp);
    }
    chess.push_back(tmp);
  }
  if ( win('X', chess) ) {
    output<<"X won"<<endl;
  } else if (win('O', chess)) {
    output<<"O won"<<endl;
  } else if (unfinished(chess)) {
    output<<"Game has not completed"<<endl;
  } else {
    output<<"Draw"<<endl;
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
