#include <stdio.h>
#include <string.h>


const int MAXN = 128;//20;//128;


bool alive[MAXN][MAXN];


int main() {


  FILE* fin  = fopen("C.in",  "r");
  FILE* fout = fopen("C.out", "w");

  int C;
  fscanf(fin, "%d", &C);

  for(int test = 1; test <= C; ++test) {
    for(int i = 0; i < MAXN; ++i) {
      memset(alive[i], false, MAXN);
    }
    int rects;
    fscanf(fin, "%d", &rects);
//     printf("rects = %d\n", rects);
    for(int i = 0; i < rects; ++i) {
      int x1,y1,x2,y2;
      fscanf(fin, "%d %d %d %d", &x1, &y1, &x2, &y2);
      //printf("rect %d %d %d %d\n", x1, y1, x2, y2);
      //--x1; --y1; --x2; --y2; DON'T DO THIS!
      for(int x = x1; x <= x2; ++x) {
	for(int y = y1; y <= y2; ++y) {
	  alive[x][y] = true;
	}
      }
    }

    int t = 0;
    while(true) {
//       printf("t = %d\n", t);
//       for(int y = 0; y < MAXN; ++y) {
// 	for(int x = 0; x < MAXN; ++x) {
// 	  printf("%c", alive[x][y] ? '*' : '.');
// 	}
// 	printf("\n");
//       }
//       printf("\n");
      bool someone = false;
      for(int x = MAXN-1; x >= 1; --x) {
	for(int y = MAXN-1; y >= 1; --y) {
	  someone = someone || alive[x][y];
	  alive[x][y] =
	    (alive[x][y] && (alive[x-1][y] || alive[x][y-1])) ||
	    (alive[x-1][y] && alive[x][y-1]);
	}
      }
      if(!someone) break;
      t += 1;
    }

    fprintf(fout, "Case #%d: %d\n", test, t);
  }


  return(0);

}
