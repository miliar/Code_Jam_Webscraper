#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>

using namespace std;

struct Move {
  int pos;
  char who;
};

int getNextO(Move* array, int start, int length) {
  for (int i = start; i < length; i++) {
    if (array[i].who == 'O') return i;
  }
  return -1;
}

int getNextB(Move* array, int start, int length) {
  for (int i = start; i < length; i++) {
    if (array[i].who == 'B') return i;
  }
  return -1;
}


int main() {
  ifstream fin ("A.in");
  ofstream fout ("A.out");
  int howMany;
  fin >> howMany;
  for (int turn = 0; turn < howMany; turn++) {
    int numTurns;
    fin >> numTurns;
    Move* array = (Move*)malloc(sizeof(Move) * numTurns);
    if (array == NULL) {
      cout << "ARRAY CANNOT BE MADE!" << endl;
    }
    for (int i = 0; i < numTurns; i++) {
      fin >> array[i].who;
      fin >> array[i].pos;
    }
    int oPos = 1, bPos = 1;
    bool oButton = false;
    int seconds = 0, pos = 0;
    bool solved = false;
    //cout << getNextO(array, 1, numTurns);
    while(!solved) {
      //Handle What O Should do
      oButton = false;
      int nextO = getNextO(array, pos, numTurns);
      if (nextO == -1) {
        // No more moves for O
      }
      else if (oPos == array[nextO].pos) {
        if (array[pos].who == 'O') {
          oButton = true;
          pos++;
          //Orange Just Went!
        }
        else {
          //Orange is waiting
        }
      }
      else {
        if (oPos > array[nextO].pos) oPos--;
        else oPos++;
      }

      //NOW TIME FOR BLUE
      int nextB = getNextB(array, pos, numTurns);
      if (nextB == -1) {
        //Blue cant go
      }
      else if (bPos == array[nextB].pos) {
        if (array[pos].who == 'B') {
          if (oButton == false) {
            //Blue Pushes!
            pos++;
          }
        }
        else {
          //Idle
        }
      }
      else {
        if (bPos > array[nextB].pos) bPos--;
        else bPos++;
      }

      seconds++;
      if (pos == numTurns) break;
      /**
      oButton = false, bButton = false;
      char whoNeedsToGo = array[pos].who;
      int toWhere = array[pos].pos;
      int nextO = getNextO(array, pos, numTurns);
      if (nextO == -1) {
        cout << "odone" << endl;
        //O is done, remain idle
      }
      else if (oPos == array[nextO].pos) {
        cout << "yes!" << endl;
        if (whoNeedsToGo == 'O') {
          //Orange Goes!
          oButton = true;
          pos++;
        }
        else {
          //Just remain idle
        }
      }
      else {
        oPos++;
      }
      if (pos == numTurns) break;
      whoNeedsToGo = array[pos].who;
      toWhere = array[pos].pos;
      int nextB = getNextB(array, pos, numTurns);
      if (nextB == -1) {
        //B is done, remain idle
      }
      else if (bPos == array[nextB].pos) {
        if (whoNeedsToGo == 'B') {
          if (oButton == false) {
            pos++;
            bButton = true;
            cout << "blue hit" << endl;
          }
          else {
            //Orange is pushing, must wait
          }
        }
        else {
          //just reamin idle
        }
      }
      else {
        bPos++;
      }
      seconds++;
      if (pos == numTurns) solved = true;
      cout << oPos << ' ' << bPos << whoNeedsToGo << getNextB(array, pos, numTurns) << ' ' << pos << endl;
      **/
      /*****
      if (whoNeedsToGo == 'O') {
        if (oPos == toWhere) {
          //Press button
        }
        else oPos++;
        if (bPos == getNextB(array, pos, numTurns)) {
          //wait
        }
        else bPos++;
      }
      else if (whoNeedsToGo == 'B') {
        if (bPos == toWhere) {
          //Press button
        }
        else bPos++;
        if (oPos == getNextO(array, pos, numTurns)) {
          //wait
        }
        else oPos++;
      }
      else cout << "who goes?" << endl;
      if (pos == (numTurns-1)) {
        solved = true;
      }
      seconds++;
      ***/
    }
    fout << "Case #" << turn + 1 << ": " << seconds << endl;
  }
}
