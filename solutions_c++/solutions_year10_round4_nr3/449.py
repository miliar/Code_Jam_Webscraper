#include<iostream>
#include<vector>

using namespace std;

int main(){
  int T;
  cin>>T;
  for (int t=1;t<=T;t++){
    vector<vector<int> > board(102);
    for (int i=0;i<102;i++){
      board[i].resize(102);
      for (int j=0;j<102;j++){
	board[i][j]=0;
      }
    }
    int R;
    cin>>R;
    for (int r=0;r<R;r++){
      int x1,x2,y1,y2;
      cin>>x1>>y1>>x2>>y2;
      for (int a=x1;a<=x2;a++){
	for (int b=y1;b<=y2;b++){
	  board[a+1][b+1]=1;
	}
      }
    }
    int k=0;
    for (;;k++){
      int test=0;
      for (int i=101;i>=1;i--){
	for (int j=101;j>=1;j--){
	  if ((board[i][j] && (board[i-1][j]+board[i][j-1])) ||
	      (board[i-1][j] && board[i][j-1])){
	    board[i][j]=1;
	    test=1;
	  }
	  else
	    board[i][j]=0;
	}
      }
      if (test==0) break;
    }
    cout<<"Case #"<<t<<": "<<k+1<<endl;
  }
}
