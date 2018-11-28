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

ll a[3][3];
ll n,A,B,C,D,X,Y,M;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>TC;
    REP(tc,TC){
        memset(a,0,sizeof a);
        cin>>n>>A>>B>>C>>D>>X>>Y>>M;
        a[X%3][Y%3]++;
        REP(i,n-1){
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            a[X%3][Y%3]++;            
        }
        ll num=0;
        REP(i,3) REP(j,3) if(a[i][j]>=3) 
            num+=(a[i][j])*(a[i][j]-1)*(a[i][j]-2);
        REP(i1,3) REP(j1,3) 
            REP(i2,3) REP(j2,3)  if(i1!=i2 || j1!=j2)
                REP(i3,3) REP(j3,3)  if(i2!=i3 || j2!=j3) if(i1!=i3 || j1!=j3)
                if((i1+i2+i3)%3==0)
                    if((j1+j2+j3)%3==0)
                        num+=a[i1][j1]*a[i2][j2]*a[i3][j3];                        
        cout<<"Case #"<<tc+1<<": "<<num/6<<endl;
    }
    return 0;
}