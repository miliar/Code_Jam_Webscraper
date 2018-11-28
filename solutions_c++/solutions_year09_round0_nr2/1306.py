#include <string>
#include <iostream>
using namespace std;

char c,b[100][100];
int W,H,a[100][100];
int f(int x, int y, int val)
{
  if((x<0)||(y<0)||(x>=H)||(y>=W))
    return 0;
  return (a[x][y]<val)?1:0;
}

char fn(int x,int y)
{
  // cout<<"call sequence"<<x<<" "<<y<<"\n";
  if(b[x][y]<'a')
    {
      int flag=0;
      int m=a[x][y];
      if(f(x-1,y,m))
	{
	  flag=1;
	  m=a[x-1][y];
	}
      if(f(x,y-1,m))
	{
	  flag=2;
	  m=a[x][y-1];
	}
      if(f(x,y+1,m))
	{
	  flag=3;
	  m=a[x][y+1];
	}
      if(f(x+1,y,m))
	{
	  flag=4;
	  m=a[x+1][y];
	}
      switch(flag)
	{
	case 0: b[x][y]=c++;
	  break;
	case 1: b[x][y]=fn(x-1,y);
	  break;
	case 2: b[x][y]=fn(x,y-1);
	  break;
	case 3: b[x][y]=fn(x,y+1);
	  break;
	case 4: b[x][y]=fn(x+1,y);
	}
    }
  return b[x][y];
}
int main()
{
  int i,j,T,t;
  cin>>T;
  for(t=1;t<=T;t++)
    {
      c='a';
      cin>>H>>W;
      for(i=0;i<H;i++)
	for(j=0;j<W;j++)
	  {
	    cin>>a[i][j];
	    b[i][j]='A';
	  }
      for(i=0;i<H;i++)
	for(j=0;j<W;j++)
	  b[i][j]=fn(i,j);
      cout<<"Case #"<<t<<":\n";
      for(i=0;i<H;i++)
	{
	  for(j=0;j<W;j++)
	    cout<<b[i][j]<<" ";
	  cout<<"\n";
	}   
    }
}
