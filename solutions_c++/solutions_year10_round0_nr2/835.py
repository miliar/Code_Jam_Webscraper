#include <iostream>
#include <cstring>
#include <fstream>
#include <cmath>
using namespace std;
ofstream fout("pro2.out");
long long T,N,cnt;
long long num[3];
long long gcd(long a,long b){
     if(b==0) return a;
     else return gcd(b,a%b);
}
void solve(){
     if(N==2){
              long long temp=abs(num[0]-num[1]);
              if(num[0]%temp!=0) cnt=temp-num[0]%temp;
              else cnt=0;
     }
     if(N==3){
              long long temp=gcd(abs(num[0]-num[1]),abs(num[1]-num[2]));
              if(num[0]%temp!=0) cnt=temp-num[0]%temp;
              else cnt=0;
     }
}
int main(){
    cin>>T;
    for(int i=1;i<=T;i++){
            cin>>N;
            for(int j=0;j<N;j++){
                    cin>>num[j];
            }
            solve();
            fout<<"Case #"<<i<<": "<<cnt<<endl;
    }
}
            
          
