#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solve();

const int N=10;
int bad[1<<N];
int ok[1<<N];
int bits[1<<N];
int badize(int n);

int main(){
  for(int i=0;i< (1<<N);i++){
    bad[i]=badize(i);
  }
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<solve()<<'\n';
}

const int unseen=-1;

int memo(const vector<int>& v,int x,int people,vector<vector<int> >& state,int Y);

int solve(){
  int X,Y;
  cin>>X>>Y;
  vector<string> v(X);
  for(int i=0;i<X;i++)
    cin>>v[i];
  vector<int> vv(X);
  for(int i=0;i<v.size();i++)
    for(int j=0;j<v[i].size();j++)
      if(v[i][j]=='x')
        vv[i]|= 1<<j;
  vector<vector<int> > state(X,vector<int>(1<<Y,unseen));
  return memo(vv,0,0,state,Y);
}

int badize(int n){
  int ret=0;
  ok[n]=true;
  for(int i=0;i<N;i++)
    if(n & (1<<i)){
      int up= 1<<(i+1);
      ret|= up;
      if(n & up)
        ok[n]=false;
      if(i){
        int down= 1<<(i-1);
        ret|= down;
        if(n & down)
          ok[n]=false;
      }
    }
  int bit=0;
  int nn=n;
  while(n){
    if(n&1) bit++;
    n/=2;
  }
  bits[nn]=bit;
  return ret;
}

int memo(const vector<int>& v,int x,int people,vector<vector<int> >& state,int Y){
  if(x==v.size()) return 0;
  if(state[x][people]!=unseen)
    return state[x][people];
  int& ret=state[x][people]=0;
  for(int now=0;now< (1<<Y);now++)
    if(ok[now] && (now & v[x])==0 && (bad[now]&people)==0){
      int value=bits[now]+memo(v,x+1,now,state,Y);
      ret=max(value,ret);
    }
  return ret;
}
