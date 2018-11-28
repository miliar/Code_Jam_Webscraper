#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;
ifstream fin("B-small.in");
ofstream fout("B-small.out");

int main() {
  int cases;
  fin >> cases;
  char number[30];
  char track[30];
  for (int i = 0; i < cases; i++) {
    int j;
    fin >> number;
    int len = strlen(number);
    for (j = 0; j < len; j++) {
      track[j] = number[j];
    }
    sort(track, track + len);
    next_permutation(number, number + len);
    for (j = 0; j < len; j++) {
      if (track[j] != number[j]) break;
      track[j] = number[j];
    }
    if (j != len) {
      fout << "Case #" << i+1 << ": " << number << endl;
    } else {
      while (number[0] == '0')
        next_permutation(number, number + len);
      fout << "Case #" << i+1 << ": " << number[0] << "0";
      for (int k = 1; k < len; k++) {
        fout << number[k];
      }
      fout << endl;
    }
  }
  return 0;
}

