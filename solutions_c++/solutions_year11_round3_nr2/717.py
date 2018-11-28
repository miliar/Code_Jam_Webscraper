#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

long long T,L,t,N,C;
long long a[1000010];
long long b[1000010],p;


int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("out","w",stdout);
    long long h,i,j,k;
    //scanf("%d",&T);
    cin>>T;


    for(int h=1;h<=T;++h){
        //system("pause");
        cout<<"Case #"<<h<<": ";
        cin>>L>>t>>N>>C;
        for(int i=0;i<C;++i){
            cin>>a[i];
            a[i]<<=1;
        }
        int kkkk=0;
        for(int i=0;i<100;i++)kkkk++;
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
    for(int i=0;i<100;i++)
    a[i]=0;
    return 0;
}
