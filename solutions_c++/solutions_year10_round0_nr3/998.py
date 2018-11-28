#include<iostream>
using namespace std;

int main(){
    long r,n,k,i=0,t,j,l;
    //long long p;
    cin>>t;
    while(i<t){i++;
    long long sum=0;
    
    long g[1000][3]={0};
    cin>>r>>k>>n;
    for(j=0;j<n;j++)cin>>g[j][0];
    for(j=0;j<n;j++){l=j+1;g[j][1]=g[j][0];if(l>=n)l=l%n;
        while((g[j][1]+g[l][0]<=k)&&l!=j){g[j][1]=g[j][1]+g[l][0];l++;if(l>=n)l=l%n;}
        g[j][2]=l;
    }
    l=0;
    //for(j=0;j<n;j++)cout<<j<<" "<<g[j][0]<<" "<<g[j][1]<<" "<<g[j][2]<<endl;
    for(j=0;j<r;j++){sum+=g[l][1];l=g[l][2];}
    cout<<"Case #"<<i<<": "<<sum<<"\n";
    }
    return 0;
    }
