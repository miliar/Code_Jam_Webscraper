#include<iostream>
#include<iomanip>
#include<math.h>
using namespace std;

int main()
{
  int t,tc,n;
  double x1,y1,x2,y2,x3,y3,r1,r2,r3,ans,tmp;
  cin>>t;
  for(tc=1;tc<=t;tc++)
  {
    printf("Case #%d: ",tc);
    cin>>n;
    if(n==3)
    {
      cin>>x1>>y1>>r1;
      cin>>x2>>y2>>r2;
      cin>>x3>>y3>>r3;
      ans=r1+r2+sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
      ans = ans/2;
      ans=max(ans,r3);
      tmp=r3+r2+sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3));
      tmp = tmp/2;
      tmp = max(tmp,r1);
      if(tmp<ans)
	ans=tmp;
      
      tmp=r3+r1+sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3));
      tmp = tmp/2;
      tmp = max(tmp,r2);
      if(tmp<ans)
	ans=tmp;
      cout<<fixed;
      cout<<setprecision(6)<<ans<<endl;
    }
    else if(n==2)
    {
      cin>>x1>>y1>>r1;
      cin>>x2>>y2>>r2;
      cout<<fixed;
      cout<<setprecision(6)<<max(r1,r2)<<endl;
    }
    else if(n==1)
    {
      cin>>x1>>y1>>r1;
      cout<<fixed;
      cout<<setprecision(6)<<r1<<endl;
    }
  }
  return 0;
}