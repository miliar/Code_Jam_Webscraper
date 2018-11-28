#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;
ifstream fin("C-small.in");
ofstream fout("C-small.out");

unsigned long long dparray[501][19];
string base = "welcome to code jam";

int main() {
    int cases;
    char process[501];
    fin >> cases;
    fin.getline(process, 501);
    for (int i=0;i<cases;i++) {
      unsigned long long answer = 0;
      char finalanswer[5];
      fin.getline(process, 501);
      for (int j=0;j<strlen(process);j++) {
        for (int k=0;k<19;k++) {
          dparray[j][k] = 0;
        }
        if (process[j] == 'w') {
          dparray[j][0] = 1;
        } else {
          for (int k=1;k<base.length();k++) {
            if (process[j] == base[k]) {
              for (int l=0;l<j;l++) {
                dparray[j][k]+=dparray[l][k-1];
              }
            }
          }
          answer+=dparray[j][18];
        }
      }
      sprintf(finalanswer, "%.4lld", answer % 10000);
      fout << "Case #" << i+1 << ": " << finalanswer << endl;
    }
    return 0;
}

