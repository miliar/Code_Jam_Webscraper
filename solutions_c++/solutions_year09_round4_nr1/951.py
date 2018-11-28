#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int last1In(string arg) {
  for(int i = arg.size()-1; i >= 0; i--)
    if(arg[i] == '1')
      return i;
  return -1;
}

void swap(int *ar, string *str, int i, int j, int &counter) {
  int itmp = ar[i];
  ar[i] = ar[j];
  ar[j] = itmp;

  string strtmp = str[i];
  str[i] = str[j];
  str[j] = strtmp;

  counter++;
  return;
}

int main(int argc, char **argv) {
  ifstream fin(argv[1]);
  ofstream fout(argv[2]);

  int numCases;
  fin >> numCases;

  for(int caseNum = 1; caseNum <= numCases; caseNum++) {
    int size;
    fin >> size;

    int lasts[size];
    string strs[size];
    
    for(int i = 0; i < size; i++) {
      string s;
      fin >> s;
      lasts[i] = last1In(s);
      strs[i] = s;
    }

    int counter = 0;

    for(int j = 0; j < size; j++) {
      for(int i = j; i < size; i++) {
	if(lasts[i] <= j) {
	  for(int k = i; k > j; k--)
	    swap(lasts, strs, k, k-1, counter);
	  i = size;
	}
      }
    }

    fout << "Case #" << caseNum << ": " << counter << "\n";
    cout << "Case #" << caseNum << ": " << counter << "\n";
  }
}

//for all i, a[i] <= i
