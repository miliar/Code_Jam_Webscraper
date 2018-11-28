#include <iostream>

using namespace std;

int c[4][2];
int r[4][2];
int d[2][2];

int main(){
  int t, won;
  char x;
  cin >> t;

  for(int k = 1;k<=t;k++){
    memset(c, 0, sizeof c);
    memset(r, 0, sizeof r);
    memset(d, 0, sizeof d);
    won = 0;

    for(int j=0;j<4;j++)
      for(int i=0;i<4;i++){
	cin >> x;
	if(x == 'X' || x == 'T'){
	  c[i][0]++;
	  r[j][0]++;
	  if(i == j)
	    d[0][0]++;
	  if(i == 3 - j)
	    d[1][0]++;
	}
	if(x == 'O' || x == 'T'){
	  c[i][1]++;
	  r[j][1]++;
	  if(i == j)
	    d[0][1]++;
	  if(i == 3 - j)
	    d[1][1]++;
	}
	if(x == '.' && won == 0)
	  won = 3;
	if(c[i][0] == 4 || r[j][0] == 4 || d[0][0] == 4 || d[1][0] == 4)
	  won = 1;
	if(c[i][1] == 4 || r[j][1] == 4 || d[0][1] == 4 || d[1][1] == 4)
	  won = 2;
      }
    
    cout << "Case #" << k << ": ";
    if(won == 0)
      cout << "Draw" << endl;
    if(won == 1)
      cout << "X won" << endl;
    if(won == 2)
      cout << "O won" << endl;
    if(won == 3)
      cout << "Game has not completed" << endl;
  }

  return 0;
}
