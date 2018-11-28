#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

bool snap (long N, long K) {
  if ( (1<<N) -1 == K% (1<<N))
    return true;
    else return false;     
}

int main () {
   ifstream ifs("A-large.in");
   ofstream ofs("A.out");
   long T;
   ifs >> T;
   long snappers, clicks;
   for (long k = 0; k < T; k++){
      ifs >> snappers;
      ifs >> clicks;
      if (snap(snappers, clicks))
        ofs << "Case #" << (k+1) << ": ON\n";
      else ofs << "Case #" << (k+1) << ": OFF\n";
   }
   ofs.close();
   return 0;
   
}
