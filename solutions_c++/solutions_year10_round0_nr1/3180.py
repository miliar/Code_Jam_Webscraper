#include<cstdio>
#include<iostream>

using namespace std;

int pow2[31];
void calc(){
    pow2[1]=2;
    for(int i=2;i<=30;i++){
        pow2[i]=pow2[i-1]*2;
        //cout<<pow2[i]<<endl;
    }
}

int main(){
    int t,n,k,cases=0;
    calc();
    cin>>t;
    while(cases++<t){
        cin>>n>>k;
        k++;
        cout<<"Case #"<<cases<<": ";
        if(k%pow2[n]==0) cout<<"ON";
        else cout<<"OFF";
        cout<<endl;
    }
    return 0;
}
