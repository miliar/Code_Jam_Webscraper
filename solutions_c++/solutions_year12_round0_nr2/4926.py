//
//  main.cpp
//  GCJ
//
//  Created by Bryan Hooi on 14/4/12.
//  Copyright (c) 2012 Clinkle. All rights reserved.
//

#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;
typedef vector<int> vi;
int main (int argc, const char * argv[])
{
  ifstream fin("/Users/HOOI/Documents/CS/GCJ/GCJ/in.txt");
  ofstream fout("/Users/HOOI/Documents/CS/GCJ/GCJ/out.txt");
  int cases; fin>>cases;
  for (int cs=1;cs<=cases;cs++){
    int n, surp, goal;
    fin>>n>>surp>>goal; 
    vi scores(n);
    for (int i=0;i<n;i++) fin>>scores[i];
    
    int points=0;
    int nonsurp=n-surp;
    for (int x=0;x<n;x++){
      bool canSurp=false, canNonSurp=false;
      for (int i=0;i<=10;i++){
        for (int j=i;j<=10;j++){
          int k=scores[x]-i-j;
          if (k<goal) continue;
          int maxdiff = max(max(abs(i-j),abs(j-k)),abs(i-k));
          if (maxdiff>2) continue;
          if (maxdiff==2) canSurp=true;
          if (maxdiff<2) canNonSurp=true;
          
        }
      }
      if (canSurp && !canNonSurp && surp>0) { surp--; points++; }
      else if (!canSurp && canNonSurp && nonsurp>0) { nonsurp--; points++;}
      else if (canSurp && canNonSurp) { points++;}
    }
    fout<<"Case #"<<cs<<": "<<points<<endl;
  }
  return 0;
}

