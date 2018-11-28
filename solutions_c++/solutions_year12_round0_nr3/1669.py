#include <vector>
#include <iostream>
#include <stdlib.h>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;


inline int checkString(int A, int B) {
  int num = 0;
  char s[8];
  sprintf(s,"%d",A);
  int digits = strlen(s);
  int check;
  set<int> solution;
  for(int i=1; i < digits;++i){
    for(int r=0;r<digits;++r){
      rotate(s,s+1,s+digits);
      check = atoi(s);
      if(check>A && check <= B){
	if(solution.end () == solution.find(check)){
	  ++num;
	  solution.insert(check);
	}
      }
    }
  }
  return num;
}

unsigned long long bf(int A, int B) {
  unsigned long long num =0;
  for(int i =A;i<B;++i){
    num +=checkString(i,B);
  }
  return num;
}

int main() {
  int T;
  cin>>T>>ws;
  for(int t = 1 ;t<=T;++t) {
    int A, B;
    cin >> A>>B;

    cout << "Case #"<<t<<": "<<bf(A,B)<<endl;
  }
}
