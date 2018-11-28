#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int T;
int N;
int K;
int TC = 1;
char board[50][50];
char flip[50][50];
int next_op[50];
char buf[50];

bool inbounds(int i, int j, int N)
{
  if (i < 0 || j <0 || i >= N || j >= N)
      return false;
  return true;
}


int main ()
{
    for (scanf ("%d", &T); TC <= T; TC++)
    {
      scanf("%d %d", &N, &K);

      char junk;
      scanf("%c", &junk);
      for(int i = 0; i < N; i++) {
	int j = 0;
	while(j < N){
	  scanf("%c", &board[i][j]);
	  j++;
	}
	scanf("%c", &junk);
      }
 
      // flip
      for(int i = 0; i < N; i++)
	for(int j = 0; j < N; j++)
	  flip[j][N-i-1] = board[i][j];
      
      // do gravity
      for (int i = 0; i < N; i++)
	next_op[i] = N-1;

      for (int r = N-1; r >= 0; r--) {
	for (int c = 0; c < N; c++) {
	  if(flip[r][c] != '.') {
	    flip[next_op[c]][c] = flip[r][c];
	    if(next_op[c] > r)
	      flip[r][c] = '.';
	    next_op[c]--;
	  }
	}
      }
      

      bool red = false;
      bool blue = false;

      // find k
      for (int i = 0; i < N; i++) {
	for(int j = 0; j < N; j++){
	  if(flip[i][j] == '.')
	    continue;
	  int up = 0;
	  int down = 0;
	  int left = 0;
	  int right = 0;
	  int dl = 0;
	  int dr = 0;
	  int ul = 0;
	  int ur = 0;
	    
	  bool go_up = true;
	  bool go_down = true;
	  bool go_left = true;
	  bool go_right = true;
	  bool go_dl = true;
	  bool go_dr = true;
	  bool go_ul = true;
	  bool go_ur = true;

	  char c = flip[i][j];

	  for (int k = 1; k < N; k++) {
	    if(inbounds(i-k,j,N) && go_up)
	      {
		if (flip[i-k][j] == c)
		  up++;
		else
		  go_up = false;
	      }
	    if(inbounds(i+k,j,N) && go_down)
	      {
		if (flip[i+k][j] == c)
		  down++;
		else
		  go_down = false;
	      }
	    if(inbounds(i,j-k, N) && go_left){
	      if(flip[i][j-k] == c)
		left++;
	      else
		go_left = false;
	    }
	    if(inbounds(i,j+k,N) && go_right){
	      if(flip[i][j+k] == c)
		right++;
	      else
		go_right = false;
	    }
	    if(inbounds(i-k,j+k,N) && go_ur) {
	      if(flip[i-k][j+k] == c)
		ur++;
	      else
		go_ur = false;
	    }
	    if(inbounds(i-k,j-k,N) && go_ul) {
	      if(flip[i-k][j-k] == c)
		ul++;
	      else
		go_ul = false;
	    }
	    if(inbounds(i+k,j+k,N) && go_dr){
	      if(flip[i+k][j+k] == c)
		dr++;
	      else
		go_dr = false;
	    }
	    if(inbounds(i+k,j-k,N) && go_dl)
	      if(flip[i+k][j-k] == c)
		dl++;
	      else
		go_dl = false;
	  }
	  
	  if(up+down+1 >= K || left+right+1 >= K || dl+ur+1 >= K 
	     || ul+dr+1 >= K)
	    {
	      if(flip[i][j] == 'R')
		red = true;
	      if(flip[i][j] == 'B')
		blue = true;
	    }
	}

      }
      

      
      if (red && blue)
	printf("Case #%d: Both\n", TC);
      
      if (red && !blue)
	printf("Case #%d: Red\n", TC);

      if (!red && blue)
	printf("Case #%d: Blue\n", TC);

      if (!red && !blue)
	printf("Case #%d: Neither\n", TC);


    }

    return 0;
}
