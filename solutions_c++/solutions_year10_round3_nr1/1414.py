#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<vector>
   using namespace std;

   int Ax[10020],Bx[10020];



   int main()
   {      freopen("Al.in","r",stdin);
          freopen("Al.out","w",stdout);
          int i,j,m,n,kase,T;

          cin>>T;

          kase=1;

          while(T--)
          {
                    cin>>n;

                    for(i=0;i<n;i++)
                              cin>>Ax[i]>>Bx[i];

                    int cnt=0;

                    for(i=0;i<n;i++)
                    {
                         for(j=i+1;j<n;j++)
                              {
                                      if(Ax[i]>Ax[j])
                                      {  if(Bx[i]<Bx[j])
                                                  cnt++;
                                      }
                                      else if(Ax[i]<Ax[j])
                                      {      if(Bx[i]>Bx[j])
                                                  cnt++;
                                      }
                              }
                    }
                    printf("Case #%d: %d\n",kase,cnt);
                    kase++;
          }
          return 0;
   }
