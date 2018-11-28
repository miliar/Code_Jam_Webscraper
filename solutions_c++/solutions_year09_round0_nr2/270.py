#include<cstdio>
#include<cstring>
char col[111111];
int fa[111111],a[111][111],dir[]={-1,0,0,1,0,-1,1,0};
int getroot(int a){
  if(a-fa[a])fa[a]=getroot(fa[a]);
  return fa[a];
}
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int n,m;
    scanf("%d%d",&n,&m);
    int i,j;
    for(i=0;i<n;++i)
      for(j=0;j<m;++j)
        scanf("%d",a[i]+j);
    for(i=0;i<n*m;++i)
      fa[i]=i;
    for(i=0;i<n;++i)
      for(j=0;j<m;++j){
        int pi=i,pj=j;
        for(;;){
          int k;
          int nexti=-2,nextj=-2,minn=a[pi][pj];
          for(k=0;k<4;++k){
            int ti=pi+dir[k],tj=pj+dir[k+4];
            if(0<=ti&&ti<n && 0<=tj&&tj<m && minn>a[ti][tj]){
              minn=a[ti][tj];
              nexti=ti;
              nextj=tj;
            }
          }
          if(nexti==-2&&nextj==-2)break;
          pi=nexti;
          pj=nextj;
          fa[getroot(i*m+j)]=getroot(pi*m+pj);
          if(getroot(pi*m+pj)-pi*m-pj)break;
        }
      }
    char collen=97;
    memset(col,0,sizeof(col));
    printf("Case #%d:\n",testi);
    for(i=0;i<n;++i){
      for(j=0;j<m;++j){
        if(!col[getroot(i*m+j)])
          col[getroot(i*m+j)]=collen++;
        putchar(col[getroot(i*m+j)]);
        putchar(' ');
      }
      putchar('\n');
    }
  }
  return 0;
}