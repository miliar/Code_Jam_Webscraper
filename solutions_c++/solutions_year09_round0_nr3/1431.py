#include <cstdio>
#include <string>
#include <iostream>

std::string welcome = "welcome to code jam";
int answer[19], temp[19];
int N;

int main() {
  std::cin >> N;
  scanf("\n");
  for(int i = 0; i < N; ++i) {
    std::string s;
    char sym, result;
    scanf("%c", &sym);
    while (sym != '\n' && result != EOF) {
      s += sym;
      result = scanf("%c", &sym);
    }
    //std::cout << s;
    memset(answer, 0, sizeof(answer));
    for(int j = 0; j < s.size(); ++j) {
      memcpy(temp, answer, sizeof(answer));
      if (s[j] == 'w') {
        answer[0]++;
      }
      for(int k = 1; k < welcome.size(); ++k) {
        if (s[j] == welcome[k]) {
          //std::cout << i << j << k << std::endl;
          answer[k] += temp[k - 1];
          answer[k] %= 10000;
        }
      }
    }
    std::cout << "Case #" << i + 1 << ": ";
    if (answer[18] < 10) {
      std::cout << "0";
    }
    if (answer[18] < 100) {
      std::cout << "0";
    }
    if (answer[18] < 1000) {
      std::cout << "0";
    }
    std::cout << answer[18] << std::endl;
  }
}