#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)
#define ll long long
#define clear(d) memset(d,0,sizeof(d))
#define INF 2000000000

using namespace std;

struct grp{
  int size;
  int rsize;
  int next;
};

grp G[1010];

int main(){
  int CN;
  cin >> CN;
  For1(CI,CN){
    int R,K,N;
    cin >> R >> K >> N;
    clear(G);
    For(g, N){
      cin >> G[g].size;
    }
    int rs, nx; 
    For(g, N){
      for(rs=0,nx=g;true;){
        if(rs+G[nx].size>K) break;
        rs+=G[nx].size;
        nx=(nx+1)%N;
        if(nx==g) break;
      }
      G[g].rsize=rs;
      G[g].next=nx;
    }
    ll res=0;
    int g=0;
    For(i,R){
      res+=G[g].rsize;
      g=G[g].next;
    }

    cout << "Case #" << CI << ": " << res << endl;
  }
}
