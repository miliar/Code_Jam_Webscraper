#include<cstdio>
#include<algorithm>
using namespace std;
char board[55][55];
int T, K, N;

int cnt(char rb, int rc){

  if(rc == 0){
    for(int i = 0; i < N; i++){
      int cnt = 0;
      for(int j = 0; j < N; j++){
	if(board[i][j] == rb) cnt++;
	else cnt = 0;
	if(cnt >= K) return 1;
      }
    }
  }else{
    for(int i = 0; i < N; i++){
      int cnt = 0;
      for(int j = 0; j < N; j++){
	if(board[j][i] == rb) cnt++;
	else cnt = 0;
	if(cnt >= K) return 1;
      }
    }
  }
  return 0;
}
int cntdiag(char rb){
  for(int i = N-1; i >= -N+1; i--){
    int cnt = 0;
    for(int j = max(-i, 0); j < N && j+i < N; j++){
      if(board[j][i+j] == rb) cnt++;
      else cnt = 0;
      if(cnt >= K) return 1;
    }
  }
  for(int i = 0; i < 2*N-1; i++){
    int cnt = 0;
    for(int j =max(i-(N-1), 0); j < N && i-j >= 0; j++){
      if(board[j][i-j] == rb) cnt++;
      else cnt = 0;
      if(cnt >= K) return 1;
    }
  }
  return 0;
}
int main(){

  scanf("%d", &T);
  
  for(int ca = 0; ca < T; ca++){
    scanf("%d%d", &N, &K);
    
    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
	scanf(" %c", &board[i][j]);
    
    for(int i = 0; i < N; i++){
      int n = 0;
      for(int j = N-1; j >= 0; j--){
	if(board[i][j] != '.'){
	  if(N-1-n == j){
	    n++;
	    continue;
	  }
	  board[i][N-1-n] = board[i][j];
	  board[i][j] = '.';
	  n++;
	}
      }
    }


    bool r = cnt('R', 0) || cnt('R', 1) || cntdiag('R');

    bool b = cnt('B', 0) || cnt('B', 1) || cntdiag('B');
    
    printf("Case #%d: ",ca+1);
    if(r && b){
      printf("Both\n");
    }else if(r){
      printf("Red\n");
    }else if(b){
      printf("Blue\n");
    }else{
      printf("Neither\n");
    }
  }
}
