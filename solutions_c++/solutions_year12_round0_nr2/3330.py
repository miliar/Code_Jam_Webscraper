#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

int v[1000];
int n,p;
int re;



int main()
{
    freopen("B-large.in","r",stdin);
     freopen("outBL.txt","w",stdout);
     int cas,s,t;
     cas=0;

     scanf("%d",&t);
     while(t--)
     {

          scanf("%d%d%d",&n,&s,&p);
          for(int i=0;i<n;i++)
            scanf("%d",&v[i]);
          re=0;
          for(int i=0;i<n;i++)
          {
              if(v[i]%3==0)
              {
                  if(v[i]/3>=p)
                    re++;
                  else if((v[i]+3)/3>=p&&s>0&&v[i]>=3)
                  {
                      re++;
                      s--;
                  }

              }

              else if(v[i]%3==1)
                 {
                     if((v[i]+2)/3>=p)
                       re++;
                 }
              else
                  {
                      if((v[i]+1)/3>=p)
                        re++;
                      else if((v[i]+4)/3>=p&&s>0)
                      {
                          re++;
                          s--;
                      }

                  }



          }
          //cout<<re<<endl;
          printf("Case #%d: %d\n",++cas,re);

     }
    return 0;


}
