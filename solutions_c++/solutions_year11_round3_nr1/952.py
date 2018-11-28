#include <iostream>

using namespace std;

char pic[50][50];
int R, C;

bool update() {
for(int i = 0; i < R; i++) {
  for(int j = 0; j < C; j++) {
    if(pic[i][j] == '#') {
      if((i == R - 1) || (j == C - 1) ||
	 (pic[i+1][j] != '#') ||
	 (pic[i][j+1] != '#') ||
	 (pic[i+1][j+1] != '#')
	 ) {
	return false;
      }
      pic[i][j] = '/';
      pic[i+1][j] = '\\';
      pic[i][j+1] = '\\';
      pic[i+1][j+1] = '/';
    }
  }
 }
 return true;
}


int main() {
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> R >> C;
    for(int i = 0; i < R; i++) {
      for(int j = 0; j < C; j++) {
	cin >> pic[i][j];
      }
    }
    cout << "Case #" << t << ":" << endl;
    if(update()) {
      for(int i = 0; i < R; i++) {
	for(int j = 0; j < C; j++) {
	  cout << pic[i][j];
	}
	cout << endl;
      }
    } else {
      cout << "Impossible" << endl;
    }
  }
}
