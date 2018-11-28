#include <iostream>
#include <set>
#include <cstring>
#include <cstdlib>
#include <sstream>

using namespace std;

// bool r[2000001][2000001];

std::string IntToStr(int tmp)
{
  std::ostringstream out;
  out << tmp;
  return out.str();
}

int StrToInt(string tmp){
  return atoi(tmp.c_str());
}

int getRecycles(int n , int B ){
  int r = 0;
  string ns, ms;
  ns = IntToStr(n);
  ms = ns;
  ms += ns;
  int l = ns.size();
  set<int> c;
//   cout << "Para " << n << endl;
  for(int i = 1 ; i < l ; ++i){
    string substring = ms.substr(i,l);
    int m = StrToInt(substring);
//     cout << "\tProbando " << m << endl;
    if( n < m && m <= B && c.count(m) == 0){
      c.insert(m);
      ++r;
    }
  }
  return r;
}

bool isRecycled(int n , int m ){
  string ns, ms;
  ns = IntToStr(n);
  ms = IntToStr(m);
  if(ns.size() != ms.size()){
    return false;
  }
  ns += ns;
  return  ns.find(ms) != string::npos;
}

int main(){
  int c;
  cin >> c;
  for(int i = 1 ; i <= c ; ++i){
    int A, B;
    cin >> A >> B;
    int recycled = 0;
    for(int n = A ; n < B ; ++n){
      recycled += getRecycles(n,B);
//       for(int m = n+1; m <= B ; ++m){
// //         cout << "Probando " << n << " y " << m << endl;
//         if(isRecycled(n,m)){
//           ++recycled;
//         }
//       }
    }
    cout << "Case #" << i << ": " << recycled << endl;
  }
}