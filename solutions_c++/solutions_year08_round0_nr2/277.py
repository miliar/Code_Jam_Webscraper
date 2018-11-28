#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue> 
#include <iostream>
#include <iterator>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <sstream>

#pragma comment(linker, "/STACK:60777216")

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n)
#define UNIQUE(v) SORT(c),v.erase(unique(v.begin(),v.end()),v.end())
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define ld long double
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define Y second
#define X first

#define INF 1000000000

int N,T;
int n[2];
int x1,x2,x3,x4;
vector<pii> v;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>N;
    REP(t,N){
        cin>>T>>n[0]>>n[1];
        v.clear();
        REP(i,n[0]){
            scanf("%d:%d %d:%d",&x1,&x2,&x3,&x4);
            v.pb(pii(x1*60+x2,2));
            v.pb(pii(x3*60+x4+T,0));
        }
        REP(i,n[1]){
            scanf("%d:%d %d:%d",&x1,&x2,&x3,&x4);
            v.pb(pii(x1*60+x2,3));
            v.pb(pii(x3*60+x4+T,1));
        }
        int t_a,t_b;    
        t_a=t_b=n[0]+n[1];
        SORT(v);
        REP(i,n[0]+n[1]+1) REP(j,n[1]+n[0]+1) if(i+j<t_a+t_b){
            int v1=i,v2=j;
            REP(k,v.size()){
                if(v[k].second==2) v1--;
                if(v[k].second==3) v2--;
                if(v[k].second==0) v2++;
                if(v[k].second==1) v1++;
                if(v1<0 || v2<0) break;
            }
            if(v1>=0 && v2>=0){
                t_a=i;t_b=j;
            }
        }            
        printf("Case #%d: %d %d\n",t+1,t_a,t_b);
    }
	return 0;
}