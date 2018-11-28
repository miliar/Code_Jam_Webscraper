#include <cstdio>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
using namespace std;

vector<int> bases;

string dec_to_base(int number, int base) {
  string res;
  if (number == 0) return "0";
  while (number > 0) {
    res += char(number % base + '0');
    number /= base;
  }
  return res;
}

int base_to_dec(string& number, int base) {
  int res = 0;
  for (char *d = (char*)number.c_str(); *d != '\0'; ++d) {
    res = res * base + int(*d - '0');
  }
  return res;
}

bool is_happy_in_base(int number, int base) {
  set<int> old;
  while (number != 1) {
    if (old.find(number) != old.end()) return false;
    old.insert(number);
    string str_number = dec_to_base(number, base);
    number = 0;
    for (char *d = (char*)str_number.c_str(); *d != '\0'; ++d) {
      number += int(*d - '0') * int(*d - '0');
    }
  }
  return true;
}

int main() {
  int n_tests;
  char line[1<<10];

  scanf("%d", &n_tests);
  for (int test = 1; test <= n_tests; ++test) {

    scanf(" %[^\n]", line);

    bases.clear();
    stringstream ss(line);
    for (int b; ss >> b; ) {
      bases.push_back(b);
    }

    int res = 2;
    for (;;++res) {
      bool ok = true;
      for (int i = 0; i < bases.size(); ++i) {
        if (!is_happy_in_base(res, bases[i])) {
          ok = false;
          break;
        }
      }
      if (ok) {
        break;
      }
    }

    printf("Case #%d: %d\n", test, res);
  }
  return 0;
}
