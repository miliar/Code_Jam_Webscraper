#include<iostream>

using namespace std;
bool min(int,int,int,int);
void lebel(int,int);
void sink(int,int);
int Arr[100][100],W,H,cnt;
char label[100][100];
bool vis[100][100];

     
     
int main()
{
 int T,c=0;
 cin>>T;
 while(c++<T)
 {
  int i,j;
  cin>>H>>W;
  for(i=0;i<H;i++)
   for(j=0;j<W;j++)
    {
     cin>>Arr[i][j];
     vis[i][j]=false;
     }
    cnt=0;
  for(i=0;i<H;i++)
  {
   for(j=0;j<W;j++)
   {
    if(!vis[i][j])
    {
     sink(i,j);
     cnt++;
     }
    }
   }
    cout<<"Case #"<<c<<": \n";
    for(i=0;i<H;i++)
    {
     for(j=0;j<W;j++)
     {
       cout<<label[i][j];
       if(j<W-1)
         cout<<" ";
     }
    cout<<"\n";
    }
  }
  return 0;
}
    bool min(int x,int y,int x1,int y1)
{
 int mn=Arr[x][y],posx=-1,posy=-1;
 //int posx=-1,posy=-1;
 if(x-1>=0 && Arr[x-1][y]<mn)
     {posx=x-1;
      posy=y;
      mn=Arr[x-1][y];
     }
 if(y-1>=0 && Arr[x][y-1]<mn)
     {posx=x;
      posy=y-1;
      mn=Arr[x][y-1];
     }
 if(y+1<W && Arr[x][y+1]<mn)
     {posx=x;
      posy=y+1;
      mn=Arr[x][y+1];
     }
 if(x+1<H && Arr[x+1][y]<mn)
     {posx=x+1;
      posy=y;
      mn=Arr[x+1][y];
     }
 if(posx==x1 && posy==y1)
     return true;
 return false;
}
     
void lebel(int x,int y)
{
  label[x][y]=(char)('a'+cnt);
  vis[x][y]=true;
  if(x-1>=0 && Arr[x-1][y]>Arr[x][y] && min(x-1,y,x,y))
     lebel(x-1,y);
  if(y-1>=0 && Arr[x][y-1]>Arr[x][y] && min(x,y-1,x,y))
     lebel(x,y-1);
  if(y+1<W && Arr[x][y+1]>Arr[x][y] && min(x,y+1,x,y))
     lebel(x,y+1);
  if(x+1<H && Arr[x+1][y]>Arr[x][y] && min(x+1,y,x,y))
     lebel(x+1,y);
}
     
void sink(int x,int y)
{
     label[x][y]=(char)('a'+cnt);
     vis[x][y]=true;
     int mn=Arr[x][y];
     int posx=-1,posy=-1;
     if(x-1>=0 && Arr[x-1][y]<mn && !vis[x-1][y])
      {posx=x-1;
       posy=y;
       mn=Arr[x-1][y];
      }
     if(y-1>=0 && Arr[x][y-1]<mn && !vis[x][y-1])
      {posx=x;
       posy=y-1;
       mn=Arr[x][y-1];
      }
     if(y+1<W && Arr[x][y+1]<mn && !vis[x][y+1])
     {posx=x;
      posy=y+1;
      mn=Arr[x][y+1];
     }
     if(x+1<H && Arr[x+1][y]<mn && !vis[x+1][y])
     {posx=x+1;
      posy=y;
      mn=Arr[x+1][y];
     }
     if(posx==-1)
      lebel(x,y);
     else
      sink(posx,posy);
}

                     
    
