#include<iostream>
using namespace std;
int main(){
    int t,num=0,n,a[1000],b[1000],i,j,count;
    cin>>t;
    while(t--){
        cin>>n;
        for(i=0;i<n;i++)cin>>a[i]>>b[i];
        count=0;
        for(i=0;i<n;i++)
            for(j=i+1;j<n;j++)
                if((a[i]-a[j])*(b[i]-b[j])<0)count++;
        cout<<"Case #"<<++num<<": "<<count<<endl;;
        }
    return 0;
    }
