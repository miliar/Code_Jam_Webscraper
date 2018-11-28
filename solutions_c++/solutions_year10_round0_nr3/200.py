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

int r,k,n;
int a[1111];
int per[1111];
int   s[1111];

int main(){
#ifdef LocalHost
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int TC;
    cin>>TC;
    REP(tc,TC){
        scanf("%d %d %d",&r,&k,&n);
        REP(i,n) scanf("%d",a+i);
        REP(i,n){
            int p = i;
            int sum = 0;
            while(sum+a[p]<=k && (sum==0 || p!=i)) sum+=a[p],p=(p+1)%n;
            per[i] = p;
              s[i] = sum;
        }
        ll res = 0;
        int c = 0;
        while(r){
            res+=s[c];
            c = per[c];
            r--;
        }
        cout<<"Case #"<<tc+1<<": "<<res<<endl;
    }

    return 0;
}