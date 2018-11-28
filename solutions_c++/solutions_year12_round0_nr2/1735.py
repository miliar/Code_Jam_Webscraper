#include <iostream>
using namespace std;

int main()
{
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  
  int T,i,j;

  cin>>T;
  for (i=1; i<=T; ++i)
    {
      int unsurprising_above[101];
      int surprising_above[101];
      int ans;
      int n,s,p;

      cin>>n>>s>>p;
      for (j=1; j<=n; ++j)
        {
          int sum;
          
          cin>>sum;
          switch (sum%3)
            {
              case 0: surprising_above[j]=(sum/3+1)>=p?1:0; break;
              case 1: surprising_above[j]=(sum/3+1)>=p?1:0; break;
              case 2: surprising_above[j]=(sum/3+2)>=p?1:0; break;
            }
          switch (sum%3)
            {
              case 0: unsurprising_above[j]=(sum/3)>=p?1:0;   break;
              case 1: unsurprising_above[j]=(sum/3+1)>=p?1:0; break;
              case 2: unsurprising_above[j]=(sum/3+1)>=p?1:0; break;
            }

          if (sum==0||sum==1) surprising_above[j]=-1;//冻结在unsurprising
        }
        
      //从unsurprising -> surprising看成是激发，共四种
      int count[4]={0};//unsurprising -> surprising
      
      for (j=1; j<=n; ++j)
        if (surprising_above[j]!=-1)
          ++count[(unsurprising_above[j]<<1)+surprising_above[j]];
      
      //激发的优先级：(0,1) (1,1) (0,0) (1,0)
      if (s<=count[1]) ans=count[3]+count[2]+s;
      else if (s<=count[1]+count[3]+count[0]) ans=count[1]+count[3]+count[2];
      else ans=count[1]+count[3]+(count[2]-(s-count[1]+count[3]+count[0]));
      for (j=0; j<=n; ++j)
        if (surprising_above[j]==-1&&unsurprising_above[j]==1)
          ++ans;
      
      cout<<"Case #"<<i<<": "<<ans<<endl;
    }

  fclose(stdin);
  fclose(stdout);
  
  return(0);
}
