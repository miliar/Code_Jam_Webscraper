#include <iostream>
#include <string>

using namespace std;

char translate(char);

int main() {
  string message;
  string translation;
  int numCases = 0;

  cin >> numCases;
  cin.ignore(80, '\n');

  for (int i =0; i < numCases; i++) {
    message.clear();
    translation.clear();
    getline(cin, message);
    translation.resize(message.length());
    for (int j = 0; j < message.length(); j++) {
      translation[j] = translate(message[j]);
    }
    cout << "Case #" << i+1;
    cout << ": " << translation << endl;
  }
  return 0;
}

char translate(char in) {
  static char trans[] = "yhesocvxduiglbkrztnwjpfmaq";
  char out = '0';
  if (in == ' ') return in;
  return trans[(int) (in - 97)];
}
