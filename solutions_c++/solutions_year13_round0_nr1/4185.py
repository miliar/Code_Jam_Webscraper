#include<cstdio>
#include<cstdlib>
#include<string>
#include<vector>
#include<iostream>
using namespace std;

int main() {
  int TCn;
  char m[4][4];
  int x,o,t;
  bool pts = false;
  scanf("%d%*c", &TCn);

  //casos de teste
  for (int TC = 1; TC <=TCn; ++TC) {
    cout << "Case #" << TC << ": ";
    pts = false;

    //leitura
    for (int i = 0; i < 4; ++i) {
      scanf("%s%*c",m[i]);
    } 

    //percorrer horizontalmente
    for (int i = 0; i < 4; ++i) {
      x = o = t = 0;
      for (int j = 0; j < 4; ++j) {
	switch(m[i][j]) {
	case '.':
	  pts = true;
	  break;
	case 'X':
	  ++x;
	  break;
	case 'O':
	  ++o;
	  break;
	case 'T':
	  ++t;
	  break;
	}
      }
      if (x == 4 || (x==3 && t==1)) {
	cout << "X won" << endl;
	goto final;
      }
      else if (o == 4 || (o==3 && t==1)) {
	cout << "O won" << endl;
	goto final;
      }
    }
    //percorrer verticalmente
    for (int i = 0; i < 4; ++i) {
      x = o = t = 0;
      for (int j = 0; j < 4; ++j) {
	switch(m[j][i]) {
	case '.':
	  pts = true;
	  break;
	case 'X':
	  ++x;
	  break;
	case 'O':
	  ++o;
	  break;
	case 'T':
	  ++t;
	  break;
	}
      }
      if (x == 4 || (x==3 && t==1)) {
	cout << "X won" << endl;
	goto final;
      } else if (o == 4 || (o==3 && t==1)){
	cout << "O won" << endl;
	goto final;
      }
    }

    //percorrer diagonal
    x = o = t = 0;
    for (int i = 0; i < 4; ++i) {
      switch(m[i][i]) {
      case '.':
	pts = true;
	break;
      case 'X':
	++x;
	break;
      case 'O':
	++o;
	break;
      case 'T':
	++t;
	break;
      }
      if (x == 4 || (x==3 && t==1)) {
	cout << "X won" << endl;
	goto final;
      }
      else if (o == 4 || (o==3 && t==1)) {
	cout << "O won" << endl;
	goto final;
      }
    }

    //percorrer outra diagonal
    x = o = t = 0;
    for (int i = 0; i < 4; ++i) {
      switch(m[i][3-i]) {
      case '.':
	pts = true;
	break;
      case 'X':
	++x;
	break;
      case 'O':
	++o;
	break;
      case 'T':
	++t;
	break;
      }
      if (x == 4 || (x==3 && t==1)) {
	cout << "X won" << endl;
	goto final;
      }
      else if (o == 4 || (o==3 && t==1)) {
	cout << "O won" << endl;
	goto final;
      }
    }
  
 
    pts ? cout << "Game has not completed" << endl : cout << "Draw" << endl;
    continue;

  final:
    ;
  }

  return 0;
}
	
/*

6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

*/
