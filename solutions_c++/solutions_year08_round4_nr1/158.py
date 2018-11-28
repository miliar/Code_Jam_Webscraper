#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int treeA[10005][2];
int M,V;
int save[10005][2];

void init(){
  int i,t;
  scanf("%d%d",&M,&V);
  memset(save,-1,sizeof(save));
  t=(M-1)/2;
  for (i=0;i<t;i++){
    scanf("%d%d",&treeA[i][0],&treeA[i][1]);    
  }
  for (;i<M;i++){
    treeA[i][0]=-1;
    scanf("%d",&treeA[i][1]);
  }
}

int ask(int node,int v){
  int l,r,t;
  if (save[node][v]!=-1) return save[node][v];
  if (treeA[node][0]==-1){
    if (treeA[node][1]==v) save[node][v]=0; else save[node][v]=-2;
    return save[node][v];
  }

  save[node][v]=0x7fffffff;
  if (treeA[node][0]){
    if (v==0){
      l=ask(node*2+1,0);
      r=ask(node*2+2,1);
      if (l!=-2 && r!=-2){
        t=l+r;
      }else t=0x7fffffff;
      
      save[node][v]=min(save[node][v],t);
      
      l=ask(node*2+1,1);
      r=ask(node*2+2,0);
      if (l!=-2 && r!=-2){
        t=l+r;
      }else t=0x7fffffff;
      save[node][v]=min(save[node][v],t);
      
      l=ask(node*2+1,0);
      r=ask(node*2+2,0);
      if (l!=-2 && r!=-2){
        t=l+r;
      }else t=0x7fffffff;
      save[node][v]=min(save[node][v],t);

    } else{
      l=ask(node*2+1,1);
      r=ask(node*2+2,1);
      if (l!=-2 && r!=-2){
        t=l+r;
      }else t=0x7fffffff;
      save[node][v]=min(save[node][v],t);      
    }
  }else{
    if (v==0){
      l=ask(node*2+1,0);
      r=ask(node*2+2,0);
      if (l!=-2 && r!=-2){
        t=l+r;
      }else t=0x7fffffff;
      save[node][v]=min(save[node][v],t);
    }
    
    if (v==1){
      l=ask(node*2+1,0);
      r=ask(node*2+2,1);
      if (l!=-2 && r!=-2){
        t=l+r;
      }else t=0x7fffffff;
      save[node][v]=min(save[node][v],t);
      
      l=ask(node*2+1,1);
      r=ask(node*2+2,0);
      if (l!=-2 && r!=-2){
        t=l+r;
      }else t=0x7fffffff;
      save[node][v]=min(save[node][v],t);
      
      l=ask(node*2+1,1);
      r=ask(node*2+2,1);
      if (l!=-2 && r!=-2){
        t=l+r;
      }else t=0x7fffffff;
      save[node][v]=min(save[node][v],t);
    }
  }
  
  if (treeA[node][1]){
    treeA[node][0]=(!treeA[node][0]);
    
    if (treeA[node][0]){
      if (v==0){
        l=ask(node*2+1,0);
        r=ask(node*2+2,1);
        if (l!=-2 && r!=-2){
          t=l+r+1;
        }else t=0x7fffffff;
        
        save[node][v]=min(save[node][v],t);
        
        l=ask(node*2+1,1);
        r=ask(node*2+2,0);
        if (l!=-2 && r!=-2){
          t=l+r+1;
        }else t=0x7fffffff;
        save[node][v]=min(save[node][v],t);
        
        l=ask(node*2+1,0);
        r=ask(node*2+2,0);
        if (l!=-2 && r!=-2){
          t=l+r+1;
        }else t=0x7fffffff;
        save[node][v]=min(save[node][v],t);

      } else{
        l=ask(node*2+1,1);
        r=ask(node*2+2,1);
        if (l!=-2 && r!=-2){
          t=l+r+1;
        }else t=0x7fffffff;
        save[node][v]=min(save[node][v],t);      
      }
    }else{
      if (v==0){
        l=ask(node*2+1,0);
        r=ask(node*2+2,0);
        if (l!=-2 && r!=-2){
          t=l+r+1;
        }else t=0x7fffffff;
        save[node][v]=min(save[node][v],t);
      }
      
      if (v==1){
        l=ask(node*2+1,0);
        r=ask(node*2+2,1);
        if (l!=-2 && r!=-2){
          t=l+r+1;
        }else t=0x7fffffff;
        save[node][v]=min(save[node][v],t);
        
        l=ask(node*2+1,1);
        r=ask(node*2+2,0);
        if (l!=-2 && r!=-2){
          t=l+r+1;
        }else t=0x7fffffff;
        save[node][v]=min(save[node][v],t);
        
        l=ask(node*2+1,1);
        r=ask(node*2+2,1);
        if (l!=-2 && r!=-2){
          t=l+r+1;
        }else t=0x7fffffff;
        save[node][v]=min(save[node][v],t);
      }
    }
    
    treeA[node][0]=(!treeA[node][0]);
  }
  
  if (save[node][v]==0x7fffffff) save[node][v]=-2;
  return save[node][v];
}

int main(){
  int n,i,t;
  scanf("%d",&n);
  for (i=1;i<=n;i++){
    printf("Case #%d: ",i);
    init();
    t=ask(0,V);
    if (t==-2) printf("IMPOSSIBLE\n"); else printf("%d\n",t);
  }
  return 0;
}

