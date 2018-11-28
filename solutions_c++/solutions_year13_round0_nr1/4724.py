#include<iostream>
using namespace std;
class S
{
  public:
  char data[4][4];
  void getin()
  {
     for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
        cin>>data[i][j];
  }
  bool juge(char c)
{
  for(int i=0;i<4;i++)
    {
      int j=0;
      for(j=0;j<4;j++)
        if(data[i][j]!='T'&&data[i][j]!=c)
          break;
      if(j==4)
        return true;
    }
  for(int j=0;j<4;j++)
  {
    int i=0;
    for(i=0;i<4;i++)
      if(data[i][j]!='T'&&data[i][j]!=c)
        break;
    if(i==4)
      return true;
  }
  int i=0;
  for(i=0;i<4;i++)
    if(data[i][i]!='T'&&data[i][i]!=c)
        break;
  if(i==4)
    return true;
  for(i=0;i<4;i++)
    if(data[i][3-i]!='T'&&data[i][3-i]!=c)
        break;
  if(i==4)
    return true;
  return false;
}
  bool full()
 {
   for(int i=0;i<4;i++)
     for(int j=0;j<4;j++)
       if(data[i][j]=='.')
         return false;
   return true;
 }
};



int main()
{
  int t;
  S s;
 //freopen("A-small-attempt0.in","r",stdin);
  //freopen("out.ot","w",stdout);
  cin>>t;
  for(int k=1;k<=t;k++)
  {
   
    s.getin();
    if(s.juge('X'))
    {
      cout<<"Case #"<<k<<": X won\n";
    }
    else
    if(s.juge('O'))
    {
       cout<<"Case #"<<k<<": O won\n";
    }
    else
    if(s.full())
    {
      cout<<"Case #"<<k<<": Draw\n";
    }
    else
    {
      cout<<"Case #"<<k<<": Game has not completed\n";
    }

  }
  return 0;
}
