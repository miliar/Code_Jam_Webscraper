#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<queue>
#include<set>
#include<sstream>
using namespace std;
char cad[9];
int n;
void procesa(int test){
    cout<<"Case #"<<test<<":";
    cin>>n;
    vector<int> v;
    for(int i=0;i<n;++i){
        cin>>cad;
        int temp=0;
        for(int j=0;j<n;++j)if(cad[j]=='1')temp=j+1;
        v.push_back(temp);
    }
    map<vector<int>,int> D;
    queue<vector<int> >Q;
    D[v]=0;
    Q.push(v);
    while(!Q.empty()){
        v=Q.front();
        Q.pop();
        bool ok=1;
        for(int i=0;i<n;++i)if(v[i]>i+1)ok=0;
        if(ok){
            cout<<" "<<D[v]<<endl;
            break;
        
        }
        vector<int> v2=v;
        for(int i=0;i<n-1;++i){
            swap(v[i],v[i+1]);
            if(D.find(v)==D.end()){
                D[v]=D[v2]+1;
                Q.push(v);
            }
            swap(v[i],v[i+1]);
        }
    }
}
int main(){
    int N;
    cin>>N;
    int test=1;
    while(N--){
        procesa(test++);
    }
}
