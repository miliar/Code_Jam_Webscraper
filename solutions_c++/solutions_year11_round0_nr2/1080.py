#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

int charCount[26];
vector<char> status;

char combineTable[26][26]; // '.' = "not combinable"
bool conflictTable[26][26]; // true = "conflict"

void eraseStack() {
  status.clear();
  for (int i = 0; i<26; i++) {
    charCount[i] = 0;
  }
}

void initialize() {
  for (int i = 0; i <26; i++) {
     for (int j = 0; j<26; j++) {
      combineTable[i][j] = '.';
      conflictTable[i][j] = false;
    }
  }
  eraseStack();
}

void add2Stack(char next) {
  status.push_back(next);
  charCount[next-'A']++;
}

void removeLast() {
  char last = status.back();
  charCount[last-'A']--;
  status.pop_back();
}

bool isConflict(char c) {
  for (int i = 0; i< 26; i++) {
    if (charCount[i] > 0 && conflictTable[i][c-'A']) {
      return true;
    }
  }
  return false;
}

int main() {
  int T;
  cin >> T;

  int C, D, N;
  for (int t = 1; t<=T; t++) {
    initialize();
    // read combine table
    cin >> C;
    for (int j = 0; j<C; j++) {
      char B1, B2, R;
      cin >> B1 >> B2 >> R;
      B1 = toupper(B1);
      B2 = toupper(B2);
      combineTable[B1-'A'][B2-'A'] = toupper(R);
      combineTable[B2-'A'][B1-'A'] = toupper(R);
    }
    // read comflict table
    cin >> D;
    for (int j = 0; j < D; j++) {
      char B1, B2;
      cin >> B1 >> B2;
      B1 = toupper(B1);
      B2 = toupper(B2);
      conflictTable[B1-'A'][B2-'A'] = conflictTable[B2-'A'][B1-'A'] = true;
    }
    // process sequence
    cin >> N;
    char next;
    for (int j = 0; j<N; j++) {
      cin >> next;
      int nextIdx = toupper(next)-'A';
      // case 1. stack is empty, add next to stack
      if (status.empty()) {
        //        cout << "  case 1: adding " << next << endl;
        add2Stack(next);
        continue;
      }
      // case 2. can be combined with last one
      char lastone = status.back();
      char combined = combineTable[nextIdx][lastone-'A'];
      //      cout << "   combined = " << combined << endl;
      if (combined != '.') {
        //        cout << "  case 2: replacing "<< lastone << " with " << combined << endl;
        removeLast();
        add2Stack(combined);
        continue;
      }

      // case 3. if next is conflict with last one
      if (isConflict(next)) {
        //        cout << "  case 3: conflict. Clear stack\n";
        eraseStack();
        continue;
      }

      // case 4. add next to stack
      add2Stack(next);
      //      cout << "  case 4: JUST ADD TO STACK -- " << next << endl;
    }

    // print out result
    cout << "Case #" << t << ": [";
    if (status.empty()) {
      cout << "]" << endl;
    } else {
      cout << status[0];
      for (int j = 1; j<status.size(); j++) {
        cout << ", " << status[j];
      }
      cout << "]" << endl;
    }
  }
}
      








