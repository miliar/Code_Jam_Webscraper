#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string replaceAll(string input) {
  replace(input.begin(), input.end(), 'a', 'Y');
  replace(input.begin(), input.end(), 'b', 'H');
  replace(input.begin(), input.end(), 'c', 'E');
  replace(input.begin(), input.end(), 'd', 'S');
  replace(input.begin(), input.end(), 'e', 'O');
  replace(input.begin(), input.end(), 'f', 'C');
  replace(input.begin(), input.end(), 'g', 'V');
  replace(input.begin(), input.end(), 'h', 'X');
  replace(input.begin(), input.end(), 'i', 'D');
  replace(input.begin(), input.end(), 'j', 'U');
  replace(input.begin(), input.end(), 'k', 'I');
  replace(input.begin(), input.end(), 'l', 'G');
  replace(input.begin(), input.end(), 'm', 'L');
  replace(input.begin(), input.end(), 'n', 'B');
  replace(input.begin(), input.end(), 'o', 'K');
  replace(input.begin(), input.end(), 'p', 'R');
  replace(input.begin(), input.end(), 'q', 'Z');
  replace(input.begin(), input.end(), 'r', 'T');
  replace(input.begin(), input.end(), 's', 'N');
  replace(input.begin(), input.end(), 't', 'W');
  replace(input.begin(), input.end(), 'u', 'J');
  replace(input.begin(), input.end(), 'v', 'P');
  replace(input.begin(), input.end(), 'w', 'F');
  replace(input.begin(), input.end(), 'x', 'M');
  replace(input.begin(), input.end(), 'y', 'A');
  replace(input.begin(), input.end(), 'z', 'Q');
  transform(input.begin(), input.end(), input.begin(), ::tolower);
  return input;
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 0;i <= T; ++i) {
    string str;
    getline(cin, str);
    if (i == 0) continue;
    str = replaceAll(str);
    cout << "Case #" << i << ": " << str << endl;
  }
  return 0;
}
