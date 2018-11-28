#include <cstdio>

int main() {
  unsigned t;
  scanf("%u ", &t);
  for (unsigned test=0; test<t; test++) {
    char mat[4][5];
    scanf(" %s %s %s %s ", mat[0], mat[1], mat[2], mat[3]);
    bool winO=false, winX=false, completed=true;
    for (int i=0; i<4; i++) {
      char c=mat[i][0];
      int j=1;
      if (c=='T') c = mat[i][j++];
      bool win = c!='.';
      for (; j<4; j++) {
	if (mat[i][j]!=c && mat[i][j]!='T') {
	  win = false;
	  break;
	}
      }
      if (win && c=='O') {
	winO = true;
	break;
      } else if (win) {
	winX = true;
	break;
      }
    }
	for (int i=0; i<4; i++) {
      char c=mat[0][i];
      int j=1;
      if (c=='T') c = mat[j++][i];
      bool win = c!='.';
      for (; j<4; j++) {
		if (mat[j][i]!=c && mat[j][i]!='T') {
	  	win = false;
	  	break;
		}
      }
    	if (win && c=='O') {
	winO = true;
	break;
      } else if (win) {
	winX = true;
	break;
      }
    }
    char c = mat[0][0];
    int j=1;
    if (c=='T') c = mat[1][1], j++;
    bool win = c!='.';
    for (; j<4; j++) {
    	if (c!=mat[j][j] && mat[j][j]!= 'T') {
    		win = false;
    		break;
    	}
    }
    if (win && c=='O') {
	winO = true;
      } else if (win) {
	winX = true;
      }
    win = true;
    j = 1;
    c = mat[0][3];
    if (c=='T') c = mat[1][2], j++;
    win = c!='.';
    for (; j<4; j++) {
    	if (c!=mat[j][3-j] && mat[j][3-j]!='T') {
    		win = false;
    		break;
    	}
    }
    if (win && c=='O') {
	winO = true;
      } else if (win) {
	winX = true;
      }
    if (winX) {
    	printf("Case #%u: X won\n", test+1);
    	continue;
    } else if (winO) {
    	printf("Case #%u: O won\n", test+1);
    	continue;
    }
    for (unsigned i=0; i<16; i++) {
    	if (mat[i/4][i%4]=='.') {
    		completed=false;
    		break;
    	}
    }
    if (completed==false) {
    	printf("Case #%u: Game has not completed\n", test+1);
    } else {
    	printf("Case #%u: Draw\n", test+1);
    }
    	
  }
  return 0;
}
