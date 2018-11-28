#include<iostream>
using namespace std;
int main ()
{
  int k,k1;
  cin>>k;
  for(k1=0;k1<k;k1++)
  {
  int n,i,j,br2=0,br1=0,x=0,y=0,l=0,t=0,t1=0;
  char a[8][8];
  for(i=0;i<4;i++)
  for(j=0;j<4;j++)
  cin>>a[i][j];
  for(i=0;i<4;i++)
  {
    br1=br2=t=0;
    for(j=0;j<4;j++)
    {
      if(a[i][j]=='.')l=1;
      if(a[i][j]=='O')br1++;
      if(a[i][j]=='X')br2++;
      if(a[i][j]=='T')t=1;
      x=max(x,br1+t);
      y=max(y,br2+t);
    }
  }
  for(i=0;i<4;i++)
  {
    br1=br2=t=0;
    for(j=0;j<4;j++)
    {
      if(a[j][i]=='.')l=1;
      if(a[j][i]=='O')br1++;
      if(a[j][i]=='X')br2++;
      if(a[j][i]=='T')t=1;
      x=max(x,br1+t);
      y=max(y,br2+t);
    }
  }
  br1=br2=0;
  t=t1=0;
  for(i=0;i<4;i++)
  {
    if(a[i][i]=='O')br1++;
    if(a[i][i]=='T')t=1;
    if(a[i][i]=='X')br2++;
  }
  x=max(x,br1+t);
  y=max(y,br2+t);
  br1=br2=t=0;
  for(i=0;i<4;i++)
  {
    if(a[i][4-i-1]=='O')br1++;
    if(a[i][4-i-1]=='T')t=1;
    if(a[i][4-i-1]=='X')br2++;
  }
  x=max(x,br1+t);
  y=max(y,br2+t);
  ///cout<<x<<" "<<y<<endl;
  cout<<"Case #"<<k1+1<<": ";
  if(y==4)cout<<"X won"<<endl;
  else if(x==4)cout<<"O won"<<endl;
  else if(l==1)cout<<"Game has not completed"<<endl;
  else cout<<"Draw"<<endl;
  }
  return 0;
}