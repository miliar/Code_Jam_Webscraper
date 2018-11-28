#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#define rep(i,n) for(int i=0;i<n;i++)
#define fr(i,c) for(__typeof (c.begin()) i=c.begin(); i!=c.end(); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
using namespace std;

typedef vector<int> vi;
typedef long long ll;

inline void MX(int &a,int b){
  if(a<b)a=b;
}
int main(){
  int t; cin>>t;
  rep(it,t){
    cerr<<"it: "<<it+1<<endl;
    int n, r[100], p[100]; cin>>n;
    char c;
    rep(i,n){
      cin>>c>>p[i];
      p[i]--;
      r[i] = c=='O';
    }
    
    static int dp[2][100][100];
    int cur=0, next=1, tmp, mx=0;
    rep(i,100)rep(j,100)dp[0][i][j]=-1;
    dp[0][0][0]=0;
    
    rep(i,11111){
      rep(j,100)rep(k,100)dp[next][j][k]=-1;
      
      rep(j,100)rep(k,100){
        tmp = dp[cur][j][k];
        if(tmp<0)continue;

        if(tmp==n){
          cout<<"Case #"<<it+1<<": "<<i<<endl;
          goto END;
        }
        for(int dj=-1;dj<2;dj++)for(int dk=-1;dk<2;dk++){
            int nj=j+dj, nk=k+dk;
            if(nj<0||nk<0||nj>99||nk>99)continue;
            
            if(dk==0&&r[tmp]&&p[tmp]==k)MX(dp[next][nj][nk],tmp+1);
            if(dj==0&&!r[tmp]&&p[tmp]==j)MX(dp[next][nj][nk],tmp+1);
            
            MX(dp[next][nj][nk],tmp);
          }
      }
      swap(cur,next);
    }
  END:;
  }
  return 0;
}
