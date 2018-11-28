#include<iostream>
#include<set>
using namespace std;
int main(){
    int getTotalDigits(int);
    long int powerTen(int);
    int t;
    cin>>t;
    for(int i=0;i<t;++i){
            int r,s;
            cin>>r>>s;
            int k=getTotalDigits(r);
            int count=0;
           
            for(int j=r;j<=s;++j){
                    int m=j,cases=k-1,p=0,l=0;
                                    while(cases!=0){
                                             int a=m/10;
                                             int b=m%10;
                                             int y = (b*powerTen(k-1)+a);
                                             
                                             if( y<=s && y>=r && y!=j && l!=y) {
                                                 
                                                 count++;
                                                 //cout<<"j: "<<j<<"Y: "<<y<<endl;
                                                 l=y;
                                                 }
                                             cases--;
                                             m=y;
                                             }
    
                             r++;
                    }
                   
                    cout<<"Case #"<<i+1<<": "<<count<<endl;
            }
            
 
}
int getTotalDigits(int n){
    int ret=0;
    while(n!=0){
                n=n/10;
                ret++;
                }
    return ret;
}
long int powerTen(int n){
    long int s=1;
    for(int i=0;i<n;++i)s*=10;
    return s;
}
