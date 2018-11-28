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

int digits(int x) {
  if (x < 10) return 1 ;
  return 1+digits (x/10);
}
int nextPowerOfTen(int x) {
  if (x < 10) return 10 ;
  return 10*nextPowerOfTen(x/10);
}

int rotate(int x,int powerOfTen) {
  x *= 10 ;
  int c = x / powerOfTen ;
  x += c ;
  return x % powerOfTen ;
}

int checkPair(int x, int y, int digs, int powerOfTen) {
  int i ;
  for (i = 1; i < digs; i++) {
    y = rotate(y,powerOfTen);
    if (x == y) return 1;
  }
  return 0 ;  
}

int bruteForce(int a, int b) {
  int count = 0;
  int numDigits = digits(a);
  int powerOfTen = nextPowerOfTen(a);
  if (verbose)
    cout << "Digits: " << numDigits << " powerOfTen: " << powerOfTen << endl;
  int i,j ;
  for (i=a; i < b; i++) {
    for (j=i+1 ; j <= b ; j++) {
      if (checkPair(i,j,numDigits,powerOfTen)) {
        if (verbose>1)
          cout << i << " " << j << " recycled pair" << endl ; 
        count ++ ;
      }
    }
  }
  return count ;
}

int bruteForce2(int a, int b) {
  int count = 0 ;
  int numDigits = digits(a);
  int powerOfTen = nextPowerOfTen(a);
  if (verbose)
    cout << "Digits: " << numDigits << " powerOfTen: " << powerOfTen << endl;
  int i,j ;
  for (i=a; i < b; i++) {
    int rot = i ;
    for (j = 0 ; j < numDigits-1 ; j++) {
      rot = rotate(rot,powerOfTen) ;
      if ((rot > i) && (rot <= b))
        count++;
      else if (rot == i)
        break ;
    }
  }
  return count ;
}

int main (int argc, const char * argv[])
{
  int testCases ;
  cin >> testCases ;
  if (verbose)
    cout << "Test cases: " << testCases << endl ;
  int i;
  for (i=0 ; i < testCases ; i++) {
    int a,b ;
    cin >> a >> b ;
    if (verbose) {
      cout << "A = " << a << ", B = " << b << endl ;
    }
    
    cout << "Case #" << i + 1 << ": " ;
    cout << bruteForce2(a,b);
    cout << endl;
  }
  
  return 0;
}

