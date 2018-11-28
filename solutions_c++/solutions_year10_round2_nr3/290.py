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

const int mod = 100003;

int d[555][555];
int cc[555][555];
int c(int n,int m){
    if(m>n || m<0 || n<0) return 0;
    if(m==0 || n==m) return 1;
    if(cc[n][m]!=-1) return cc[n][m];    
    return cc[n][m]=(c(n-1,m-1)+c(n-1,m))%mod;
}
int go(int n,int pos){
    if(pos==1) return 1;
    if(d[n][pos]!=-1) return d[n][pos];
    int val = 0;
    FOR(i,1,n){
        val += ll(go(pos, i)) * c(n-pos-1,pos-i-1);
        val%=mod;
    }
    return d[n][pos]=val;
}

int main(){
#ifdef LocalHost
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    CL(d,-1);CL(cc,-1);
        
    int TC;
    cin>>TC;
    REP(tc,TC){
        int n;
        cin>>n;
        int res = 0;
        FOR(i,1,n){
            res += go(n,i);
            if(res>=mod) res-=mod;
        }
        printf("Case #%d: %d\n",tc+1,res);
    }

    return 0;
}