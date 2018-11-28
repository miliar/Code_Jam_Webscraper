#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

#if 0

#define CIN cin
#define COUT cout


#else

FILE *ofp;
FILE *ifp;

#define SCANF(fmt, ...) fscanf_s(ifp, fmt, ##__VA_ARGS__)
#define PRINTF(fmt, ...) fprintf(ofp, fmt, ##__VA_ARGS__)



#endif


int main() {
  int N;
  long K;
  int C;
  ifstream myfile;
  ofstream res;
  myfile.open("A-large.in");
  res.open("res-large.txt");
  myfile >> C;
  int c = 1;
  while(c <= C) {
    myfile >> N >> K;
    long T = 1 << N;
    T--;
    K ^= -1l;
    K &= T;
    res << "Case #" << c << ": " << (K == 0 ? "ON" : "OFF") << endl;
    c++;
  }
}