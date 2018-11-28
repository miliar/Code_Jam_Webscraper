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

int N,s,q;
map<string,int> m;
string name[111],se;
int x[1111][111];

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>N;
    REP(t,N){
        cin>>s;
        m.clear();
        int nm=0;
        getline(cin,name[0]);
        REP(i,s) getline(cin,name[i]),m[name[i]]=nm,nm++;
        cin>>q;
        memset(x,0,sizeof x);
        REP(i,s) x[0][i]=0;
        getline(cin,se);
        FOR(i,1,q+1){
            getline(cin,se);
            int pos=m[se];
            REP(j,s){
                x[i][j]=INF;
                REP(k,s)if(k!=pos) x[i][j]=min(x[i][j],x[i-1][k]+(j==k ?0 :1));
            }
        }
        int res=INF;
        REP(i,s) res=min(res,x[q][i]);

        printf("Case #%d: %d\n",t+1,res);
    }
	return 0;
}