#include <iostream>
#include <vector>
#include <string>
#include <cctype>

#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

const int N=128;

struct pt{ int i,j; };
const int DI[]={-1,0,0,1};
const int DJ[]={0,-1,1,0};

int li,lj;
int alt[N][N];
pt snk[N][N];

bool done[N][N];
char ans[N][N];

inline bool valid(int i,int j){ return 0<=i && i<li && 0<=j && j<lj; }

pt calc(int ci,int cj){
  if(!done[ci][cj]){
    done[ci][cj]=true;

    int v[4];
    REP(d,4){
      int ni=ci+DI[d], nj=cj+DJ[d];
      v[d]=valid(ni,nj) ? alt[ni][nj] : 1<<20;
    }
    int p=min_element(v,v+4)-v;
    snk[ci][cj]=(v[p]<alt[ci][cj] ? calc(ci+DI[p],cj+DJ[p]) : (pt){ci,cj});  
  }

  return snk[ci][cj];
}

int main(){
  int C; cin >> C;
  REP(CC,C){
    cin >> li >> lj;
    REP(i,li) REP(j,lj) cin >> alt[i][j];
    memset(done,false,sizeof done);
    memset(ans,0,sizeof ans);

    cout << "Case #" << CC+1 << ":" << endl;
    int cnt=0;
    REP(i,li){
      REP(j,lj){
        if(j) cout << ' ';
        pt s=calc(i,j);
        if(!ans[s.i][s.j]) ans[s.i][s.j]=cnt+'a', cnt++;
        cout << ans[s.i][s.j];
      }

      cout << endl;
    }
  }
}
