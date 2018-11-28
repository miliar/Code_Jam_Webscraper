#include<iostream>
using namespace std;
long long gcd(long long a,long long b){
    if(b==0)return a;
    else if(a<b)return gcd(b,a);
    else return gcd(b,a%b);}

int main(){
    long n,i=0,T,j,l;
    
    cin>>T;
    while(i<T){i++;
    long long sum=0;
    
    long long t[3]={0},t1[3],mint;
    cin>>n;
    for(j=0;j<n;j++){cin>>t[j];if(j==0)mint=t[j];else if(mint>t[j])mint=t[j];}
    long long gc=-1;
    for(j=0;j<n;j++){
        t1[j]=t[j]-mint;
        if(gc==-1&&t[j]!=0)gc=t1[j];
        else gc=gcd(gc,t1[j]);}
    if(gc!=0&&gc!=1){
        //cout<<mint<<" "<<gc<<endl;
        sum=gc-(mint%gc);
        sum=sum%gc;
        }
    cout<<"Case #"<<i<<": "<<sum<<"\n";
    }
    return 0;
    }
