#include <cstdio>
#include <cstdlib>

using namespace std;

struct trainT{
  int dep,arr;
  char flag;
};

trainT sA[105],sB[105];
int na,nb;
int T;

int cmp(const void *_a,const void *_b){
  trainT *a,*b;
  a=(trainT *)_a;
  b=(trainT *)_b;
  return (a->dep)-(b->dep);
}

void init(){
  int i;
  int h,m;
  scanf("%d",&T);
  scanf("%d%d",&na,&nb);
  for (i=0;i<na;i++){
    scanf("%d:%d",&h,&m);
    sA[i].dep=h*60+m;
    scanf("%d:%d",&h,&m);
    sA[i].arr=h*60+m;    
    sA[i].flag=0;
  }
  for (i=0;i<nb;i++){
    scanf("%d:%d",&h,&m);
    sB[i].dep=h*60+m;
    scanf("%d:%d",&h,&m);
    sB[i].arr=h*60+m;    
    sB[i].flag=0;
  }
  
  qsort(sA,na,sizeof(sA[0]),cmp);
  qsort(sB,nb,sizeof(sB[0]),cmp);
  
  /*for (i=0;i<na;i++) printf("%d %d\n",sA[i].dep,sA[i].arr);
  for (i=0;i<nb;i++) printf("%d %d\n",sB[i].dep,sB[i].arr);*/
  
  sA[na].dep=sB[nb].dep=9999;
}

void moveT(int side,int k){
  int n,i;
  trainT *tl,*tr;
  if (side==0){
    tl=sA;
    tr=sB;
    n=nb;
  }else{
    tl=sB;
    tr=sA;
    n=na;
  }
  
  tl[k].flag=1;
  for (i=0;i<n;i++) if(tr[i].flag==0){
    if (tr[i].dep>=tl[k].arr+T){
      break;
    }
  }
  if (i<n){
    moveT((side+1)%2,i);
  }
  return;
}

void solve(){
  int a,b;
  int i,j;
  a=b=0;
  while (1){
    for (i=0;i<na;i++) if(sA[i].flag==0) break;
    for (j=0;j<nb;j++) if(sB[j].flag==0) break;
    if (i==na && j==nb) break;
    if (sA[i].dep<sB[j].dep){
      moveT(0,i);
      a++;
    }else{
      moveT(1,j);
      b++;
    }
  }
  printf("%d %d\n",a,b);
}

int main(){
  int n,i;
  scanf("%d",&n);
  for (i=1;i<=n;i++){
    init();
    printf("Case #%d: ",i);
    solve();
  }
  return 0;
}

