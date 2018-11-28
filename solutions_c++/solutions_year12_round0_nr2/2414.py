//
//  main.cpp
//  b
//
//  Created by Andrew Bloch on 4/13/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//
int verbose = 0 ;

#include <iostream>
using namespace std ;


int maxScoreNormal(int total) {
  return (total + 2) / 3 ;
}
int maxScoreSurprising(int total) {
  if (total < 2) return total;
  if (total >= 26) return 10 ;
  return (total + 4)/3 ;  
}

int runTest() {
  int n,s,p;
  cin >> n >> s >> p;
  if (verbose)
    cout << "n " << n << " s " << s << " p " << p << endl;
  int count=0 ;
  int i ;
  for (i = 0 ; i < n ; i++) {
    int score ;
    cin >> score ;
    if (verbose)
      cout << score << " " << maxScoreNormal(score) << " " << maxScoreSurprising(score) << endl; 
    if (maxScoreNormal(score) >= p)
      count++;
    else if (maxScoreSurprising(score) >= p) {
      if (s) {
        count++ ;
        s--;
      }
    }
  }
  return count;
}

int main (int argc, const char * argv[])
{
  int testCases ;
  cin >> testCases ;
  if (verbose)
    cout << "Test cases: " << testCases << endl ;
  int i;
  for (i=0 ; i < testCases ; i++) {
    int r = runTest();
    cout << "Case #" << i + 1 << ": " ;
    cout << r;
    cout << endl;
  }

  return 0;
}

