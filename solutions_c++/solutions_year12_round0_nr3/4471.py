//gskhirtladze

#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<queue>
#include<map>
#include<math.h>
#include<time.h>

using namespace std;

long long a,b,x,y,t,k,ans,r,l;
long long sa,sb,ba[1000],bb[1000];
long long i,j;
bool p;

main()
{
      freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
      cin>>t;
      for (k=1;k<=t;k++)
       {
                        cin>>r>>l;
                        ans=0;
                        for (x=r;x<=l;x++)
                         for (y=x+1;y<=l;y++)
                          {
                                             a=x; sa=0; while ( a>0 ) { ba[sa++]=a%10; a=a/10; }
                                             b=y; sb=0; while ( b>0 ) { bb[sb++]=b%10; b=b/10; }
                                             if (sa!=sb ) continue;
                                             for (i=0;i<sa;i++)
                                              {
                                                               p=true;
                                                               for (j=0;j<sa;j++)
                                                                if (ba[j]!=bb[(i+j)%sb])
                                                                 {
                                                                                        p=false;
                                                                                        break;
                                                                 }
                                                               if (p) { ans++; break; }
                                              }
                          }
                        cout<<"Case #"<<k<<": "<<ans<<endl;
       }
}
