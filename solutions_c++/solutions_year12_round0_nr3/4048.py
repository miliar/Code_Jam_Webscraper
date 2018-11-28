#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <string>
#include <set>
using namespace std;
set<pair<int,int> > pairs;
inline int countRecycles(int a, int b, int len){
  int temp;
  int shift = pow(10,len-1);
  int x = a;
  int count = 0;
  for(int i=1; i < len; i++){
    temp = x/10;
    x =((x-temp*10)*shift)+temp;
    if(x > a && x <= b){
      pair<int,int>(a,x);
      if(pairs.insert(pair<int,int>(a,x)).second)
        count++;
    }
  }
  return count;
}

int main(int argc, char** argv){
  int cases;
  cin >> cases;
  int a,b;
  string astr;
  int sum;

  for(int i=1; i<(cases+1); i++){
    cin >> astr;
    cin >> b;
    int len = astr.length();
    int a = atoi(astr.c_str());
    sum = 0;
    for(; a < b; a++)
      sum += countRecycles(a, b, len);
    pairs.clear();
    cout << "Case #" << i << ": " << sum <<endl;
  }
}