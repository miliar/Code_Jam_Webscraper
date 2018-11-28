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

int n,k,b,t;
int x[55],v[55];

int main(){
#ifdef LocalHost
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int TC;
    cin>>TC;
    REP(tc,TC){
        printf("Case #%d: ",tc+1);

        cin>>n>>k>>b>>t;
        REP(i,n) scanf("%d",x+i);
        REP(i,n) scanf("%d",v+i);

        int res = 0;
        int bad = 0;
        for(int i=n-1;i>=0;i--)if(x[i]+ll(t)*v[i]>=b){
            res += bad;
            k--;
            if(k==0) break;
        }else bad++;

        if(k) puts("IMPOSSIBLE");
        else cout<<res<<endl;
    }

    return 0;
}