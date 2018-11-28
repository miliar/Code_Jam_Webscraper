#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

main(){
  int N;
  cin >> N;

  for(int NN = 1;NN <= N;NN++){
    int T,K;
    cin >> T >> K;
    int game[T][T];

    for(int i = 0;i < T;i++){
      for(int j = 0;j < T;j++){
	game[i][j] = 0;
      }
    }

    string tmp;
    for(int i = 0;i < T;i++){
      int counter = 0;
      cin >> tmp;
      for(int j = T-1;j >= 0;j--){
	int val = 0;
	switch(tmp[j]){
	case 'R':
	  val = 1;
	  break;
	case 'B':
	  val = 2;
	  break;
	}
	if(val != 0){
	  game[T-counter-1][i] = val;
	  counter++;
	}
      }

    }
    int dx[4] = {0,1,1,-1};
    int dy[4] = {1,1,0,1};
    bool win[3] = {false,false,false};
    for(int i = 0;i < T;i++){
      for(int j = 0;j < T;j++){
	int target;
	if(game[i][j] == 0)
	  continue;
	else
	  target = game[i][j];
	
	for(int d = 0;d < 4;d++){
	  int count;
	  for(count = 1;count < K;count++){
	    int nx = i+dx[d]*count ,ny = j+dy[d]*count;
	    if(! (nx >= 0 && ny>= 0 && nx < T && ny < T && game[nx][ny]==target) )
	      break;
	  }
	  if(count == K)
	    win[target] = true;
	}
      }
    }
    if(win[1] && win[2])
      printf("Case #%d: Both\n",NN);
    else if(win[1])
      printf("Case #%d: Red\n",NN);
    else if(win[2])
      printf("Case #%d: Blue\n",NN);
    else
      printf("Case #%d: Neither\n",NN);
  }
}
