#include<iostream>
#include<vector>
using namespace std;

int main(){
    int t;
    cin>>t;
    for(int cas=1;cas<=t;++cas){
        int n;
        cin>>n;
        vector<vector<int> > v(n,vector<int> (2));
        for(int i=0;i<n;++i){
            cin>>v[i][0]>>v[i][1];
        }
        int cont=0;
        for(int i=0;i<n;++i)
            for(int j=i+1;j<n;++j)
                if((v[i][0]>v[j][0] and v[i][1]<v[j][1]) or (v[i][0]<v[j][0] and v[i][1]>v[j][1]))++cont;
        
        cout<<"Case #"<<cas<<": "<<cont<<endl;
    }
}