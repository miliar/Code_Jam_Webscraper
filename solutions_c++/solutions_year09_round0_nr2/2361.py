#include<iostream.h>
#include<fstream.h>

int map[105][105];

#define N(i,j) i-1][j
#define S(i,j) i+1][j
#define W(i,j) i][j-1
#define E(i,j) i][j+1


enum direc{sink,nth,wst,est,sth};

direc small(int i,int j)
{
  direc path=sink;
  int small=map[i][j];
  if(map[N(i,j)]<small)
  {
    small=map[N(i,j)];
    path=nth;
  }
  if(map[W(i,j)]<small)
  {
    small=map[W(i,j)];
    path=wst;
  }
  if(map[E(i,j)]<small)
  {
    small=map[E(i,j)];
    path=est;
  }
  if(map[S(i,j)]<small)
  {
    small=map[S(i,j)];
    path=sth;
  }
  return path;
}

int main()
{
//  ifstream ip("ip.txt");
  ifstream ip("ipb.txt");
  ofstream op("op.txt");

  int h,w,t,i,j,count,tests,r,c,fill;
  int result[105][105];
  direc to[105][105],path;

  ip>>tests;
  for(t=0;t<tests;t++)
  {
    ip>>h>>w;
    for(i=0;i<=h+1;i++)
    for(j=0;j<=w+1;j++)
    map[i][j]=10000;
    for(i=1;i<=h;i++)
    for(j=1;j<=w;j++)
    {
      ip>>map[i][j];
      result[i][j]=0;
    }
    count=1;
    for(i=1;i<=h;i++)
      for(j=1;j<=w;j++)
        to[i][j]=small(i,j);
/*
    for(i=1;i<=h;i++)
    {
      for(j=1;j<=w;j++)
      cout<<to[i][j]<<" ";
      cout<<endl;
    }
*/
    for(i=1;i<=h;i++)
    {
      for(j=1;j<=w;j++)
      {
        r=i;c=j;
        path=to[i][j];
        while(path!=sink)
        {
          switch(path)
          {
            case nth :
              r--;
              path=to[r][c];
              break;
            case wst :
              c--;
              path=to[r][c];
              break;
            case est :
              c++;
              path=to[r][c];
              break;
            case sth :
              r++;
              path=to[r][c];
              break;
          }
        }
        if(result[r][c]==0)
        result[r][c]=count++;

        fill=result[r][c];
/*
if(t==3)
{
    cout<<"i:"<<i<<" j:"<<j<<" r:"<<r<<" c:"<<c<<" fill:"<<fill<<endl;
}
*/
        r=i;c=j;
        result[r][c]=fill;
        path=to[i][j];
        while(path!=sink)
        {
          switch(path)
          {
            case nth :
              r--;
              result[r][c]=fill;
              path=to[r][c];
              break;
            case wst :
              c--;
              result[r][c]=fill;
              path=to[r][c];
              break;
            case est :
              c++;
              result[r][c]=fill;
              path=to[r][c];
              break;
            case sth :
              r++;
              result[r][c]=fill;
              path=to[r][c];
              break;
          }
        }
/*
if(t==3)
{
    cout<<"i:"<<i<<" j:"<<j<<" r:"<<r<<" c:"<<c<<" fill:"<<fill<<endl;
    for(int p=1;p<=h;p++)
    {
      for(int q=1;q<=w;q++)
      cout<<result[p][q]<<" ";
      cout<<endl;
    }
}
*/
      }
    }

    op<<"Case #"<<t+1<<":"<<endl;
    for(i=1;i<=h;i++)
    {
      for(j=1;j<=w;j++)
        op<<char(result[i][j]+96)<<" ";
      op<<endl;
    }
/*    
    cout<<"Case #"<<t+1<<":"<<endl;
    for(i=1;i<=h;i++)
    {
      for(j=1;j<=w;j++)
        cout<<char(result[i][j]+96)<<" ";
      cout<<endl;
    }
    */
  }  
  ip.close();
  op.close();
//  getchar();
  return 1;
}
