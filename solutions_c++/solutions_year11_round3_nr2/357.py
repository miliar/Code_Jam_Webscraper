#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)
long long dis[1010000];
int main()
{
     freopen("inputB.txt","r",stdin);
     freopen("output4.txt","w",stdout);
     long long t,i,j,k,n,cn=1,L,T,c,a,sum2;

     cin>>t;
     while(t--)
     {
           cin>>L>>T>>n>>c;
           FOR(i,c)
           {
               cin>>a;
               for(j=i;j<n;j+=c)
               {
                 dis[j]=a;
               }
           }
           long long sum=0,ans=0,sum1[1010];
           //FOR(i,n)cout<<dis[i]<<endl;


                FOR(i,n)
                {

                    sum+=dis[i]*2;
                 //   sum1[i]=sum;
                    //cout<<"SUM "<<sum<<endl;
                }
                //cout<<"SUM "<<sum<<endl;
           if(L==0)
           {
               ans=sum;
            }
            else
            {
                ans=1000000000000000000LL;
                vector<long long>v;
                long long currt=0;
                sum2=0;
                FOR(i,n)
                {

                    if(sum2>=T)
                    {
                        v.push_back(dis[i]);
                        //ans=min(ans,sum-dis[i]);
                    }
                    else
                    if(T>sum2&&T<=sum2+2*dis[i])
                    {
                        long long p=dis[i]-((T-sum2)/2);
                        long long sum22=sum2+(T-sum2+p);
                        ans=min(ans,sum-p);
                        v.push_back(p);
                    }

                    sum2+=2*dis[i];
                }

                sort(v.begin(),v.end());
                reverse(v.begin(),v.end());
                FOR(i,min(L,(long long)v.size()))
                {
                    sum-=v[i];
                }
                ans=sum;
            }
            /*else if(L==2)
            {
                ans=1e9;
                long long currt=0;
                sum2=0;
                FOR(i,n)
                {
                    if(sum2>=T)
                    {

                        //ans=min(ans,dis[i]+sum2);
                     //   sum3=sum2+dis[i];
                        FORab(j,i+1,n-1)
                        {
                            ans=min(ans,sum-dis[i]-dis[j]);

                        }


                    }
                    else if(T>sum2&&T<=sum2+2*dis[i])
                    {
                       long long p=dis[i]-((T-sum2)/2);
                        long long sum3=sum2+(T-sum2+p);
                        FORab(j,i+1,n-1)
                        {
                            ans=min(ans,sum-p-dis[j]);

                        }

                    }

                    sum2+=2*dis[i];

                }

            }*/
           cout<<"Case #"<<cn++<<": "<<ans<<endl;

     }
    return 0;
}
