#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int hextochar(char a){
  if(a >= '0' && a <= '9')
    return a - '0';
  else
    return a - 'A' + 10;
    
}



int board[512][512];
void print_board(int M,int N ){
  for(int i = 0;i < M;i++){
      for(int j = 0;j < N;j++){
	cout << board[i][j] << " ";
      }
      cout << endl;
  }
}
void print_s(int M,int N,int* s){
  for(int i = 0;i < M;i++){
      for(int j = 0;j < N;j++){
	cout << s[i*N+j] << " ";
      }
      cout << endl;
  }
}

int score[512][512];
int create_table(int M,int N){
  
  for(int x = 0;x < M;x++){
    for(int y = 0;y < N;y++){
      int base = board[x][y];
      
      int start = 1;
      if(y-1 >= 0)
	start = max(start,score[x][y-1]) - 1;
      if(x-1 >= 0)
	start = max(start,score[x-1][y]) - 1;

      int w = 1;
      bool flag = true;

      for(w = start+1;w <= min(M-x,N-y);w++){
	int color = (base + w-1) % 2;

	//tate
	for(int dx = 0;dx < w;dx++){
	  if(board[x+dx][y+w-1] != (color + dx) % 2){
	    flag = false;
	    break;
	  }
	}
	for(int dy = 0;dy < w;dy++){
	  if(board[x+w-1][y+dy] != (color + dy) % 2){
	    flag = false;
	    break;
	  }
	}
	if(flag == false)
	  break;
      }
      w -= 1;
      //cout << "x:" << x << " y:" << y << " start:" << start << " w:" << w<<endl;
      score[x][y] = w;
    }
  }
}




main(){
  int T;
  cin >> T;


  for(int t = 0;t < T;t++){
    int M,N;
    cin >> M >> N;

    for(int i = 0;i < M;i++){
      string tmp;
      cin >> tmp;

      for(int j = 0;j < tmp.size();j++){
	int num = hextochar(tmp[j]);
	board[i][j*4+3] = num & 0x1;
	board[i][j*4+2] = (num & 0x2) >> 1;
	board[i][j*4+1] = (num & 0x4) >> 2;
	board[i][j*4+0] = (num & 0x8) >> 3;
      }
    }
    int remain = M * N;
    int result[min(M,N)];
    for(int i = 0;i <= min(M,N);i++){
      result[i] = 0;
    }

    create_table(M,N);
    //print_board(M,N);
    //cout << endl;
    //print_s(M,N,&score[0][0]);
    
    while(remain > 0){
      int max_w=0,max_x,max_y;
      for(int x = 0;x < M;x++){
	for(int y = 0;y < N;y++){
	  if(score[x][y] > max_w){
	    max_w = score[x][y];
	    max_x = x;
	    max_y = y;
	  }
	}
      }
      remain -= max_w * max_w;
      result[max_w-1]++;

      for(int dx = 0;dx < max_w;dx++){
	for(int dy = 0;dy < max_w;dy++){
	  score[max_x+dx][max_y+dy] = -1;
	}
      }

      for(int x = 0;x < M;x++){
	for(int y = 0;y < N;y++){
	  if(score[x][y] == -1)
	    continue;
	  if(x <= max_x){
	    if(y <= max_y){
	      int wx = (x+score[x][y]) - max_x;
	      int wy = (y+score[x][y]) - max_y;
	      if(wx > 0 && wy > 0){
		int len = min(wx,wy);
		score[x][y] -= len;
	      }
	    }
	    else{
	      int wx = (x+score[x][y]) - max_x;
	      int wy = max_y+max_w - y;
	      if(wx > 0 && wy > 0){
		int len = wx;
		score[x][y] -= len;
	      }
	    }
	  }
	  else{
	    if(y <= max_y){
	      int wx = max_x+max_w - x;
	      int wy = (y+score[x][y]) - max_y;
	      if(wx > 0 && wy > 0){
		int len = wy;
		score[x][y] -= len;
	      }
	    }
	    else{
	      int wx = max_x+max_w - x;
	      int wy = max_y+max_w - y;
	      if(wx > 0 && wy > 0){
		score[x][y] = -1;
	      }
	    }
	  }
	}
      }
      //print_s(M,N,&score[0][0]);
    }

    
    int result_count = 0;
    for(int i = 0;i < min(M,N);i++){
      if(result[i] != 0)
	result_count++;
    }
    
    
    cout << "Case #" << (t+1) << ": " << result_count << endl;
    for(int i = min(M,N);i >= 0;i--){
      if(result[i] != 0)
	cout << i+1 << " " << result[i] << endl;
    }
  }
  return 0;
}
