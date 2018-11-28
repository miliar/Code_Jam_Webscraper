#include <cstdio>
#include <string>

/*
1 : X won
2 : O won
0 : else
 */
int chkRow(char tbl[5][5]){
  for(int i=0;i<4;++i){
    int x=0,o=0;
    for(int j=0;j<4;++j){
      char c = tbl[i][j];
      if(c=='X') ++x;
      if(c=='O') ++o;
      if(c=='T') ++x,++o;
    }
    if(x==4) return 1;
    if(o==4) return 2;
  }
  return 0;
}
int chkCol(char f[5][5]){
  char tmp[5][5];
  for(int i=0;i<5;++i) for(int j=0;j<5;++j) tmp[i][j] = f[j][i];
  return chkRow(tmp);
}

int chkDig(char tbl[5][5]){
  int x=0,o=0;
  for(int i=0;i<4;++i){
    char c = tbl[i][i];
    if(c=='X') ++x;
    if(c=='O') ++o;
    if(c=='T') ++x,++o;
  }
  if(x==4) return 1;
  if(o==4) return 2;
  x=0,o=0;
  for(int i=0;i<4;++i){
    char c = tbl[i][3-i];
    if(c=='X') ++x;
    if(c=='O') ++o;
    if(c=='T') ++x,++o;
  }
  if(x==4) return 1;
  if(o==4) return 2;

  return 0;
}
int main(){
  int T;
  char f[5][5];
  char ans[4][256] = {"Game has not completed","X won","O won","Draw"};
  scanf("%d",&T);
  int t = 0;
  while(T--&&++t){
    for(int i=0;i<4;++i){
      scanf("%s",f[i]);
    }
    int p = chkRow(f);
    if(!p) p = chkCol(f);
    if(!p) p = chkDig(f);
    if(!p){
      int cnt = 0;
      for(int i=0;i<4;++i) for(int j=0;j<4;++j) if(f[i][j]=='.') ++cnt;
      if(!cnt) p = 3;
    }
    printf("Case #%d: %s\n",t,ans[p]);
  }
  return 0;
}
