#include<iostream>
using namespace std;
int map[210][210];
int cover(int x,int y,int x1,int y1)
{
   int i,j;
   for(i=y;i<=y1;i++)
     for(j=x;j<=x1;j++)
       map[i][j]=1;
}
int check()
{
  int i,j,k;
  int flag=0;
  for(i=1;i<=200;i++)
  { 
     for(j=1;j<=200;j++)
     if(map[i][j]==1) 
     {
       return 0;
     }                  
  }
  return 1;
}  
void move()
{
  int i,j,k;
  int flag=0;
  int mat[210][210];
  memcpy(mat,map,sizeof(map));
  for(i=1;i<=200;i++)
  { 
     for(j=1;j<=200;j++)
     {
       if(map[i][j]==0)                 
         if(map[i-1][j]==1&&map[i][j-1]==1) mat[i][j]=1;
      if(map[i][j]==1)   
        if(map[i-1][j]==0&&map[i][j-1]==0) mat[i][j]=0;
     }              
  } 
  memcpy(map,mat,sizeof(mat));
}
void show()
{
  int i,j,k;
  int flag=0;
  for(i=1;i<=10;i++)
  { 
     for(j=1;j<=10;j++)
       cout<<map[i][j]<<" ";
     cout<<endl;       
  } 
  cout<<endl;
}
int main()
{
  int i,j,k,r,t;
  int cnt=0;
  int x,y,x1,y1;
  freopen("C-small-attempt0.in","r",stdin); 
  freopen("out.txt","w",stdout); 
  scanf("%d",&t);
  for(int ii=0;ii<t;ii++)
  {
     cnt=0;
     memset(map,0,sizeof(map));
     scanf("%d",&r);
     for(i=0;i<r;i++)
     {
        scanf("%d%d%d%d",&x,&y,&x1,&y1);
        cover(x,y,x1,y1);
     }
    // show();
     while(1)
     {
        if(check()) break;
        move();
       // show();
        cnt++;
     } 
     printf("Case #%d: %d\n",ii+1,cnt);
  }
  //while(1);
  return 0;
}
