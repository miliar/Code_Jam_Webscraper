#include <iostream>
#include <vector>

using namespace std;

vector<int> solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    vector<int> v=solve();
    cout<<"Case #"<<i+1<<":";
    if(v.size()){
      for(int j=0;j<v.size();j++)
        cout<<' '<<v[j];
      cout<<'\n';
    }else
      cout<<" IMPOSSIBLE\n";
  }
}

bool valid(int x,int xx,int X);
int mini(int x,int xx,int X);
inline int area(int x,int y,int xx,int yy);
vector<int> solve(){
  int X,Y,A;
  cin>>X>>Y>>A;
  for(int x=-X;x<=X;x++) for(int xx=-X;xx<=X;xx++) if(valid(x,xx,X))
  for(int y=-Y;y<=Y;y++) for(int yy=-Y;yy<=Y;yy++) if(valid(y,yy,Y)){
    int a=area(x,y,xx,yy);
    //cout<<a<<'\n';
    if(a==A){
      vector<int> v(6);
      v[0]=mini(x,xx,X); v[1]=mini(y,yy,Y);
      v[2]=v[0]+x; v[3]=v[1]+y;
      v[4]=v[2]+xx; v[5]=v[3]+yy;
      return v;
    }
  }
  return vector<int>();
}

int area(int x,int y,int xx,int yy){
  return abs(x*yy-y*xx);
}

bool valid(int x,int xx,int X){
  if(x>=0 && xx>=0)
    return x+xx<=X;
  if(x<0 && xx<0)
    return x+xx>=-X;
  return true;
}

int mini(int x,int xx,int X){
  if(x>=0 && xx>=0)
    return 0;
  if(x<0 && xx<0)
    return X;
  if(x>=0 && xx<0)
    return X-x;
  if(x<0 && xx>=0)
    return -x;
  assert(false);
}
