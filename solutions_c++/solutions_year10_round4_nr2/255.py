#pragma comment(linker, "/STACK:36777216")

#include <algorithm>
#include <iostream>
#include<stdio.h>
#include <string>
#include<sstream>   
#include<string.h>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>
#include<memory.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<int,pii> p3i;
typedef long double ld;
typedef vector<ld> vd;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define SORT(a) sort((a).begin(),(a).end())

struct T{
    int n,p;
    vector<vi> v;
    T(){}
    T(int N,int P){n=N;p=P;}
    void ccin(){
        v.clear();
        FOR(i,1,p+1){
            vi t(1<<(p-i));
            REP(j,1<<(p-i)) scanf("%d",&t[j]);
            v.pb(t);            
        }
    }
};

T t;
int m[1111];
const int inf = 1011111111;
int d[1111][11][11];

pair<T,T> split(T t){
    T t1(t.n/2,t.p-1),t2(t.n/2,t.p-1);
    t1.v.resize(t.p-1);
    t2.v.resize(t.p-1);
    REP(i,t.p-1){
        REP(j,t.v[i].size()){
            if(j<t.v[i].size()/2) t1.v[i].pb(t.v[i][j]);
            else t2.v[i].pb(t.v[i][j]);
        }
    }
    return pair<T,T>(t1,t2);
}

int solve(T t,int start = 0,int missed = 0,int level=0){
    REP(i,t.n) if(m[start + i] < missed) return inf;
    if(t.n==1) return 0;
    if(d[start][missed][level]!=-1) return d[start][missed][level];

    pair<T,T> x = split(t);

    int res = inf;

    res = min(res,solve(x.first,start,missed,level+1)+solve(x.second,start+x.first.n,missed,level+1)+t.v[t.p-1][0]);

    res = min(res,solve(x.first,start,missed+1,level+1)+solve(x.second,start+x.first.n,missed+1,level+1));


    return d[start][missed][level] = res;

}

int main(){
#ifdef LocalHost
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int TC;
    cin>>TC;
    REP(tc,TC){
        int p;
        cin>>p;
        int n = (1<<p);
        REP(i,n) scanf("%d",m+i);
        t =  T(n,p);
        t.ccin();
        CL(d,-1);

        printf("Case #%d: %d\n",tc+1,solve(t));  
    }

    return 0;
}