#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <math.h>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <complex>

#pragma comment(linker, "/STACK:60777216")

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(a) sort((a).begin(),(a).end())
#define UNIQUE(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())
#define ll long long
#define pb push_back
#define vi vector<int>
#define pii pair<int,int>
#define INF 1111111111
int TC;

int k,n,x;
int m[1111111];

struct P{
#define LEN 1048576
    
    int a[LEN];

    P(){memset(a,0,sizeof a);}
    void clear(){
        memset(a,0,sizeof a);
    }
    int init(int to,int v=LEN/2,int step=LEN/4){
        if(v<=to) a[v]=1;
        if(step) a[v]+=init(to,v-step,step/2);
        if(step) a[v]+=init(to,v+step,step/2);
        return a[v];       
    }
    void del(int val,int v=LEN/2,int step=LEN/4){
        a[v]--;
        if(val<v) del(val,v-step,step/2);
        if(val>v) del(val,v+step,step/2);
    }
    int num(int val,int v=LEN/2,int step=LEN/4){
        if(!step) return a[val];
        if(val<v) return num(val,v-step,step/2);
        if(val==v) return a[v]-a[v+step];
        if(val>v) return a[v]-a[v+step]+num(val,v+step,step/2);
    }
    int get(int val,int v=LEN/2,int step=LEN/4){
        if(!step) return v;
        if(a[v-step]>=val) return get(val,v-step,step/2);
        if(a[v]-a[v+step]>=val) return v;
        return get(val-(a[v]-a[v+step]),v+step,step/2);
    }
};

int main(){
 
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>TC;
    REP(tc,TC){
        cin>>k;
        P tree;
        tree.clear();
        tree.init(k);

        int pos=0;
        REP(i,k){
            int t=tree.num(pos)+i;
            t%=(k-i);
            pos=tree.get(t+1);
            m[pos]=i+1;
            tree.del(pos);
        }
     
        cout<<"Case #"<<tc+1<<":";
        cin>>n;
        REP(i,n){
            cin>>x;
            cout<<" "<<m[x];
        }
        cout<<endl;  
    }
    return 0;
}