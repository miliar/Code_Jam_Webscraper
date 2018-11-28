#include<iostream>
using namespace std;
int main(){
    int n,T,i,test=0;
    unsigned int x,val,min;
    long sum;
    //int i,j,T,t,temp,test=0,ta,tb,pa,pb,num,n,rob;
    cin>>T;
    while(T--){
        sum=0;
        x=0;
        min=0;
        cin>>n;
        for(i=0;i<n;i++){
            cin>>val;
            x=x^val;
            if(min==0 || min>val)min=val;
            sum+=val;
        }
        if(x!=0)cout<<"Case #"<<(++test)<<": NO"<<endl;
        else cout<<"Case #"<<(++test)<<": "<<(sum-min)<<endl;
    }
    return 0;
}

