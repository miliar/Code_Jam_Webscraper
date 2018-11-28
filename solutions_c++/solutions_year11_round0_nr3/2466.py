#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main() {
  ifstream fin ("C.in");
  ofstream fout ("C.out");

  int numTimes;
  fin >> numTimes;
  for (int turn = 0; turn < numTimes; turn++) {
    int n;
    fin >> n;
    int* array = (int*)malloc(sizeof(int) * n);
    if (array == NULL) {
      cout << "oh shit, cant make array!" << endl;
    }
    for (int i = 0; i < n; i++) {
      fin >> array[i];
    }
    int bestNum = 0;
    int bestValue = 0;
    for (int i = 0; i < n; i++) {
      int xorSum = 0;
      int Sum = 0;
      for (int j = 0; j < n; j++) {
        if (j == i) continue;
        xorSum = xorSum^array[j];
        Sum += array[j];
      }
      if (xorSum == array[i]) {
        if (Sum > bestValue) {
          bestValue = Sum;
          bestNum = array[i];
        }
        else if (Sum == bestValue) {
          if (array[i] < bestNum) {
            bestNum = array[i];
          }
        }
      }
    }
    //All Done, see if any
    fout << "Case #" << turn + 1 << ": ";
    if (bestNum == 0) fout << "NO" << endl;
    else fout << bestValue << endl;
    free(array);
  }
}
