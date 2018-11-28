#include<iostream>
#include<cstdlib>
#include<vector>
#include<climits>
#include<cctype>
#include<map>
#include<list>
#include<fstream>
#include<cstdio>
#include<algorithm>
#include<memory.h>
#include<cmath>
#include<queue>
#define L long long int
#define LD long double
#define pi 3.141592653589793238462643383
#define M 1000000007

using namespace std;

int main()
{
    int t,n,s,p,c,i,k=1,m1,m2;
    cin>>t;
    ofstream out("cjqra");
    while(t--)
    {
              cin>>n>>s>>p;
              int a[n];
              for(i=0;i<n;i++)
              cin>>a[i];
              sort(a,a+n);
              c=0;
              for(i=n-1;i>=0;i--)
              {
                                 if(p>=1)
                                 m1=3*p-2;
                                 else
                                 m1=0;
                                 if(a[i]>=m1)
                                 c++;
                                 else if(p>=2&&s>0&&a[i]>=3*p-4)
                                 {
                                 c++;
                                 s--;
                                 }
              }
              out<<"Case #"<<k<<": "<<c<<"\n";
              k++;
              
              
    }
    return 0;
}
