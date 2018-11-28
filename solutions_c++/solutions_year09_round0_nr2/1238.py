#include <iostream>
#include <cstdio>
#include <string>

using std::cout ;

int map[200][200],out[200][200],times,h,w,d[4][2]={-1,0,0,-1,0,1,1,0};
int ans[200][200],cases=0;
bool vis[200][200];
int input (){
 int i,j ;
  scanf("%d %d",&h,&w);
  for(i=0;i<h;i++)
     for(j=0;j<w;j++)
     scanf("%d",&map[i][j]);    
}
int flowto(int r,int c){
 if(vis[r][c])return out[r][c];
 vis[r][c]=1;
 int i,min=-1,minr,minc;
 for(i=0;i<4;i++)
   if(r+d[i][0]>=0&&r+d[i][0]<h&&c+d[i][1]>=0&&c+d[i][1]<w&&
      map[r+d[i][0]][c+d[i][1]]<map[r][c]&&(min==-1||(map[r+d[i][0]][c+d[i][1]]<min))){
        min = map[r+d[i][0]][c+d[i][1]];
        minr=r+d[i][0],minc=c+d[i][1];                                                                                
      }

 if(min==-1)
 out[r][c]=r*w+c;
 else 
 out[r][c]=flowto(minr,minc);
 //printf("%d %d %d\n",r,c,out[r][c]);    
 return out[r][c];
}
int sol(){
 int i ,j,k,l ; 
 memset(vis,0,sizeof(vis));
 for(i=0;i<h;i++)
    for(j=0;j<w;j++)
      if(!vis[i][j])flowto(i,j);
 int A=0;
 for(i=0;i<h;i++)
    for(j=0;j<w;j++)
    if(out[i][j]>=0)
    {
      int T=out[i][j];
      for(k=0;k<h;k++)
         for(l=0;l<w;l++){
      if(out[k][l]==T){
        out[k][l]=-1;
        ans[k][l]=A;                         
      }                  
      }
      A++;               
    }
 cases++;
 printf("Case #%d:\n",cases);
 for(i=0;i<h;printf("\n"),i++)
 for(j=0;j<w;j++){
  if(j)printf(" ");
  printf("%c",'a'+ans[i][j]);
 }
 
         
}
int main (){
  scanf("%d",&times);
  while(times--){
    input ();
    sol();               
  }  
}
