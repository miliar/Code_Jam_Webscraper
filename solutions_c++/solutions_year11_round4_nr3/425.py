#include<iostream>
#include<stdio.h>
#include<cmath>

using namespace std;

bool m[1000001];

int main(){
    freopen("C-large.in","r",stdin);
    freopen("x.out","w",stdout);
    m[1]=true;
    for(int i=2;i<=1000000;i++)
        if(!m[i])
            for(int j=2;i*j<=1000000;j++)
                m[i*j]=true;
    long long tc,n;
    cin>>tc;
    for(int t=1;t<=tc;t++){
        cin>>n;
        int res=0;
        if(n>1){
            for(int i=2;(long long)i*i<=n;i++)
                if(!m[i])
                    for(long long a=i;a*i<=n;a*=i)res++;
            res++;
        }
        printf("Case #%d: %d\n",t,res);
    }
    return 0;
}
