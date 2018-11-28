#include <cstdio>
#include <iostream>
using namespace std;


int main() {

  //FILE* file = fopen("C-test-in.txt", "r");
  FILE* file = fopen("C-small-attempt0.in", "r");
  FILE* fileOut = fopen("C-file.out.txt", "w");
  
  if (file==NULL) {
    cout << "File not found" << endl;
    return -1;
  }
  
  int T;
  fscanf(file, "%d", &T);
  cout << "Test cases : " << T << endl;
 
  int caseID = 0;
  for (caseID=1; caseID<=T; caseID++) {
    
    long long R,k,N;
    // R: rounds, k: capacity, N: number of groups
    fscanf(file, "%lld %lld %lld", &R, &k, &N);
    //cout << "R:" << R << "    k:" << k << "    N:" << N << endl;
    long long groups[1000]; // people in each group
    for (long long i=0; i<N; i++) {
      fscanf(file, "%d", &(groups[i]));
      //cout << groups[i] << " ";
    }
    //cout << endl;
    
    long long queueStart = 0;
    long long money = 0;
    for (long long r = 0; r<R; r++) {
      long long sum = 0;
      long long numGroupsIn = 0;
      for (long long z=queueStart; z<queueStart + N; z++) {
        long long i = z % N;
        if (sum + groups[i]<= k) {
          sum += groups[i];
          numGroupsIn++;
        }
        else 
          break;
      }
      money+= sum;
      queueStart += (numGroupsIn % N);
    }
    
    fprintf(fileOut, "Case #%d: %lld\n", caseID, money);
  }
  cout << "OK" << endl;
}
