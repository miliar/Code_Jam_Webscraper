#include <iostream>
#include <string>
//#include <map>

using namespace std;

int main() {
  char dictionary[256];
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    string alien;
    int base = 2;
    long long int answer = 0;
    //map<char, int> dictionary;
    char dictionary[256];
    memset(dictionary, 80, 256);

    bool got_zero = false;

    cin >> alien;
    dictionary[alien[0]] = 1;
    
    for (int j = 1; j < alien.length(); j++) {
      //if (dictionary.find(alien[j]) == dictionary.end()) {
      if (!got_zero && dictionary[alien[j]] > 62) {
        dictionary[alien[j]] = 0;
        got_zero = true;
      } else if (dictionary[alien[j]] > 62) {
        dictionary[alien[j]] = base++;
      }
    }

    for (int j = 0; j < alien.length(); j++) {
      answer *= base;
      answer += dictionary[alien[j]];
    }

    cout << "Case #" << i+1 << ": " << answer << endl;
  }
}
