#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <ctype.h>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

int main(){ 
  ifstream in("A-large.in");
  ofstream out("A-large.out");  
  int N;
  int K;
  int i;
  int inc;
  int cont=1;
  bool ON;
  int cases;
  in>>cases;
  while(cases--){
    in>>N>>K;  
    ON = false;
    while((1<<N)-1<=K){
      i = (1<<N)-1;
      inc = 1<<(N+1);
      while(i<=K){
	if(K==i){
	  ON = true; 
	  break;
	}
	i+=inc;
      }
      if(ON)break;
      N++;
    }
    out<<"Case #"<<(cont++)<<(ON?": ON":": OFF")<<endl;
  }
  in.close();
  out.close();
  return 0;
}
