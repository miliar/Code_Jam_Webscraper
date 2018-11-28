/*
Author:MarsChenly
Date:2011.06.04
*/
#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

const double zero(1e-8);

double len[105];

int main()
{
      freopen("A.in","r",stdin);
      freopen("A.out","w",stdout);
      int task,cases(0);
      scanf("%d",&task);
      while (task--)
      {
            int X,N;
            double S,R,t;
            scanf("%d %lf %lf %lf %d",&X,&S,&R,&t,&N);
            memset(len,0,sizeof(len));
            len[0] = X;
            for (int i(0);i<N;i++)
            {
                  int x,y,z;
                  scanf("%d %d %d",&x,&y,&z);
                  len[z]+=y-x;
                  len[0]-=y-x;
            }
            double ans(0);
            for (int i(0);i<=100;i++)
                  while (len[i] > zero)
                  {
                        if (t > zero)
                        {
                              if ((R + i)*t > len[i])
                              {
                                    double times = len[i] / (R+i);
                                    ans = ans + times;
                                    t = t - times;
                                    len[i] = 0;
                              } else
                              {
                                    len[i] = len[i] - t*(R+i);
                                    ans = ans + t;
                                    t = 0;
                              }
                        } else
                        {
                              double times = len[i] / (S+i);
                              ans = ans + times;
                              len[i] = 0;
                        }
                  }
            ans = ans + zero;
            printf("Case #%d: %.7lf\n",++cases,ans);
      }
      return 0;
}
