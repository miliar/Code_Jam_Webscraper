#include <stdio.h>
#include <inttypes.h>

#include <iostream>
using namespace std;

namespace {
size_t Check(size_t Pd) {
  if (Pd == 0)
    return 1;

  size_t result = 1;
  for (size_t i = 0; i < 2; ++i) {
    if (Pd % 2 != 0)
      result *= 2;
    else
      Pd /= 2;

    if (Pd % 5 != 0)
      result *= 5;
    else
      Pd /= 5;
  }

  return result;
}

void PrintOutput(size_t iter, const char* result) {
  printf("Case #%d: %s\n", iter+1, result);
}
} //namespace

int main() {
  size_t T;
  cin >> T;

  for (size_t i = 0; i < T; ++i) {
    uint64_t N;
    size_t Pd,Pg;
    cin >> N >> Pd >> Pg;
    size_t min = Check(Pd);

    if (N < min)
      PrintOutput(i, "Broken");
    else {
      if (Pd != 100 && Pg == 100)
        PrintOutput(i, "Broken");
      else if (Pd != 0 && Pg == 0)
        PrintOutput(i, "Broken");
      else
        PrintOutput(i, "Possible");
    }
  }
  return 0; 
}
