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
int W,L,U,G;
typedef pair<long double,long double> p2;
vector<p2> lower,upper;
long double area(p2 a,p2 b){
#define EPS 1e-9
  assert(a.first<b.first+EPS);
  return (double)(b.first-a.first)*(a.second+b.second)/2;
}
long double area(long double x,p2 a,p2 b){
  if(x<a.first)return 0;
  if(x>b.first)return area(a,b);
  double len=b.first-a.first;
  p2 c(x,b.second*(x-a.first)/len + a.second*(b.first-x)/len);
  return area(a,c);
}
void solve(){
  scanf("%d %d %d %d",&W,&L,&U,&G);
  lower.clear();
  upper.clear();
  FOR(i,L){
    int x,y;
    scanf("%d %d",&x,&y);
    lower.push_back(p2(x,y));
  }
  FOR(i,U){
    int x,y;
    scanf("%d %d",&x,&y);
    upper.push_back(p2(x,y));
  }
  long double total=0;
  FOR(i,lower.size()-1)total-=area(lower[i],lower[i+1]);
  FOR(i,upper.size()-1)total+=area(upper[i],upper[i+1]);
  for(int i=1;i<G;i++){
    long double desired=total*i/G;
    long double from=0,to=W;
    FOR(z,300){
      long double middle=(from+to)/2;
      long double cur=0;
      FOR(i,lower.size()-1)cur-=area(middle,lower[i],lower[i+1]);
      FOR(i,upper.size()-1)cur+=area(middle,upper[i],upper[i+1]);
      if(cur>desired)to=middle;else from=middle;
    }
    printf("%.8lf\n",(double)from); 
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
    printf("Case #%d:\n",tt);
    solve();
    fflush(stdout);
  }
  freopen(out,"r",stdin);
  char c;while((c=getc(stdin))!=EOF)putc(c,stderr);
}
