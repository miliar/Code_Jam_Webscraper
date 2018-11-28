#include <iostream>

using namespace std;

int main() {
  int cases, googlers, surprises, at_least, note, resposta;

  cin >> cases;
  for (int i = 0; i < cases; i++) {
    resposta = 0;
    cin >> googlers >> surprises >> at_least;
    for (int j = 0; j < googlers; j++) {
      cin >> note;
      note -= at_least;
      if (note < 0) continue;
      if ((at_least - 1) * 2 <= note) {
        resposta++;
      }
      else if ((at_least - 2) * 2 <= note && surprises) {
        resposta++;
        surprises--;
      }
    }
    cout << "Case #" << i + 1 << ": " << resposta << endl;
  }
}
