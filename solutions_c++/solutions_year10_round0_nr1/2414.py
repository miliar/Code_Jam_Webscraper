#include <iostream>
#include <vector>
using namespace std;

typedef vector<bool> VB;

int main(){
    int t;
    cin>>t;
    for(int i=1;i<=t;++i){
        int n,k;
        cin>>n>>k;
        VB v(n,false);
        for(int j=0;j<k;++j){
            bool acaba=false;
            for(int l = 0;l<n and not acaba;++l){ 
                if(!v[l])acaba = true;
                if(v[l]) v[l]=false;
                else v[l]=true;
            }
        }
        cout<<"Case #"<<i<<": ";
        bool on = false;
        for(int j=0;j<n and v[j];++j)
            if(j==n-1)on = true;
        if(on)cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;
    }
}