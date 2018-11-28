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

ll a,b,p;

vector<int> pr;
int c[1111];

int main(){
    FOR(i,2,1000){
        bool pri=true;
        for(int j=2;j*j<=i;j++)
            if(i%j==0){
                pri=false;
                break;
            }
        if(pri)
            pr.pb(i);
    }
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>TC;
    REP(tc,TC){
        cin>>a>>b>>p;
        int num=0;
        memset(c,0,sizeof c);
        FOR(i,a,b+1)if(!c[i]){
            num++;
            queue<int> q;
            q.push(i);
            while(!q.empty()){
                int e=q.front();
                c[e]=1;
                FOR(j,a,b+1) if(!c[j]){
                    REP(k,pr.size()) if(pr[k]>=p && j%pr[k]==0 && e%pr[k]==0){
                        c[j]=1;
                        q.push(j);
                    }
                }
                q.pop();
            }
        }
        cout<<"Case #"<<tc+1<<": "<<num<<endl;  
    }
    return 0;
}