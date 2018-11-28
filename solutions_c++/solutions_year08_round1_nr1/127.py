#include<iostream>
#include<vector>

using namespace std;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int T,n;
    
    cin>>T;
    
    long long prod;
    
    for(int i=0;i<T;i++){
        cin>>n;
        
        vector<int> x(n);
        vector<int> y(n);
        
        for(int j=0;j<n;j++) cin>>x[j];
        for(int j=0;j<n;j++) cin>>y[j];
        
        sort(x.begin(),x.end());
        sort(y.begin(),y.end());
        
        prod=0;
        
        for(int j=0;j<n;j++){
            prod+=x[j]*y[n-1-j];
        }
        
        cout<<"Case #"<<i+1<<": "<<prod<<endl;
    }
    
    return 0;
}
