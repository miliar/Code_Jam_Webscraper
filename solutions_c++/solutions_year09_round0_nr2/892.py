#include<cstdio>
#include<iostream>
using namespace std;
int chck(int Alt[100][100],int x,int y,int H,int W)
{  int f=1;
   if((x-1)>=0)  {  if(Alt[x-1][y]<Alt[x][y]) f=0; }
   if((y-1)>=0)  {  if(Alt[x][y-1]<Alt[x][y]) f=0; }
   if((x+1)<H)   {  if(Alt[x+1][y]<Alt[x][y]) f=0; }
   if((y+1)<W)   {  if(Alt[x][y+1]<Alt[x][y]) f=0; }
   return f;
}
int com(char Map[100][100],int H,int W)
{   int f=0,y,z;
    for(y=0;y<H;y++)
    {  for(z=0;z<W;z++)
        if(Map[y][z]=='0'){f=1; break;}
       if(f==1) break;
    }
    return f;
}
void low(int Alt[100][100],int x,int y,int H,int W,int &m,int &n)
{  m=0; n=0;
   if((x+1)<H)   {  m=x+1; n=y; }
   if((y+1)<W)   {  m=x; n=y+1; }
   if((y-1)>=0)  {  m=x; n=y-1; }
   if((x-1)>=0)  {  m=x-1; n=y; }
   if((x+1)<H)   {  if(Alt[x+1][y]<=Alt[m][n]) {m=x+1; n=y;} }
   if((y+1)<W)   {  if(Alt[x][y+1]<=Alt[m][n]) {m=x; n=y+1;} }
   if((y-1)>=0)  {  if(Alt[x][y-1]<=Alt[m][n]) {m=x; n=y-1;} }
   if((x-1)>=0)  {  if(Alt[x-1][y]<=Alt[m][n]) {m=x-1; n=y;} }
}
int main()
{
    int x,y,z,H,W,T,Alt[100][100],m,n; char c,Map[100][100],C[200];
    scanf("%d",&T);
    for(x=0;x<T;x++)
    {
       scanf("%d %d",&H,&W);
       for(y=0;y<H;y++)
         for(z=0;z<W;z++)
           scanf("%d",&Alt[y][z]);
       c='A';
       for(y=0;y<H;y++)
         for(z=0;z<W;z++)  Map[y][z]='0';
       for(y=0;y<H;y++)
       {  for(z=0;z<W;z++)
          {   if(chck(Alt,y,z,H,W))
              Map[y][z]=c++;
          }
       }
       while(com(Map,H,W))
       {   
           for(y=0;y<H;y++)
           {  for(z=0;z<W;z++)
             {  if(Map[y][z]!='0')
                {  if((y-1)>=0 && Map[y-1][z]=='0')  
                   {  low(Alt,y-1,z,H,W,m,n);  if(m==y && n==z) Map[y-1][z]=Map[m][n];}
                   if((z-1)>=0 && Map[y][z-1]=='0')  
                   {  low(Alt,y,z-1,H,W,m,n);  if(m==y && n==z) Map[y][z-1]=Map[m][n];}
                   if((y+1)<H && Map[y+1][z]=='0')   
                   {  low(Alt,y+1,z,H,W,m,n);  if(m==y && n==z) Map[y+1][z]=Map[m][n];}
                   if((z+1)<W && Map[y][z+1]=='0')   
                   {  low(Alt,y,z+1,H,W,m,n);  if(m==y && n==z) Map[y][z+1]=Map[m][n];}
               
               }
             }
           }
          
       }
       for(y=0;y<200;y++) C[y]='0';
       c='a';
       for(y=0;y<H;y++)
       {  for(z=0;z<W;z++)
          { if(C[Map[y][z]]=='0')
            {C[Map[y][z]]=c; c++;}
          }
       }
       for(y=0;y<H;y++)
         for(z=0;z<W;z++)
           Map[y][z]=C[Map[y][z]];
       printf("Case #%d:\n",x+1);
       for(y=0;y<H;y++)
       { cout<<Map[y][0];
         for(z=1;z<W;z++)
           cout<<" "<<Map[y][z];
         cout<<endl;
       }
     
    }
    return 0;
}
