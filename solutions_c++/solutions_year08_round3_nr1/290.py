#include <vector>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>

#define GETI ({int p;cin>>p;p;})
#define REP(i,st,end) for(typeof(st) i(st);i!=(end);i++)

using namespace std;
vector<int> freq;
int cmp(const int a,const int b){
    return freq[a]<freq[b];
}

void process(int t){
     
     int P,K,L;
     cin>>P>>K>>L;
     
     
     REP(i,0,L)  freq.push_back(GETI);
     
     int presses[1001];
     vector<int> sorted;
     
     REP(i,0,L) sorted.push_back(i);
     
     sort(sorted.begin(),sorted.end(),cmp);
     
    // REP(i,0,L) cout<<freq[sorted[i] ]<<" ";
     int p=1;
     int k=0;
     for(int i=L-1;i>=0;i--){
                if(p>P && k==0) {
                       cout<<"Case #"<<t<<": Impossible\n";
                       return;
                       }
                presses[sorted[i]]=p;
                k++;
                if(k==K)p++,k=0;
     }
     long long res=0;
     REP(i,0,L)res+= presses[i]*freq[i];
     
     cout<<"Case #"<<t<<": "<<res<<"\n";
     freq.clear();
     return;
}
int main(){
    
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    process(i+1);
    return 0;
}
