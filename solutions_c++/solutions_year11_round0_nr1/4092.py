#include<stdio.h>
#include<memory.h>
int abs(int a){
  return a<0?-a:a;
}
struct DStruct{
  int pos;
  char type;
  DStruct *next;
  DStruct(){
    next=NULL;
  }     
};
int step(DStruct *que,DStruct *&first,DStruct *&second,int &posfirst,int &possecond,int j){
  int res,tres=res=abs(que[j].pos-posfirst)+1;
  if(second){
    int tmp=abs(second->pos-possecond);
    if(tres>tmp) tres=tmp;
    if(possecond>second->pos) tres=-tres;
    possecond+=tres;
  }
  first=first->next;
  posfirst=que[j].pos;
  return res;
}
int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w+",stdout);
  char C;
  int T,N,Pt,ps1,ps2,res;
  scanf("%d",&T);
  DStruct *O,*B,**DP;
  DStruct que[100];
  for(int i=0;i<T;i++){
    scanf("%d",&N);
    O=B=NULL;
    for(int j=0;j<N;j++){
      scanf("%c%c%d",&C,&C,&Pt);
      que[j].pos=Pt;
      que[j].type=C;
      if(C=='O') DP=&O;
      else DP=&B;
      if(*DP) (*DP)->next=&que[j];
      (*DP)=&que[j];
    }
    ps1=ps2=1;
    res=0;
    O=B=NULL;
    for(int j=0;j<N;j++){
      if(!O&&que[j].type=='O') O=&que[j];
      if(!B&&que[j].type=='B') B=&que[j];
      if(O&&B) break;
    }
    for(int j=0;j<N;j++){
      switch(que[j].type){
        case'B':res+=step(que,B,O,ps1,ps2,j);break;
        case'O':res+=step(que,O,B,ps2,ps1,j);break;
      }
    }
    printf("Case #%d: %d\n",i+1,res);
  }
  return 0;   
}
