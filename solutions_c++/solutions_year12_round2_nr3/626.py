#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <stack>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
double EPS=1e-10;
double EQ(double a,double b){
    return abs(a-b)<EPS;
}
void fast_stream(){
  std::ios_base::sync_with_stdio(0);
}

int T;
int as[101];
int N;

void check(map<ll,vector<int> > &m){
    for(map<ll,vector<int> >::iterator it=m.begin();it!=m.end();it++){
        if(it->second.size()<2)continue;
        vector<int> v[2];
        int a=it->second[0];
        int b=it->second[1];
        for(int k=0;k<N;k++){
            if((a>>k)&1){
                v[0].push_back(as[k]);
            }
        }
        for(int k=0;k<N;k++){
            if((b>>k)&1){
                v[1].push_back(as[k]);
            }
        }
        for(int k=0;k<2;k++){
            for(int l=0;l<v[k].size();l++){
                cout<<v[k][l];
                if(l==v[k].size()-1)cout<<endl;
                else cout<<" ";
            }
        }
        return;
    }
    cout<<"Impossible"<<endl;
}

void solve(){
    cin>>T;
    for(int p=0;p<T;p++){
        map<ll,vector<int> > m;
        cin>>N;
        for(int i=0;i<N;i++)cin>>as[i];
        for(int s=0;s<(1<<N);s++){
            ll sum=0;
            for(int i=0;i<N;i++)
                if((s>>i)&1)sum+=as[i];
            m[sum].push_back(s);
        }
        cout<<"Case #"<<p+1<<":"<<endl;
        check(m);
    }
}
