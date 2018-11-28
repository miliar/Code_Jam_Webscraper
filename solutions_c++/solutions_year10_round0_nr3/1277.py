#include <iostream>

using namespace std;
int t;
long long int g[1004];
long long sum[1004];
int next[1004];
long long int ic[1004];


int main()
{
    cin>>t;
    for(int i=0; i<t; i++) {
        long long int nic=0;
        long long a=0;
        int r,k,n;
        cin>>r>>k>>n;
        for(int j=0; j<n; j++) {
            cin>>g[j];
        }
        long long cs=g[0];
        int ce=0;
        int nxt=(ce+1)%n;
        while(cs+g[nxt]<=k && nxt!=0) {
            cs+=g[nxt];
            ce=nxt;
            nxt=(ce+1)%n;
        }
        next[0]=(ce+1)%n;
        sum[0]=cs;
        for(int j=1; j<n; j++) {
            int prev=(j-1+n)%n;
            cs-=g[prev];
            if(ce==prev){
              ce=j;
              cs=g[j];
            }
            nxt=(ce+1)%n;

            while(cs+g[nxt]<=k && nxt!=j) {
                cs+=g[nxt];
                ce=nxt;
                nxt=(ce+1)%n;
            }
            next[j]=nxt;
            sum[j]=cs;
        }

        a+=sum[0];
        ic[0]=sum[0];
        nic++;
        int pos=next[0];
        r--;
        while(pos!=0&&r>0){
            r--;
            a+=sum[pos];
            ic[nic]=sum[pos];
            nic++;
            pos=next[pos];
        }
        if(r){
           long long sc=a;
           long long nc=r/nic;
           a+=sc*nc;
           r=r%nic;
           while(r){
               a+=ic[pos];
               r--;
               pos++;
           }
        }
        cout<<"Case #"<<(i+1)<<": "<<a<<endl;
    }
    return 0;
}
