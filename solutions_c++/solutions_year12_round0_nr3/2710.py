#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <map>
#define eps 1e-9
#define inf 0x7fffffff
#define N 1005
using namespace std;
int sj(int a,int b){
    int s=1,d=a,c=0,m=0,i;
    while (d/=10){c++;s*=10;}
    s*=10;
    for (i=a;i<=b;i++){
        if (i>s){s*=10;c++;}
        int y=10,x=0,z=c;
        int bb=0,ss[20],st=0;
        while (z--){
              int p,q,k=0;
              p=i%y*(s/y)+i/y;
              if (p<=b && p>i && p>s/10){
                         for (q=0;q<st;q++)if (p==ss[q]){k=1;break;}
                         if (k==1)continue;
                         ss[st++]=p;
                         x++;
                         bb=1;
                         }
              y*=10;
              }
        m+=x;
        }
    return m;
    } 
int main()
{
    int n,i,j,m,t;
    //freopen ("3.out","w",stdout);
    cin>>t;
    for (j=0;j<t;j++){
    int a,b;
    cin>>a>>b;
    m=0;
    m+=sj(a,b);
    cout<<"Case #"<<j+1<<": "<<m<<endl;
    }
    return 0;
}
