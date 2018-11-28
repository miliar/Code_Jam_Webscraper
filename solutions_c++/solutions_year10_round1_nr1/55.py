#include <iostream>
#include <fstream>


const int MAXN = 128;


int n, K;
char board[MAXN][MAXN+1];
char board2[MAXN][MAXN+1];
int pos[MAXN];

int main() {

  FILE* fout = fopen("A.out", "w");

  int tests;

  std::ifstream fin("A.in");
  fin >> tests;
  for(int t = 0; t < tests; ++t) {
    fin >> n >> K;
    fin.getline(board[0], MAXN, '\n');
    for(int i = 0; i < n; ++i) {
      fin.getline(board[i], MAXN, '\n');
      //std::cout << board[i] << "\n";
    }

    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < n; ++j) {
	board2[i][j] = '.';
      }
      board2[i][n] = '\0';
      pos[i] = n-1;
    }
    for(int j = n-1; j >= 0; --j) {
      for(int i = 0; i < n; ++i) {
	if(board[i][j] == '.') continue;
	board2[pos[n-1-i]][n-1-i] = board[i][j];
	--pos[n-1-i];
      }
    }

//     for(int i = 0; i < n; ++i) {
//       std::cout << board[i] << '\n';
//     }
//     std::cout << "-----------\n";
//     for(int i = 0; i < n; ++i) {
//       std::cout << board2[i] << '\n';
//     }
//     std::cout << "\n\n";


    bool blue = false;
    bool red  = false;

    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < n; ++j) {
	if(board2[i][j] == '.') continue;
	char color = board2[i][j];
	const int dy[8] = { 0,-1,-1,-1, 0,+1,+1,+1};
	const int dx[8] = {+1,+1, 0,-1,-1,-1, 0,+1};
	for(int k = 0; k < 8; ++k) {
	  int len = 1;
	  for(int d = 1; d < K; ++d) {
	    int y = i + d*dy[k];
	    int x = j + d*dx[k];
	    if(0 <= y && y < n &&
	       0 <= x && x < n &&
	       board2[y][x] == color) {
	      len = 1+d;
	    } else {
	      break;
	    }
	  }
	  //printf("(%d,%d) len=%d\n", i, j, len);
	  if(len == K) {
	    if(color == 'R') {
	      red = true;
	    } else if(color == 'B') {
	      blue = true;
	    } else {
	      std::cerr << "Bad color " << color << "\n";
	    }
	  }
	}
      }
    }

    const char *s;
    if(red && blue) {
      s = "Both";
    } else if(red) {
      s = "Red";
    } else if(blue) {
      s = "Blue";
    } else {
      s = "Neither";
    }

    fprintf(fout, "Case #%d: %s\n", 1+t, s);

  }


  fclose(fout);


  return(0);
}
