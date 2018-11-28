#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;

const string phrase = "welcome to code jam";

void update(string &text, VI &num, int L, char c) {
  int old = num[L], running = 0; num[L] = 0;
  for (int i = L-1; i >= 0; --i) {
    if (text[i] == c) {
      running += old; running %= 10000;
      }
    old = num[i]; num[i] = running;
    }
  }

int main() {
  int N; cin >> N; cin.ignore();
  for (int c = 1; c <= N; ++c) {
    string text; getline(cin, text);
    int L = text.size(); VI num(L+1,1);
    for (string::const_reverse_iterator i = phrase.rbegin(); i != phrase.rend(); ++i)
      update(text, num, L, *i);
    cout << "Case #" << c << ": " << setw(4) << setfill('0') << num[0] << '\n';
    }
  }