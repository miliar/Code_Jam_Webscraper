#include <iostream>
#include <string>
#include <set>
#include <cstring>
#include <cstdio>

using namespace std;

const char* welcome = "welcome to code jam";


int find(const char* line) {
  int index[strlen(line)];
  int count;

  for (size_t i = 0; i < strlen(line); i++)
    if (line[i] == welcome[strlen(welcome) - 1])
      index[i] = 1;
    else
      index[i] = 0;

  for (int i = (int) strlen(welcome) - 2; i >= 0; i--) {
    char pre = welcome[i + 1];
    char cur = welcome[i];

    count = 0;
    for (int j = (int) strlen(line) - 1; j >= 0; j--) {
      if (line[j] == pre) {
        count += index[j];
        count %= 10000;
      }
      else if (line[j] == cur) {
        index[j] = count;
      }
    }
  }

  count = 0;
  for (size_t i = 0; i < strlen(line); i++) {
    if (line[i] == welcome[0]) {
      count += index[i];
      count %= 10000;
    }
  }

  return count;
}

int main() {
  int N;
  string buf;

  cin >> N;
  getline(cin, buf);

  for (int i = 1; i <= N; i++) {

    getline(cin, buf);

    int res = find(buf.c_str());
    printf("Case #%d: %.4d\n", i, res);
  }

  
  return 0;
}
