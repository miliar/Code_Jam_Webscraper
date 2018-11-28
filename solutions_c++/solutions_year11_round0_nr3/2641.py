#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int main(){
    int nc;
    cin>>nc;
    for(int k=0;k<nc;k++){
        int n;
        cin>>n;
        vector <int> v;
        int s=0;
        int sum=0;
        for(int i=0;i<n;i++){
            int x;
            cin>>x;
            v.push_back(x);
            s=s^x;
            sum+=x;
        }
        cout<<"Case #"<<k+1<<": ";    
        if(s==0){
            sort(v.begin(),v.end());
            cout<<sum-v[0]<<endl;
        }
        else cout<<"NO"<<endl;
    }    
}
