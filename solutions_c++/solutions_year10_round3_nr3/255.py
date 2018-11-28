#include <cstdio>
#include <cstdlib>

//This problem was annoying, I misread the problem statement three times.

using namespace std;

int boardsize(unsigned board[514][514], unsigned x, unsigned y, unsigned x_max, unsigned y_max){
  unsigned size;
  for (size=0;;size++){
    if (x+size+1 >= x_max) break;
    if (y+size+1 >= y_max) break;
    if (board[x+size+1][y] == 2) break;
    if (board[x+size+1][y] == board[x+size][y]) break;
    if (board[x][y+size+1] == 2) break;
    if (board[x][y+size+1] == board[x][y+size]) break;
    for (int i=x;i<x+size+1;i++){
      if (board[i][y+size+1] == board[i+1][y+size+1] || board[i+1][y+size+1] == 2) return size+1;
    }
    for (int i=y;i<y+size+1;i++){
      if (board[x+size+1][i] == board[x+size+1][i+1] || board[x+size+1][i+1] == 2) return size+1;
    }
  }
  return size+1;
}

int main(){
  unsigned tests, test;
  unsigned board[514][514];
  scanf("%d", &tests);
  for(test=0; test<tests; test++){
    unsigned m, n;
    scanf("%d %d", &m, &n);
    for (int i=0;i<m;i++)
      for (int j=0;j<n; j+=4){
	unsigned temp;
	scanf("%1x", &temp);
	board[i][j+0] = (temp&8)==8;
	board[i][j+1] = (temp&4)==4;
	board[i][j+2] = (temp&2)==2;
	board[i][j+3] = (temp&1)==1;
      }

    //for (int i=0;i<m;i++){
    //for (int j=0;j<n; j++)printf("%i", board[i][j]);
    // printf("\n");
    //}

    //    printf("%i\n", boardsize(board, 0, 13, m, n));
    //printf("%i\n", boardsize(board, 0, 14, m, n));
    //printf("%i\n", boardsize(board, 0, 12, m, n));

    unsigned count=0, maxsize2;
    unsigned result[514];
    for (int i=0;i<514;i++) result[i] = 0;
    while (true){
      unsigned maxsize=0, x, y;
      for (int i=0;i<m;i++){
	for (int j=0;j<n; j++){
	  if (board[i][j] == 2) continue;
	  int size = boardsize(board, i, j, m, n);
	  if (size>maxsize) {
	    maxsize = size;
	    x=i;
	    y=j;
	  }
	}
      }
      //printf("%i, %i, %i\n", maxsize, x, y);
      if (maxsize==0) break;
      
      result[maxsize]++;
      for (int i=x;i<x+maxsize;i++)
	for (int j=y;j<y+maxsize; j++)
	  board[i][j] = 2;
    }
    unsigned numsize=0;
    for (int i=0;i<514;i++) if(result[i] != 0) numsize++;
    printf("Case #%i: %i\n", test+1, numsize);
    for (int i=513;i>0;i--) if(result[i] != 0) printf("%i %i\n", i, result[i]);
  }
}
