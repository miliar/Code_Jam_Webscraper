#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(){
  int t,u=1,r,k,l,n,x,s;
  for(scanf("%d",&t);u<=t;u++){
    vector<int> g;
    for(scanf("%d%d%d",&r,&k,&n),s=0;n;g.push_back(x),n--)scanf("%d",&x),s+=x;
    if(s<=k){printf("Case #%d: %d\n",u,s*r);continue;}
    for(s=0;r;r--){
      for(l=k;l>=g[0];rotate(g.begin(),g.begin()+1,g.end()))l-=g[0],s+=g[0];
    }
    printf("Case #%d: %d\n",u,s);
  }
}