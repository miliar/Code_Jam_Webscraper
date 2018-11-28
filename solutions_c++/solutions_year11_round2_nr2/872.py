#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
long long t,T,n,d,res,i,p,l,r,m,pos;
bool flag;
double dpos,dm;
//double pos;
pair <long long , int > a[201];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (t=1; t<=T; t++)
    {
        cin>>n>>d;
        res=0;
        for (i=0;i<n;i++)
         cin>>a[i].first>>a[i].second;
        sort(a,a+n);
        l=0; r=1000000000000000;
        while (l!=r)
         {
             m=(l+r)/2;
             pos=a[0].first-m-d;
             flag=true;
             for (i=0; i<n;i++)
             {
                 p=a[i].second;
                   while (p!=0)
                   {
                       if (a[i].first+m-pos<d) {
                           flag=false;
                           break;
                       }

                       pos=min(max(pos+d,a[i].first-m),a[i].first+m);
                       p--;
                   }

                    if (!flag) break;
              }
              if (flag) r=m;
              else
              l=m+1;
         }
         //check for l-0.5
         dm=l-0.5;
         dpos=a[0].first-dm-d;
           flag=true;
             for (i=0; i<n;i++)
             {
                 p=a[i].second;
                   while (p!=0)
                   {
                       if (a[i].first+dm-dpos<d) {
                           flag=false;
                           break;
                       }

                       dpos=min(max(dpos+d,a[i].first-dm),a[i].first+dm);
                       p--;
                   }

                    if (!flag) break;
              }

         if (!flag) dm=l;
         cout<<"Case #"<<t<<":"<<" "<<dm<<endl;
    }
    return 0;
}
