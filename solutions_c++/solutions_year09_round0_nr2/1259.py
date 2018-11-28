#include <cstdio>
#include <cstring>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

#define EXT 5
#define MAX_T 100
#define MAX_H 100
#define MAX_W 100

#define PB push_back
#define MP make_pair
#define SZ(x)  ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define ZERO(m) memset(m,0,sizeof(m))
#define JOIN(a,b) a##b
#define REP(i,n) for(int (i) = 0; (i) < (int)(n); (i)++)
#define FOR(i,a,b) for(int (i) = (a); (i) <= (int)(b); (i)++)
#define FORD(i,a,b) for(int (i) = (a); (i) >= (int)(b); (i)--)
#define FORX(i,c) for( __typeof( (c).begin() ) i = (c).begin(), JOIN(i,__end) = (c).end(); i != JOIN(i,__end); i++)

int T;
int H,W;
int mat[MAX_H+EXT][MAX_W+EXT];
int adj[MAX_H+EXT][MAX_W+EXT];
char matl[MAX_H+EXT][MAX_W+EXT];
int delta[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
vector<pair<int,pair<int,int> > >  cells;

void print_map(){
  for(int r = 0; r < H; r++){
    for(int c = 0; c < W; c++){
      if(c) putchar(' ');
      printf("%d",mat[r][c]);
    }
    putchar('\n');
  }
}
    
void print_sol(){
  for(int r = 0; r < H; r++){
    for(int c = 0; c < W; c++){
      if(c) putchar(' ');
      putchar(matl[r][c]);
    }
    putchar('\n');
  }
}

void read_map(){
  cells.clear();
  for(int r = 0; r < H; r++){
    for(int c = 0; c < W; c++){
      scanf("%d",&mat[r][c]);
      cells.PB(MP(mat[r][c],MP(r,c)));
    }
  }
}

bool is_valid(int r, int c){
  return r>=0 && r<H && c>=0 && c<W;
}

char curlbl;
void go(int r, int c){
  //printf("%d %d\n",r,c);
  matl[r][c] = curlbl;
  for(int i = 0; i < 4; i++){
    int rr = r+delta[i][0];
    int cc = c+delta[i][1];
    if(is_valid(rr,cc) && !matl[rr][cc]){      
      int d = adj[rr][cc];
      //printf("(%d,%d,%d)\n",rr,cc,d);
      if(d>=0){
        //printf("#%d %d>%d %d\n",rr,cc,xr,xc);
        if(rr+delta[d][0]==r && cc+delta[d][1]==c){          
          go(rr,cc);
        }
      }
    }
  }
}

void solve(){
  for(int r = 0; r < H; r++){
    for(int c = 0; c < W; c++){
      adj[r][c] = -1;
      int minh = INT_MAX;
      for(int k = 0; k < 4; k++){
        int rr = r+delta[k][0];
        int cc = c+delta[k][1];
        if(is_valid(rr,cc) && mat[rr][cc]<mat[r][c]){
          if(mat[rr][cc]<minh){
            adj[r][c] = k;
            minh = mat[rr][cc];
          }
        }
      }      
    }
  }
  memset(matl,0,sizeof(matl));
  sort(ALL(cells));
  curlbl = 'a';
  FORX(it,cells){
    int r = it->second.first;
    int c = it->second.second;    
    if(!matl[r][c]){
      //printf("%d %d\n",r,c);
      go(r,c);
      if(curlbl>'z') fputs(">'z'",stderr);
      curlbl++;      
      //printf("|%c|\n",curlbl);
    }
  }
  curlbl = 'a';
  char tmp[26];
  memset(tmp,0,sizeof(tmp));
  for(int r = 0; r < H; r++){
    for(int c = 0; c < W; c++){      
      int k = matl[r][c]-'a';
      if(!tmp[k]) tmp[k] = curlbl++;
    }
  }
  for(int r = 0; r < H; r++){
    for(int c = 0; c < W; c++){
      matl[r][c] = tmp[matl[r][c]-'a'];
    }
  }
}
 
int main(){
  scanf("%d",&T);
  for(int i = 1; i <= T; i++){
    scanf("%d%d",&H,&W);
    printf("Case #%d:\n",i);
    read_map();
    solve();
    print_sol();
    //print_map();
  }
  return 0;
}
