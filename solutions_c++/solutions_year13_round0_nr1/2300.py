#include<cstdio>
#include<iostream>
#include<fstream>
using namespace std;
int l0,t,l1,l2,l3,l4,tx,ty;
string gar,a[5];
string m="XO";
bool over,f;
int win;
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("tic2.out","w",stdout);
  cin>>t;
  for(l0=1;l0<=t;l0++)
  {
    for(l1=0;l1<4;l1++)
      cin>>a[l1];
    //cin>>gar;
    over=true;
    win=-1;
    tx=-1;
    ty=-1;
    for(l1=0;l1<4;l1++)
      for(l2=0;l2<4;l2++)
        if(a[l1][l2]=='.')
          over=false;
        else if(a[l1][l2]=='T')
        {
          tx=l1;
          ty=l2;
        }
    for(l1=0;l1<2;l1++)
    {
      if(tx>-1)
        a[tx][ty]=m[l1];
      f=true;
      for(l2=0;l2<4;l2++)
        if(a[l2][l2]!=m[l1])
          f=false;
      if(f)
        win=l1;
      f=true;
      for(l2=0;l2<4;l2++)
        if(a[l2][3-l2]!=m[l1])
          f=false;
      if(f)
        win=l1;
      for(l2=0;l2<4;l2++)
      {
        f=true;
        for(l3=0;l3<4;l3++)
          if(a[l2][l3]!=m[l1])
            f=false;
        if(f)
          win=l1;
      }
      for(l2=0;l2<4;l2++)
      {
        f=true;
        for(l3=0;l3<4;l3++)
          if(a[l3][l2]!=m[l1])
            f=false;
        if(f)
          win=l1;
      }
    }
    cout<<"Case #"<<l0<<": ";
    if(win>-1)
      cout<<m[win]<<" won";
    else
    {
      if(over)
        cout<<"Draw";
      else
        cout<<"Game has not completed";
    }
    cout<<endl;
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
