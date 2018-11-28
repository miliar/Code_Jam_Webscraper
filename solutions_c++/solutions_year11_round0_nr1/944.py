#include <cstdio>
#include <vector>

using namespace std;

int N;
vector<int> buttonO, buttonB, orderO, orderB;

int countMoves () {
  int i = 0, posO = 1, posB = 1, commandO = 0, commandB = 0, turn = 0, count = 0, changeTurn = 0;
  while (i < N) {
    if (commandO < buttonO.size() && buttonO[commandO] == posO && turn == orderO[commandO]) {
      //printf ("O apertou o botao\n");
      changeTurn = 1;
      commandO++;
      i++;
    }
    else if (buttonO[commandO] > posO) {
      //printf ("O andou pra frente\n");
      posO++;
    }
    else if (buttonO[commandO] < posO)
      posO--;
    
    if (commandB < buttonB.size() && buttonB[commandB] == posB && turn == orderB[commandB]) {
      //printf ("B apertou o botao\n");
      changeTurn = 1;
      commandB++;
      i++;
    }
    else if (buttonB[commandB] > posB) {
      //printf ("B andou pra frente\n");
      posB++;
    }
    else if (buttonB[commandB] < posB)
      posB--;
    if (changeTurn == 1) {
      changeTurn = 0;
      turn++;
    }
    count++;
  }
  return count;
}
    
int main () {
  int T;
  scanf ("%d", &T);
  
  for (int t = 1; t <= T; t++) {
    scanf ("%d", &N);
    getc(stdin);
    
    buttonO = vector<int> ();
    buttonB = vector<int> ();
    orderO = vector<int> ();
    orderB = vector<int> ();
    
    for (int i = 0; i < N; i++) {
      int p;
      char r;
      scanf ("%c%d", &r, &p);
      getc(stdin);
      if (r == 'O') {
        buttonO.push_back(p);
        orderO.push_back(i);
      }
      else {
        buttonB.push_back(p);
        orderB.push_back(i);
      }
      //printf ("%c %d\n", r, p);
    }
    int c = countMoves ();
    printf ("Case #%d: %d\n", t, c);
  }
  return 0;
}
