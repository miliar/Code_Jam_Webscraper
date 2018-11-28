#include <cstdio>
#include <iostream>
using namespace std;

void print_binary(int n) {

  int z = n;
  while (z>0) {
    printf("%d", z & 1);
    z = (z >> 1);
  }
}

int main() {

  //print_binary(32);
  //return 0;
  
  //FILE* file = fopen("file.in.txt", "r");
  FILE* file = fopen("A-small-attempt3.in", "r");
  FILE* fileOut = fopen("file.out.txt", "w");
  
  int T;
  fscanf(file, "%d", &T);
  cout << "Test cases : " << T << endl;
 
  int caseID = 0;
  for (caseID=1; caseID<=T; caseID++) {
    
    int N,K;
    fscanf(file, "%d %d\n", &N, &K);
    
    // check first N bits of K
    bool allOne = true;
    int Z = K;
    for (int i=0; i<N; i++) {
      int bit = Z & 1;
      if (bit!=1) {
        allOne = false;
        break;
      }
      Z = (Z >> 1);
    }
    fprintf(fileOut, "Case #%d: %s\n", caseID, allOne?"ON":"OFF");
  }
  cout << "OK" << endl;
}