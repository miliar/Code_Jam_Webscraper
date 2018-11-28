#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <map>
#define eps 1e-9
#define inf 0x7fffffff
#define N 1005
using namespace std;
int main()
{
    int n,i,j,m,t,s,p;
    freopen ("2.out","w",stdout);
    cin>>t;
    for (j=0;j<t;j++){
        cin>>n>>s>>p;
        int a[101]={0};
        m=0;
        p*=3;
        for (i=0;i<n;i++)cin>>a[i];
        sort (a,a+n);
        for (i=0;i<n;i++){
            if (a[i]==0){if (p==0)m++;continue;}
            if (a[i]==1){if (p==1)m++;continue;}
            if (a[i]-2>=p){m++;continue;}
            if (a[i]+4>=p && s ){s--;m++;}
            else if (a[i]+2>=p)m++;
            }
        cout<<"Case #"<<j+1<<": "<<m<<endl;
        }
    return 0;
}
