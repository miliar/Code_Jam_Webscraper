// run cat in | qra
#include <iostream>
using namespace std;
int debug = 0;

int main(int argc, const char *argv[]) {
  int Tc = 0;
  char l[4][4];
  // read the number of test cases
  cin >> Tc;
  if (debug == 1) {
    cout << Tc <<  endl;
  }
  for (int k=0; k<Tc; k++) {
    cout << "Case #" << k+1 << ": ";
    if (debug == 1) {
      cout << endl;
    }
    cin >> l[0];
    cin >> l[1];
    cin >> l[2];
    cin >> l[3];
    //row count
    int X, O, T, P, Pt, done;
    Pt = 0;
    done = 0;
    for (int i = 0; i < 4; i++) {
      X=0;
      O=0;
      T=0;
      P=0;
      for (int j = 0; j < 4; j++) {
	if (debug == 1) {
	  cout << l[i][j];
	}
	if (l[i][j] == 'X') X++;
	if (l[i][j] == 'O') O++;
	if (l[i][j] == 'T') T++;
	if (l[i][j] == '.') P++;
      }
      Pt += X + O + T;
      if (debug == 1) {
	cout << "  X:" << X << " O:" << O << " T:" << T << " P:" << P << endl;
      }
      if ((done == 0) && (X+T == 4)) {
	cout << "X won" << endl;
	done = 1;
      }
      if ((done == 0) && (O+T == 4)) {
	cout << "O won" << endl;
	done = 1;
      }
    }
    if (debug == 1) {
      cout << endl;
    }
    //column count
    for (int j = 0; j < 4; j++){
      X=0;
      O=0;
      T=0;
      P=0;
      for (int i = 0; i < 4; i++) {
	if (debug == 1) {
	  cout << l[i][j];
	}
	if (l[i][j] == 'X') X++;
	if (l[i][j] == 'O') O++;
	if (l[i][j] == 'T') T++;
	if (l[i][j] == '.') P++;
      }
      if (debug == 1) {
	cout << "  X:" << X << " O:" << O << " T:" << T << " P:" << P << endl;
      }
      if ((done == 0) && (X+T == 4)) {
	cout << "X won" << endl;
	done = 1;
      }
      if ((done == 0) && (O+T == 4)) {
	cout << "O won" << endl;
	done = 1;
      }
    }
    if (debug == 1) {
      cout << endl;
    }
    //diagnal count
    X=0;
    O=0;
    T=0;
    P=0;
    for (int i = 0; i < 4; i++) {
      if (debug == 1) {
	cout << l[i][i];
      }
      if (l[i][i] == 'X') X++;
      if (l[i][i] == 'O') O++;
      if (l[i][i] == 'T') T++;
      if (l[i][i] == '.') P++;
    }
    if (debug == 1) {
      cout << "  X:" << X << " O:" << O << " T:" << T << " P:" << P << endl;
    }
    if ((done == 0) && (X+T == 4)) {
      cout << "X won" << endl;
      done = 1;
    }
    if ((done == 0) && (O+T == 4)) {
      cout << "O won" << endl;
      done = 1;
    }
    if (debug == 1) {
      cout << endl;
    }
    //reverse diagnal count
    X=0;
    O=0;
    T=0;
    P=0;
    for (int i = 0; i < 4; i++) {
      if (debug == 1) {
	cout << l[3-i][i];
      }
      if (l[3-i][i] == 'X') X++;
      if (l[3-i][i] == 'O') O++;
      if (l[3-i][i] == 'T') T++;
      if (l[3-i][i] == '.') P++;
    }
    if (debug == 1) {
      cout << "  X:" << X << " O:" << O << " T:" << T << " P:" << P << endl;
    }
    if ((done == 0) && (X+T == 4)) {
      cout << "X won" << endl;
      done = 1;
    }
    if ((done == 0) && (O+T == 4)) {
      cout << "O won" << endl;
      done = 1;
    }
    if ((done == 0) && (Pt == 16 )) {
      cout << "Draw" << endl;
      done = 1;
    }
    if (done == 0) {
      cout << "Game has not completed" << endl;
      if (debug == 1) {
	cout << endl;
	cout << "k=" << k << endl;
      }
    }
  }
  return 0;

}
