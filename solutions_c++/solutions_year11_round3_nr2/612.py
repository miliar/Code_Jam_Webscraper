#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

long long T,L,t,N,C;
long long a[1010];
long long b[1010],p;

int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B.txt","w",stdout);
    long long h,i,j,k;
    scanf("%d",&T);
    for(h=1;h<=T;++h){
        cout<<"Case #"<<h<<": ";
        cin>>L>>t>>N>>C;
        for(i=0;i<C;++i){
            cin>>a[i];
            a[i]<<=1;
        }
        long long sum=0,tot;
        for(i=0,j=0;sum<t&&j<N;i=(i+1)%C,++j)
            sum+=a[i];
        if(sum>=t){
            tot=sum;
            p=0;
            b[p++]=sum-t;
            for(;j<N;i=(i+1)%C,++j){
                tot+=a[i];
                b[p++]=a[i];
            }
            if(p<=L){
                cout<<tot/2<<endl;
            }else{
                sort(b,b+p);
                sum=0;
                for(i=p-1;i>=p-L;--i)
                    sum+=b[i];
                cout<<sum/2+tot-sum<<endl;
            }
        }else{
            cout<<sum<<endl;
        }
    }
}
