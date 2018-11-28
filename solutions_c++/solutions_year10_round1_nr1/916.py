#include <stdio.h>
#include <string.h>

using namespace std;


main() {

  int T;

  scanf("%d",&T);

  for (int i = 1; i <= T; i++) {
    
    int n,k;
    char line[1000];
    scanf("%d %d",&n,&k);
    char mat[101][101];
    //memset(mat,'.',101*101);
    for (int a = 0; a < 101; a++) {
      for (int b = 0; b < 101; b++) {
	mat[a][b] = '.';
      }
    }
    for (int l = 0; l < n; l++) {

      scanf("%s",line);
      int c = 0;
      for (int p = strlen(line) -1 ; p >= 0; p--) {
	if (line[p] != '.') {
	  mat[l][c] = line[p];
	  c++;
	}
      }
    }
    
    int won = 0;

    
    for (int col = 0; col < n; col++) {
      int count = 0;
      char color = '.';
      for (int l = 0; l < n; l++) {
	if (color == mat[l][col]) {
	  count++;
	}
	else { 
	  color = mat[l][col];
	  count = 1;
	}

	if (count >= k) {
	  if (color == 'B') {
	    won |= 1;
	  }
	  else {
	    if (color == 'R') {
	      won |= 2;
	    }
	  }
	}	
      }
    }


    if (won != 3) 
    for (int l = 0; l < n; l++) {
      int count = 0;
      char color = '.';
      for (int col = 0; col < n; col++) {
	if (color == mat[l][col]) {
	  count++;
	}
	else { 
	  color = mat[l][col];
	  count = 1;
	}

	if (count >= k) {
	  if (color == 'B') {
	    won |= 1;
	  }
	  else {
	    if (color == 'R') {
	      won |= 2;
	    }
	  }
	}	
      }
    }
    
    
    if (won != 3) 
    for (int l = -n+1; l < n; l++) {
      int count = 0;
      char color = '.';
      int start = 0;
      if (l < 0) start = -l;
      // printf("\n");
      
      for (int col = start; (col + l  < n) && ( col < n); col++) {
	// printf("%d,%d : %c",l+col,col,mat[l+col][col]);
	if (color == mat[l+col][col]) {
	  count++;
	}
	else { 
	  color = mat[l+col][col];
	  count = 1;
	}

	if (count >= k) {
	  if (color == 'B') {
	    won |= 1;
	  }
	  else {
	    if (color == 'R') {
	      won |= 2;
	    }
	  }
	}	
      }
    }


    if (won != 3) 
    for (int l = 0; l < 2*n-1; l++) {
      int count = 0;
      char color = '.';
      int start = 0;
      if (l > n-1) start = l-n+1;
      // printf("\n");
      for (int col = start; (((l - col ) >= 0) && (col < n)) ; col++) {
	// printf("%d,%d : %c ",l-col,col, mat[l-col][col]);
	if (color == mat[l-col][col]) {
	  count++;
	}
	else { 
	  color = mat[l-col][col];
	  count = 1;
	}

	if (count >= k) {
	  if (color == 'B') {
	    won |= 1;
	  }
	  else {
	    if (color == 'R') {
	      won |= 2;
	    }
	  }
	}	
      }
    }

    
    
    printf("Case #%d: ",i);
    
    if (won == 0) {
      printf("Neither\n");
    }
    if (won == 1) {
      printf("Blue\n");
    }
    if (won == 2) {
      printf("Red\n");
    }
    if (won == 3) {
      printf("Both\n");
    }

  }
  




}
