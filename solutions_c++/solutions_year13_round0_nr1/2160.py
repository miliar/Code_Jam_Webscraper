#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<numeric>
#include<map>
#include<set>
#include<cstdlib>
#include<string>
#include<cassert>
#include<iostream>
using namespace std;
typedef vector<int> vi;
typedef long long int64;
#define FOR(i,n)for(int i=0;i<(int)(n);i++)
char t[4][5];
bool check(){
  FOR(i,4){
    int cnt=0;
    FOR(j,4)cnt+=t[i][j]=='.'||t[i][j]=='O';
    if(cnt)continue;
    FOR(j,4)cnt+=t[i][j]=='X';
    if(cnt>=3)return true;
  }
  FOR(i,4){
    int cnt=0;
    FOR(j,4)cnt+=t[j][i]=='.'||t[j][i]=='O';
    if(cnt)continue;
    FOR(j,4)cnt+=t[j][i]=='X';
    if(cnt>=3)return true;
  }
  FOR(i,4){
    int cnt=0;
    FOR(j,4)cnt+=t[j][j]=='.'||t[j][j]=='O';
    if(cnt)continue;
    FOR(j,4)cnt+=t[j][j]=='X';
    if(cnt>=3)return true;
  }
  FOR(i,4){
    int cnt=0;
    FOR(j,4)cnt+=t[j][3-j]=='.'||t[j][3-j]=='O';
    if(cnt)continue;
    FOR(j,4)cnt+=t[j][3-j]=='X';
    if(cnt>=3)return true;
  }
  return false;
}
void solve(){
  FOR(i,4)scanf(" %s",t[i]);
  if(check())puts("X won");
  else{
    FOR(i,4)FOR(j,4)if(t[i][j]=='X')t[i][j]='O';else if(t[i][j]=='O')t[i][j]='X';
    if(check())puts("O won");
    else{
      bool found=false;
      FOR(i,4)FOR(j,4)found|=t[i][j]=='.';
      puts(found?"Game has not completed":"Draw");
    }
  }
}
main(){
  char in[100],out[100],*pos;
  strcpy(in,__FILE__);
  strcpy(out,__FILE__);
  pos=in;
  while(*pos!='.')pos++;
  strcpy(pos,".in");
  pos=out;
  while(*pos!='.')pos++;
  strcpy(pos,".out");
  freopen(in,"r",stdin);
  freopen(out,"w",stdout);
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    fprintf(stderr,"processing case %d\n",tt);
    printf("Case #%d: ",tt);
    solve();
    fflush(stdout);
  }
  freopen(out,"r",stdin);
  char c;while((c=getc(stdin))!=EOF)putc(c,stderr);
}

