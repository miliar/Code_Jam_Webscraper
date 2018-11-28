#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int f(string text, int m, int n, string str, int left, int right);

int main() {
  int N;
  cin >> N;
  const string str("welcome to code jam");

  string tmp;
  getline(cin, tmp);

  for (int test_case = 1; test_case <= N; test_case++) { 
    string text;
    getline(cin, text);
    cout << "Case #" << test_case << ": ";
    int count = f(text, 0, text.size(), str, 0, 19);

    std::stringstream ss;
    std::string s;
    ss << count+10000;
    s = ss.str();

    cout << s.substr(1,4) << endl;
  }
}

int f(string text, int m, int n, string str, int left, int right) {
  if (n-m == right-left)
    if (text.find(str.substr(left, right-left), m) == m) 
      return 1;
    else
      return 0;

  if (n-m < right-left)
    return 0;

  int a, b;
  a = f(text, m+1, n, str, left, right);

  if (text[m] == str[left])
    b = f(text, m+1, n, str, left+1, right);
  else
    b = 0;

  return (a+b)%10000;
}
