#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    long T,t,r,n,m,jami=0,k=0,i,drmt,tmp,mt=0;
    cin>>T;
    for(t=1;t<=T;t++){
        cin>>r>>m>>n;
        vector<long> v(n);
        for(i=0;i<n;i++){cin>>v[i];jami+=v[i];}

        for(k=0,mt=0,i=0;i<r;i++){
            for(drmt=0,tmp=0;;k++,tmp=0){
                tmp=v[k%n];
                if(drmt+tmp<=m&&drmt+tmp<=jami)drmt+=tmp;
                else break;
            }
            mt+=drmt;
        }

        cout<<"Case #"<<t<<": "<<mt<<endl; jami=0;
    }

    return 0;
}
