#include <stdio.h>
#include <iostream>
#include <string>

std::string wel = "welcome to code jam";
int cache[600][20];

int calculate(std::string& s, int n1, int n2) {
  if (n2 >= wel.length()) {
    return 1;
  }
  if (n1 >= s.length()) {
    return 0;
  }
  if (s.length() - n1 < wel.length() - n2) {
    return 0;
  }
  if (cache[n1][n2] != -1) {
    return cache[n1][n2];
  }
  int num = 0;
  int pos = n1;
  while(true) {
    pos = s.find(wel[n2], pos);
    if (pos == std::string::npos) {
      break;
    }
    num += calculate(s, pos+1, n2+1);
    pos++;
  }
  if (cache[n1][n2] == -1) {
    cache[n1][n2] = num % 10000;
  }
  return cache[n1][n2];
}

int main() {
  int N;
  std::string s;
  std::cin >> N;
  getline(std::cin, s);
  int i;
  FILE *out = fopen("out.txt", "w");
  for (i = 0; i < N; i++) {
    for (int j = 0; j < 600; j++) {
      for (int k = 0; k < 20; k++) {
        cache[j][k] = -1;
      }
    }
    getline(std::cin, s);
    int num = calculate(s, 0, 0);
    char tmp[10];
    sprintf(tmp, "%d", num);
    string tmp2(tmp);
    fprintf(out, "Case #%d: ", i + 1);
    for (int j = 0; j < 4-tmp2.length(); j++) {
      fprintf(out, "0");
    }
    fprintf(out, "%d\n", num);
  }
  fclose(out);
  return 0;
}
