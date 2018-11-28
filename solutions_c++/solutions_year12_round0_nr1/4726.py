#include <iostream>

using namespace std;

int T;

char A[300];
char S[202];

int main() {
  cin >> T;
  cin.getline(S, 200);
  /*  char X[202], Y[202];
  for (int i=0;i<3;++i) {
    cin.getline(X, 200);
    cin.getline(Y, 200);
    cout << X << endl;
    cout << Y << endl;
    for (int i=0;X[i];++i)
      A[X[i]] = Y[i];
    for (char c = 'a'; c<='z';++c) 
      cout << "A['" << c << "'] = " << A[c] << ";" << endl;
    cout << endl;
  }*/
  A[' '] = ' ';
  A['a'] = 'y';
  A['b'] = 'h';
  A['c'] = 'e';
  A['d'] = 's';
  A['e'] = 'o';
  A['f'] = 'c';
  A['g'] = 'v';
  A['h'] = 'x';
  A['i'] = 'd';
  A['j'] = 'u';
  A['k'] = 'i';
  A['l'] = 'g';
  A['m'] = 'l';
  A['n'] = 'b';
  A['o'] = 'k';
  A['p'] = 'r';
  A['q'] = 'z';
  A['r'] = 't';
  A['s'] = 'n';
  A['t'] = 'w';
  A['u'] = 'j';
  A['v'] = 'p';
  A['w'] = 'f';
  A['x'] = 'm';
  A['y'] = 'a';
  A['z'] = 'q';
  for (int tc = 1; tc<=T;++tc) {
    cin.getline(S, 200);
    for (int i=0;S[i];++i)
      S[i] = A[S[i]];
    cout << "Case #" << tc << ": " << S << endl;
  }
  return 0;
}
