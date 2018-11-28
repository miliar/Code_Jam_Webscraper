#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;

struct transf {
  char c[2];
  char res;
};

struct oppos {
  char c[2];
};

int equals(transf tr, char c1, char c2) {
  if ((tr.c[0] == c1 && tr.c[1] == c2) || (tr.c[0] == c2 && tr.c[1] == c1)) {
    return 1;
  }
  return 0;
}



int combine(char result[], int &offset, char cc, int c, transf tr[], int d, oppos op[]) {
  if (offset == -1) return 0;
  for (int i = 0; i < c; i++) {
    if (equals(tr[i], result[offset], cc)) {
      // Yes, this is a valid combination!
      result[offset] = tr[i].res;
      return 1;
    }
  }
  return 0;
}

int isOp(char cc1, char cc2, int d, oppos op) {
  if ((op.c[0] == cc1 && op.c[1] == cc2) || (op.c[0] == cc2 && op.c[1] ==cc1)) {
    return 1;
  }
  return 0;
}

int opposites(char result[], int &offset, char cc, int c, transf tr[], int d, oppos op[]) {
  if (offset == -1) return 0;
  for (int j = 0; j <= offset; j++) {
    for (int i = 0; i < d; i++) {
      if (isOp(cc, result[j], d, op[i])) {
        offset = -1;
        return 1;
      }
    }
  }
  return 0;
}

char *solve(int c, transf tr[], int d, oppos op[], int len, char seq[]) {

  char *result = new char[50000];
  int offset = 0;
  result[0] = seq[0];
  result[offset + 1] = '\0';
  for (int i = 1; i < len; i++) {
    int resu = combine(result, offset, seq[i], c, tr, d, op);
    if (resu == 0) {
      // No combination?
      // try opposites.
      resu = opposites(result, offset, seq[i], c, tr, d, op);
      if (resu == 0) {
        result[++offset] = seq[i];
      }
    }
    result[offset + 1] = '\0';
  }
  result[offset + 1] = '\0';

  return result;
}

int main() {

  ifstream f("mag.in");  
  ofstream g("mag.out");

  int t, c, d, len;
  f >> t;
  
  for (int i = 0; i < t; i++) {
    f >> c;
    transf tr[5000];
    for (int j = 0; j < c; j++) {
      char cc1, cc2, cc3;
      f >> cc1 >> cc2 >> cc3;
      tr[j].c[0] = cc1;
      tr[j].c[1] = cc2;
      tr[j].res = cc3;
    }
    f >> d;
    oppos op[5000];
    for (int j = 0; j < d; j++) {
      char cc1, cc2;
      f >> cc1 >> cc2;
      op[j].c[0] = cc1;
      op[j].c[1] = cc2;      
    }
    f >> len;
    char seq[5000];
    for (int j = 0; j < len; j++) {
      char cc;
      f >> cc;
      seq[j] = cc;
    }
    char *res = solve(c, tr, d, op, len, seq);
    g << "Case #" << i + 1 << ": [";
    if (strlen(res) > 0) g << res[0];
    for (int j = 1; j < strlen(res); j++) {
      g << ", " << res[j];
    }
    g << "]" << endl;
  }
  
  f.close();
  g.close();

  return 0;
}

