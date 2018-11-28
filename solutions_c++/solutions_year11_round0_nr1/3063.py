#include <cstdlib>
#include <iostream>

using namespace std;

int abs(int a)
{
    if(a<0)
      return -a;
    return a;
}

int main()
{
    freopen("s.txt","w",stdout);
    int p[105],p0[105],n,i,j,t,t1,t2,ans,op,bp,t3;
    char r[105];
    cin>>t;
    for(j=1;j<=t;j++)
    {
       cin>>n;
       ans=0;
       for(i=0;i<n;i++)
          cin>>r[i]>>p0[i];
       op=bp=1;
       for(i=0;i<n;i++)
       {
          if(r[i]=='O')
          {           
            p[i]=abs(p0[i]-op);
            op=p0[i]; 
          }
          else
          {
            p[i]=abs(p0[i]-bp);
            bp=p0[i]; 
          }
       }

       t2=t3=0;
       for(i=0;i<n-1;i++)
       {
          t1=p[i];
          t2=p[i+1];
          if(t3==0)
            t3=t1+1;

          ans+=(t1+1);
          if(r[i]==r[i+1])
             t3+=(t2+1);
          else
          {
             t2=t2-t3;
             if(t2<0)
                t2=0;
             t3=0;
             p[i+1]=t2;

          }      
       }
       ans+=(t2+1);
       cout<<"Case #"<<j<<": "<<ans<<endl;
    }
 

    return 0;
}
