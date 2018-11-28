#include <cstdio>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

typedef pair<int,int> pairii;
 
map< pairii ,int> save;
map< pairii ,bool> rock;
 
int move[2][2]={{-1,-2},{-2,-1}};
int H,W;

void init(){
  int i,r,x,y;
  pairii tp;
  
  scanf("%d%d%d",&H,&W,&r);
  rock.clear();
  save.clear();
  for (i=0;i<r;i++){
    scanf("%d%d",&x,&y);
    tp=pairii(x,y);
    rock[tp]=true;
  }
}

int DFS(int x,int y){
  int i,tx,ty,res=0;
  pairii tp,tp0;
  
  if (x==1 && y==1) return 1;
  tp0=pairii(x,y);
  if (save.find(tp0)!=save.end()) return save[tp0];
  for (i=0;i<2;i++){
    tx=x+move[i][0];
    ty=y+move[i][1];
    if (tx<=0 || ty<=0) continue;
    tp=pairii(tx,ty);
    if (rock[tp]==true) continue;
    res=res+DFS(tx,ty);
  }
  save[tp0]=res%10007;
  return res%10007;
}

int main(){
  int n,i;
  scanf("%d",&n);
  for (i=0;i<n;i++){
    init();
    printf("Case #%d: %d\n",i+1,DFS(H,W));
  }
  return 0;
}

