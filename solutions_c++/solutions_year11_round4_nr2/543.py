#include <iostream>
#include <vector>
#include <string>
using namespace std;

void solve(){
  int R;cin>>R;
  int C;cin>>C;
  int D;cin>>D;
  vector<vector<int>> w(R,vector<int>(C));
  for(int i=0;i<R;++i){
    string s;cin>>s;
    for(int j=0;j<C;++j){
      w[i][j]=s[j]-'0';
    }
  }
  int res = 0;
  int size = (min(C,R)-1)/2;
  vector<vector<vector<int>>> wh(R,vector<vector<int>>(C,vector<int>(size+1)));
  vector<vector<vector<int>>> wv(R,vector<vector<int>>(C,vector<int>(size+1)));
  for(int k=0;k<=size;++k){
    for(int i=0;i<R;++i){
      for(int j=0;j<C;++j){
        wv[i][j][k]=0;
        if(i-k>=0&&i+k<R)for(int l=i-k;l<=i+k;++l)wv[i][j][k]+=w[l][j];
        wh[i][j][k]=0;
        if(j-k>=0&&j+k<C)for(int l=j-k;l<=j+k;++l)wh[i][j][k]+=w[i][l];
      }
    }
  }
  for(int k=size;k>=1;--k){
    for(int i=k;i+k<R;++i){
      for(int j=k;j+k<C;++j){
        int moment = 0;
        for(int x=j-k;x<=j+k;++x){
          if(x==j-k||x==j+k)moment+=wv[i][x][k-1]*(j-x);
          else moment+=wv[i][x][k]*(j-x);
        }
        if(moment!=0)continue;
        for(int y=i-k;y<=i+k;++y){
          if(y==i-k||y==i+k)moment+=wh[y][j][k-1]*(i-y);
          else moment+=wh[y][j][k]*(i-y);
        }
        if(moment!=0)continue;
        //cout << i <<":"<<j<<endl;
        res=2*k+1;
        goto loop;
      }
    }
  }loop:

  size = min(C,R)/2;
  vector<vector<vector<int>>> wh2(R,vector<vector<int>>(C,vector<int>(size+1)));
  vector<vector<vector<int>>> wv2(R,vector<vector<int>>(C,vector<int>(size+1)));
  for(int k=0;k<=size;++k){
    for(int i=0;i<R;++i){
      for(int j=0;j<C;++j){
        wv2[i][j][k]=0;
        if(i-k>=0&&i+k-1<R)for(int l=i-k;l<=i+k-1;++l)wv2[i][j][k]+=w[l][j];
        wh2[i][j][k]=0;
        if(j-k>=0&&j+k-1<C)for(int l=j-k;l<=j+k-1;++l)wh2[i][j][k]+=w[i][l];
      }
    }
  }
  for(int k=size;k>=2;--k){
    for(int i=k;i+k-1<R;++i){
      for(int j=k;j+k-1<C;++j){
        int moment = 0;
        for(int x=j-k;x<=j+k-1;++x){
          if(x==j-k||x==j+k-1)moment+=wv2[i][x][k-1]*(2*(j-x)-1);
          else moment+=wv2[i][x][k]*(2*(j-x)-1);
        }
        if(moment!=0)continue;
        for(int y=i-k;y<=i+k-1;++y){
          if(y==i-k||y==i+k-1)moment+=wh2[y][j][k-1]*(2*(i-y)-1);
          else moment+=wh2[y][j][k]*(2*(i-y)-1);
        }
        if(moment!=0)continue;
        //cout << i <<":"<<j<<endl;
        res=max(res,2*k);
        goto loop2;
      }
    }
  }loop2:

  if(res>0)cout << res << endl;
  else cout<<"IMPOSSIBLE"<<endl;
}
int main(){
  int N;cin>>N;
  for(int i=1;i<=N;++i){
    cout << "Case #" << i <<": ";
    solve();
  }
  return 0;
}

