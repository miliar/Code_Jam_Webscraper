#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("C-small.in");
ofstream fout("C-small.out");

int main() {
  long long num;
  long long times;
  long long max;
  long long noobs;
  fin >> num;
  for (int i = 0; i < num; i++) {
    fin >> times >> max >> noobs;
    long long nooblist[noobs];
    long long dollahs = 0;
    long long index = 0;
    long long curspace;
    long long counter = 0;
    for (int j = 0; j < noobs; j++) {
      fin >> nooblist[j];
    }
    for (int j = 0; j < times; j++) {
      curspace = max;
      counter = 0;
      while (curspace > 0 && counter < noobs) {
        if (nooblist[index % noobs] <= curspace) {
          dollahs += nooblist[index % noobs];
          curspace -= nooblist[index % noobs];
          counter++;
          index++;
        }
        else {
          curspace = 0;
        }
      }
    }
    fout << "Case #" << i+1 << ": " << dollahs << endl;
  }
  return 0;
}
