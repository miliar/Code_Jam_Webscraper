#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

typedef long unsigned int lli;

lli gcd(const lli& a, const lli& b) {
  if (b == 0)
    return a;
  else
    return gcd(b,a%b);
}

lli greatest_divisor_capped(const lli& n, const lli& max) {
  for (lli i = max; i >= 1; --i) {
    if (n%i == 0)
      return i;
  }
  return 1;
}


int main(int argc, char** argv){

  if (argc != 2) {
    cerr << "Input file missing!" << endl;
    return 0;
  }

  ifstream iFile;
  iFile.open(argv[1]);
  if (!iFile.is_open()) {
    cerr << "Failed to open input file!" << endl;
    return 0;
  }

  ofstream oFile;
  oFile.open("out.txt");
  if (!oFile.is_open()) {
    cerr << "Failed to open output file!" << endl;
    return 0;
  }

clock_t t0 = clock();
clock_t now;

  int C,N;
  lli t[1000];

  iFile >> C;
  for (int c = 1; c <= C; ++c) {

now = clock();
printf("T %d/%d : %f\n",c,C,((double)(now - t0))/(double)CLOCKS_PER_SEC);

    lli global_gcd = 0;
    iFile >> N;
    for (int n = 0; n < N; ++n)
      iFile >> t[n];

    for (int i = 0; i < N - 1; ++i) {
      for (int j = i + 1; j < N; ++j) {

        lli delta = (t[i] > t[j]) ? (t[i] - t[j]) : (t[j] - t[i]);
printf("\tdelta:%lu\n",delta);
        if (global_gcd == 0)
          global_gcd = delta;

        lli g = gcd(delta,global_gcd);
printf("\tgcd:%lu\n",g);
        if (g < global_gcd)
          global_gcd = g;
      }
    }

    printf("\tglobal_gdc: %lu\n",global_gcd);

    lli g = -1;
    lli y = -1;
    do {
      ++y;
      g = gcd(t[0] + y, t[1] + y);
//printf("\t\tgcd(%ld,%ld) = %ld\n",t[0] + y, t[1] + y,g);
    } while ( (g%global_gcd) != 0);

    oFile << "Case #" << c << ": " << y << endl;
  }

  iFile.close();
  oFile.close();

  return 0;
}
