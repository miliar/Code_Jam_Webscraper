#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int t;
    cin>>t;
    for (int ct=0;ct<t;++ct){
        int k,nd;
        cin>>k>>nd;
        vector<int> d(nd);
        for (int i=0;i<nd;++i){
            cin>>d[i];
            --d[i];
        }
        vector<int> v(k,-1);
        int cnt=0,nxt=0;
        for (int i=0;nxt<k && cnt<k;i=(i+1)%k) if (v[i]==-1){
            if (nxt==cnt){
                v[i]=nxt++;
                cnt=0;
            }
            else ++cnt;
        }
        cout<<"Case #"<<ct+1<<":";
        for (int i=0;i<d.size();++i) cout<<' '<<v[d[i]]+1;
        cout<<endl;
    }
}
