#include<cstdio>
#include<algorithm>
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
bool square(int64 x){
  int64 from=0,to=1LL<<31;
  while(from+1<to){
    int64 middle=(from+to)/2;
    if(middle*middle<=x)from=middle;else to=middle;
  }
  return from*from==x;
}
void solve(){
  char buf[130];
  scanf(" %s",buf);
  int n=strlen(buf),cnt=0;
  FOR(i,n)cnt+=buf[i]=='?';
  FOR(take,1<<cnt){
    int64 x=0;
    int next=0;
    FOR(i,n){
      x*=2;
      if(buf[i]=='?')x+=!(take&1<<next++);else x+=buf[i]-'0';
    }
    if(square(x)){
      next=0;
      FOR(i,n)if(buf[i]=='?')buf[i]='0'+!(take&1<<next++);
      puts(buf);
      return;
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
