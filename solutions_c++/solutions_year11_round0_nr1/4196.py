#include <iostream>
#include <stdio.h>
using namespace std;

int rob[200];
int btn[200];
int tim[2];
int place[2];

int dist(int a , int b)
{
    int big = a>b?a:b;
  int small = a>b?b:a;
  return big-small+1;
}

int main()
{
  freopen("in.txt","r",stdin);

  int tt;
  int n;
  cin>>tt;
  // cout<<tt<<endl;
  for(int idx = 1;idx<=tt;++idx)
  {
    //cout<<tt<<endl;
    cin>>n;
    for(int i=0;i<n;++i)
    {
      char tem;
      int p;
      cin>>tem;
      cin>>p;
      
      if(tem=='O')
	rob[i] = 0;
      else
	rob[i] = 1;
      btn[i] = p;
    }
    tim[0]=tim[1]=0;
    place[0]=place[1]=1;
    
    for(int i=0;i<n;++i)
    {
      int rbt = rob[i];
      int plc = btn[i];
      int tm = tim[rbt]+dist(plc,place[rbt]);
      //   cout<<tm<<"--- "<<tim[!rbt]<<endl;
      if(tm>tim[!rbt])
	tim[rbt] = tm;
      else
	tim[rbt] = tim[!rbt]+1;
      place[rbt] = plc;
      //  cout<<rbt<<" "<<tim[rbt]<<" "<<place[rbt]<<endl;
    }
    cout<<"Case #"<<idx<<": "<<tim[rob[n-1]]<<endl;
    
  }
  
}
