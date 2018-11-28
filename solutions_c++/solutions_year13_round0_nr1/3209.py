#include <string>
#include <vector>
#include <iostream>

using namespace std;

string decide(vector <string> b) {
  int i, j;
  int ocnt, xcnt, tcnt, dcnt;
  /* H */
  for (i = 0; i < 4; i++) {
    ocnt = xcnt = tcnt = dcnt = 0;
    for (j = 0; j < 4; j++) {
      switch (b[i][j]) {
      case 'X':
	xcnt++;
	break;
      case 'O':
	ocnt++;
	break;
      case 'T':
	tcnt++;
	break;
      default:
	dcnt++;
      }
    }
    if (xcnt + tcnt == 4) {
      return "X won";
    }
    if (ocnt + tcnt == 4) {
      return "O won";
    }
  }

  /* V */
  for (j = 0; j < 4; j++) {
    ocnt = xcnt = tcnt = dcnt = 0;
    for (i = 0; i < 4; i++) {
      switch (b[i][j]) {
      case 'X':
	xcnt++;
	break;
      case 'O':
	ocnt++;
	break;
      case 'T':
	tcnt++;
	break;
      default:
	dcnt++;
      }
    }
    if (xcnt + tcnt == 4) {
      return "X won";
    }
    if (ocnt + tcnt == 4) {
      return "O won";
    }
  }
    
  /* D1 */

  ocnt = xcnt = tcnt = dcnt = 0;
  for (i = 0; i < 4; i++) {
    switch (b[i][i]) {
    case 'X':
      xcnt++;
      break;
    case 'O':
      ocnt++;
      break;
    case 'T':
      tcnt++;
      break;
    default:
      dcnt++;
    }
  }
  if (xcnt + tcnt == 4) {
    return "X won";
  }
  if (ocnt + tcnt == 4) {
    return "O won";
  }

  /* D2 */

  ocnt = xcnt = tcnt = dcnt = 0;
  for (i = 0; i < 4; i++) {
    switch (b[i][3-i]) {
    case 'X':
      xcnt++;
      break;
    case 'O':
      ocnt++;
      break;
    case 'T':
      tcnt++;
      break;
    default:
      dcnt++;
    }
  }
  if (xcnt + tcnt == 4) {
    return "X won";
  }
  if (ocnt + tcnt == 4) {
    return "O won";
  }

  /* dot check */

  ocnt = xcnt = tcnt = dcnt = 0;
  for (j = 0; j < 4; j++) {
    for (i = 0; i < 4; i++) {
      if (b[i][j] == '.') {
	return "Game has not completed";
      }
    }
  }

  return "Draw";

}



int main(void) {
  int T, t;

  cin >> T;

  for (t = 1; t <= T; t++) {
    vector <string> b;
    string s, r;
    int l;
    for (l = 0; l < 4; l++) {
      cin >> s;
      b.push_back(s);
    }
    r = decide(b);
    cout << "Case #" << t << ": " << r << endl;

  }


  return 0;
}
