#include<iostream>
using namespace std;

int T;
int A1,A2,B1,B2;


int gcd(int mx,int mn){
    if(mx<mn){
        mx^=mn^=mx^=mn;
    }
    if(mn<=0) return 1;
    if(mx>=2*mn) return 1;
    return !gcd(mn,mx-mn);
}

int first[1000010];
int last[1000010];

void sim(){
    int i;
    first[1] = 1;
    last[1] = 1;
    for(i=2;i<=1000000;++i){
        first[i] = first[i-1];
        while(gcd(i,first[i])) first[i]++;
        last[i] = last[i-1];
        while(!gcd(i,last[i]+1)) last[i]++;
    }
}



int main(){
    int i,j;
    
    sim();
    freopen("Clarge.in","r",stdin);
    freopen("Clarge.out","w",stdout);
    cin>>T;
    int cas = 0;
    while(T--){
        cin>>A1>>A2>>B1>>B2;
        long long res = 0;
        for(i=A1;i<=A2;++i){
            long long mn = B1>?first[i];
            long long mx = B2<?last[i];
            long long t1 = mx-mn+1;
            long long t2 = B2-B1+1;
            if(t2>0)
                res = res+t2;
            if(t1>0)
                res = res - t1;
            
            
        }
        ++cas;
        cout<<"Case #"<<cas<<": "<<res<<endl;
    }
    return 0;
}


