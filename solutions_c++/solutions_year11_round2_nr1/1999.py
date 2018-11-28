#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <stack>
#include <string>
#include <map>
using namespace std;
double WP[120],OWP[120],OOWP[120];
int num[120];
int ww[120];
double R[120];
char mp[120][120];

int main()
{
    int t,n;

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    int cas=0;
    while(t--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
          scanf("%s",mp[i]);
        for(int i=0;i<n;i++)
          {
            int sum=0;
            int re=0;
           for(int j=0;j<n;j++)
           {
              if(mp[i][j]!='.')
              {
                  sum++;
                  if(mp[i][j]=='1')
                    re++;
              }

           }
          // cout<<sum<<endl;
           num[i]=sum;
           ww[i]=re;
           WP[i]=1.0*re/sum;
          }
          for(int i=0;i<n;i++)
            {
                int sum=0;
                double re=0.0;
                for(int j=0;j<n;j++)
                {
                    if(mp[i][j]!='.')
                    {
                        sum++;
                        if(mp[j][i]=='1')
                        {
                            re+=(ww[j]-1.0)*1.0/(num[j]-1);
                        }
                        else

                            re+=(ww[j])*1.0/(num[j]-1) ;
                    }

                }

                OWP[i]=re/sum;
                //cout<<OWP[i]<<endl;
            }
            for(int i=0;i<n;i++)
            {
                int sum=0;
                double re=0.0;
                for(int j=0;j<n;j++)
                {
                    if(mp[i][j]!='.')
                    {
                        sum++;
                        re+=OWP[j];
                    }

                }
                OOWP[i]=re/sum;
            }
           for(int i=0;i<n;i++)
             R[i]=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
          printf("Case #%d:\n",++cas);
          for(int i=0;i<n;i++)
            printf("%.7f\n",R[i]);
      }

    //fclose(stdin);
    //fclose(stdout);
    return 0;


}
