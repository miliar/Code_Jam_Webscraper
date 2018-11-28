#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <stdlib.h>

using namespace std;

bool contains(vector<char> array, char value) {
  for (int i = 0; i < array.size(); i++) {
    if (array[i] == value) return true;
  }
  return false;
}

int main() {
  ifstream fin ("B.in");
  ofstream fout ("B.out");
  int numTimes;
  fin >> numTimes;

  for (int turn = 0; turn < numTimes; turn++) {
    int C, D, N;
    fin >> C;
    char** cList = (char**)malloc(C * sizeof(int *));
    for (int i = 0; i < C; i++) {
      cList[i] = (char*)malloc(3 * sizeof(int));
      string temp;
      fin >> temp;
      cList[i][0] = temp[0];
      cList[i][1] = temp[1];
      cList[i][2] = temp[2];

    }
    fin >> D;
    char** dList = (char**)malloc(D * sizeof(int *));
    for (int i = 0; i < D; i++) {
      dList[i] = (char*)malloc(2 * sizeof(int));
      string temp;
      fin >> temp;
      dList[i][0] = temp[0];
      dList[i][1] = temp[1];
    }
    vector<char> list;
    fin >> N;
    string input;
    fin >> input;

    //BEGIN!
    list.push_back(input[0]);
    bool change = false;
    for (int i = 1; i < N; i++) {
      change = false;
      char prev = list[list.size() - 1];
      char now = input[i];
      //loop thorugh each pair to see if need to replace
      for (int tC = 0; tC < C; tC++) {
        if ((cList[tC][0] == prev) && (cList[tC][1] == now)) {
          list.pop_back();
          list.push_back(cList[tC][2]);
          change = true;
          break;
        }
        else if ((cList[tC][0] == now) && (cList[tC][1] == prev)) {
          list.pop_back();
          list.push_back(cList[tC][2]);
          change = true;
          break;
        }
      }

      //check if pair is not allowed
      for (int tD = 0; tD < D; tD++) {
        if (change) break;
        if (dList[tD][0] == now) {
          char cannot = dList[tD][1];
          if (contains(list, cannot)) {
            list.clear();
            change = true;
            break;
          }
        }
        else if (dList[tD][1] == now) {
          char cannot = dList[tD][0];
          if (contains(list, cannot)) {
            list.clear();
            change = true;
            break;
          }
        }
      }
      if (!change) list.push_back(now);
    }

    //Now Print!
    fout << "Case #" << turn + 1 << ": [";
    for (int i = 0; i < list.size(); i++) {
      fout << list[i];
      if (i == list.size() - 1) fout << "]";
      else fout << ", ";
    }
    if (list.size() == 0) fout << "]";
    fout << endl;
    free(cList);
    free(dList);
  }
}
