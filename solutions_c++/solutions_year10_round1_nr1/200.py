#include <iostream>
#include <string>
#include <vector>

using namespace std;

string answer[4]={"Neither","Blue","Red","Both"};

int solve(vector<string>& board,int k);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int n,k;
    cin>>n>>k;
    vector<string> board(n);
    for(int j=0;j<board.size();j++)
      cin>>board[j];
    cout<<"Case #"<<i+1<<": "<<answer[solve(board,k)]<<'\n';
  }
}

vector<string> rotate(const vector<string>& board);
vector<string> gravity(vector<string> board);
bool solved(const vector<string>& board,char player,int k);
void print(const string& s,const vector<string> v);

int solve(vector<string>& board,int k){
  //print("start",board);
  board=rotate(board);
  //print("rotate",board);
  board=gravity(board);
  //print("gravity",board);
  return solved(board,'B',k)+2*solved(board,'R',k);
}

vector<string> rotate(const vector<string>& board){
  vector<string> ret(board[0].size(),string(board.size(),' '));
  for(int i=0;i<ret.size();i++)
    for(int j=0;j<ret[i].size();j++)
      ret[i][j]=board[board[0].size()-1-j][i];
  return ret;
}

vector<string> gravity(vector<string> board){
  for(int i=board.size()-1;i>=0;i--)
    for(int j=0;j<board[i].size();j++){
      int y=i;
      while(y+1<board.size() && board[y+1][j]=='.'){
        swap(board[y][j],board[y+1][j]);
        y++;
      }
    }
  return board;
}

const int dirs=8;
const int dx[dirs]={-1,-1,-1,0,0,1,1,1};
const int dy[dirs]={-1,0,1,-1,1,-1,0,1};

inline bool good(const vector<string>& v,int x,int y){
  return x>=0 && y>=0 && x<v.size() && y<v[x].size();
}

int pieces(const vector<string>& board,int x,int y,int d){
  int ret=1;
  while(true){
    const int nx=x+dx[d],ny=y+dy[d];
    if(!good(board,nx,ny) || board[nx][ny]!=board[x][y])
      return ret;
    ret++;
    x=nx;
    y=ny;
  }
  return ret;
}

bool solved(const vector<string>& board,char player,int k){
  for(int i=0;i<board.size();i++)
    for(int j=0;j<board[i].size();j++)
      if(board[i][j]==player)
        for(int d=0;d<dirs;d++)
          if(pieces(board,i,j,d)>=k)
            return true;
  return false;
}

void print(const string& s,const vector<string> v){
  cout<<s<<":\n";
  for(int i=0;i<v.size();i++)
    cout<<' '<<v[i]<<'\n';
}
