#include<iostream>
using namespace std;
int main(){
    long long n,res,p,k,l,w[1002];
    cin >> n;
    for(long long i=1;i<=n;i++){
               cin >> p>>k>>l;
               for(long long j=0;j<l;j++)
                       cin >> w[j];
               sort(w,w+l,greater<long long>());
               res=0;
               for(long long j=0;j<l;j++)
                        res+=(1+j/k)*w[j];
               cout << "Case #"<< i<<": "<<res<<endl;                                                    
            };
    
return 0;
};
