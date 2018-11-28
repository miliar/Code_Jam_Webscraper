#include <iostream>
#include <vector>

using namespace std;

int simple_answer();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<simple_answer()<<'\n';
}

const int N=101;

void print(int,vector<vector<int> >& v);
bool simulate(vector<vector<int> >& board);

int simple_answer(){
  vector<vector<int> > board(N,vector<int>(N+1));
  int r;
  cin>>r;
  int max_x=1,max_y=1;
  for(int i=0;i<r;i++){
    int x,xx,y,yy;
    cin>>x>>y>>xx>>yy;
    for(int j=x;j<=xx;j++)
      for(int k=y;k<=yy;k++)
        board[j][k]=true;
    max_x=max(xx+1,max_x);
    max_y=max(yy+1,max_y);
  }
  board.resize(max_x);
  for(int i=0;i<board.size();i++)
    board[i].resize(max_y);
  int years=1;
  print(years,board);
  while(simulate(board)){
    print(years,board);
    years++;
  }
  return years;
}

bool simulate(vector<vector<int> >& board){
  vector<vector<int> > new_board(board.size(),vector<int>(board[0].size()));
  bool ret=false;
  for(int i=0;i<new_board.size();i++)
    for(int j=0;j<new_board[i].size();j++)
      if(i && j && board[i-1][j] && board[i][j-1]){
        new_board[i][j]=1;
        ret=true;
      }else if(i && board[i][j] && board[i-1][j]){
        new_board[i][j]=1;
        ret=true;
      }else if(j && board[i][j] && board[i][j-1]){
        new_board[i][j]=1;
        ret=true;
      }
  swap(board,new_board);
  return ret;
}

void print(int year,vector<vector<int> >& v){
  return;
  cout<<year<<":\n";
  for(int i=0;i<v.size();i++){
    for(int j=0;j<v[i].size();j++)
      cout<<v[i][j];
    cout<<'\n';
  }
}
