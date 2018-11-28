#include <cstdio>
#include <cmath>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
int main()
{
          freopen("input5.txt","r",stdin);
          freopen("output2.txt","w",stdout);
          long N,i,j,T,t[101],S,p;
          scanf("%d",&T);
          long d;
          for (i=1; i<=T; i++)
          {
                    d=0;
                    scanf("%ld%ld%ld",&N,&S,&p);
                    for (j=1; j<=N; j++)
                    {
                              scanf("%d",&t[j]);
                    }
                    sort(t+1,t+N+1);

                    for (j=N; j>=1; j--)
                    {
                              if ( (t[j]>=max(p,3*p-2)) ) 
                              {
                                           d++;
                              }
                              else if ( (t[j]>=max(p,3*p-4)) && (S>0))
                              {
                                   d++;
                                   S--;
                              }
                    }
                    cout<<"Case #"<<i<<": "<<d<<endl;
          }
          //system("pause");
          return 0;
}
