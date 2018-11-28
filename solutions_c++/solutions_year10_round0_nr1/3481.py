#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string dectobin( int i){
  string reverse;
  while( i != 0 ){
    if( i%2 == 0 ) reverse += '0';
    else reverse += '1';
    i = i / 2;
  }
  return reverse;
}

int main(){
  ifstream f("in.in");
  ofstream o("out.out");
  int t;
  f >> t;
  int n, k;
  bool result;
  vector<bool> lamps;
  string series;
  for( int i(0); i < t; ++i ){
    f >> n;
    f >> k;
    result = true;
    series = dectobin( k );
    if( series.size() < n ) result = false;
    else{
      for( int j(0); j < n; ++j ){
        if( series[j] == '0' ) result = false;
      }
    }
    if( result ){
      o << "Case #" << i+1 << ": ON\n";
    }else{
      o << "Case #" << i+1 << ": OFF\n";
    }
  }
  system("pause");
  return 0;
}