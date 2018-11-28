#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <map>
#include <set>
using namespace std;

#define INF 1000000000
// 1e9 < INT_MAX/2

int W,H;
int dx[2],dy[2];
int X,Y;
vector<vector<int> > D;

int lunar(int x, int y){
  if(x<0||x>=W||y<0||y>=H){
    return 0;
  }
  if(D[x][y]){
    return 0;
  }
  D[x][y]=1;
  return 1+lunar(x+dx[0],y+dy[0])+lunar(x+dx[1],y+dy[1]);
}

void tos(){
  cin>>W>>H;
  cin>>dx[0]>>dy[0];
  cin>>dx[1]>>dy[1];
  cin>>X>>Y;
  vector<vector<int> > d(W,H);
  D=d;
  cout<< lunar(X,Y) << endl;
}

int main(){
  int nCases;
  cin>>nCases;
  for(int c=1; c<=nCases; c++){
    cout<<"Case #"<<c<<": ";
    tos();
  }
  return 0;
}
