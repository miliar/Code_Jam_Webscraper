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

/*set<ll> t;
int add(string s){
    s+="/";
    int res = 0;
    ll h = 0;
    FOR(i,1,s.size()){
        h = 37*h + (s[i]-'a');
        if(s[i]=='/') if(!t.count(h))
            t.insert(h),res++;
    }
    return res;
}*/

set<string> t;
int add(string s){
    s+="/";
    int res = 0;
    string h="";
    FOR(i,1,s.size()){
        h.pb(s[i]);        
        if(s[i]=='/') if(!t.count(h))
            t.insert(h),res++;
    }
    return res;
}


int main(){
#ifdef LocalHost
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int TC;
    cin>>TC;
    REP(tc,TC){
        t.clear();
        int n,m;
        cin>>n>>m;
        string s;
        getline(cin,s);
        REP(i,n) getline(cin,s),add(s);
        int res = 0;
        REP(i,m) getline(cin,s),res+=add(s);
        printf("Case #%d: %d\n",tc+1,res);
    }

    return 0;
}