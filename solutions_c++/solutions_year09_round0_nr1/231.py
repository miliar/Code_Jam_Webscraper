#include <iostream>
using namespace std;

char words[5000][15];
bool possiblechar[26];
bool possibleword[5000];
int L,D,N;

int main(int argc, char *argv[]) {
  char ch;
  int matches;
  cin >> L >> D >> N >> ws;
  for(int i=0; i<D; i++) {
    for(int j=0; j<L; j++) {
      cin >> words[i][j] >> ws;
    }
  }

  for(int n=1; n<=N; n++) {
    for(int i=0; i<D; i++) {
      possibleword[i] = true;
    }
    for(int j=0; j<L; j++) {
      for(int i=0; i<26; i++) {
        possiblechar[i] = false;
      }
      cin >> ws >> ch;
      if (ch >= 'a' && ch <= 'z') {
        possiblechar[ch-'a'] = true;
      } else {
        while(true) {
          cin >> ws >> ch;
          if (ch == ')') break;
          possiblechar[ch-'a'] = true;
        }
      }

      for(int i=0; i<D; i++) {
        if (!possiblechar[words[i][j]-'a']) {
          possibleword[i] = false;
        }
      }
    }

    matches = 0;
    for(int i=0; i<D; i++) {
      if (possibleword[i]) {
        matches++;
      }
    }

    cout << "Case #" << n << ": " << matches << endl;
  }

  return 0;
}
