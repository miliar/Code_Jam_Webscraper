#include <iostream>
#include <fstream>

using namespace std;

char translateSingleChar(char in) {
  switch (in) {
    case 'y': return 'a';
    case 'n': return 'b';
    case 'f': return 'c';
    case 'i': return 'd';
    case 'c': return 'e';
    case 'w': return 'f';
    case 'l': return 'g';
    case 'b': return 'h';
    case 'k': return 'i';
    case 'u': return 'j';
    case 'o': return 'k';
    case 'm': return 'l';
    case 'x': return 'm';
    case 's': return 'n';
    case 'e': return 'o';
    case 'v': return 'p';
    case 'z': return 'q';
    case 'p': return 'r';
    case 'd': return 's';
    case 'r': return 't';
    case 'j': return 'u';
    case 'g': return 'v';
    case 't': return 'w';
    case 'h': return 'x';
    case 'a': return 'y';
    case 'q': return 'z';
    default: return ' ';
  }
}

int main() {
  ifstream input("A-small-attempt0.in", ifstream::in);
  ofstream output("problem-a.out", ofstream::out);

  char buffer[8*1024];
  int caseCount;
  input >> caseCount;
  input.getline(buffer, 4);

  for (int caseId = 1; caseId <= caseCount; ++caseId) {
    input.getline(buffer, 8*1024);

    output << "Case #" << caseId << ": ";

    for (int i = 0; i < strlen(buffer); ++i) {
      output << translateSingleChar(buffer[i]);
    }

    output << endl;
  }


}