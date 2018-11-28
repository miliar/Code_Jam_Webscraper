#include<iostream>
#include<set>
#include<vector>
#include<math.h>
#include<algorithm>
#include<cstdio>
#include<map>
#include<stack>
#include<deque>
#include<queue>
#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)
using namespace std;
int main()
{
    int t,n,h,l,i,j,arr[10000],k,cas=0;
    int max,min;
    cin>>t;
    while(t--)
    {
              cin>>n>>l>>h;
              cas++;
              for(i=0;i<n;i++)
              cin>>arr[i];
              int count=0;
              int res[1000]={0};
              for(i=l;i<=h;i++)
              {
                               for(j=0;j<n;j++)
                               {
                                               
                                               max=MAX(i,arr[j]);
                                               min=MIN(i,arr[j]);
                                               if((max%min)==0)
                                               count++;
                                               }
                                               if(count==n)
                                               {res[k]=i;
                                               //cout<<res[k]<<" "<<k<<"\n";
                                               k++;}
                                               count=0;
                               }
                               int fin=0,re=res[0];
                               cout<<"Case #"<<cas<<": ";
                               for(i=0;i<k;i++)
                               {
                                               if(res[i]==0)
                                               fin++;
                                               if(res[i]<=re)
                                               re=res[i];
                                               }
                                               if(fin==k)
                                               cout<<"NO\n";
                                               else
                                               cout<<re<<"\n";
                                               k=0;
                               
              }
    return 0;
    }
