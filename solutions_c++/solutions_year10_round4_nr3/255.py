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

int a[111][111];

bool has(){
    REP(i,101) REP(j,101) if(a[i][j]) return 1;
    return 0;
}


int main(){
#ifdef LocalHost
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int TC;
    cin>>TC;
    REP(tc,TC){
        CL(a,0);
        int r;
        cin>>r;
        REP(i,r){
            int x1,x2,y1,y2;
            cin>>x1>>y1>>x2>>y2;
            FOR(x,x1,x2+1) FOR(y,y1,y2+1)
                a[x][y]=1;
        }
        int t = 0;
        while(has()){

            for(int x = 100;x>=1;x--) for(int y =100;y>=1;y--) if(a[x-1][y] && a[x][y-1]) a[x][y]=1;
            for(int x = 100;x>=1;x--) for(int y =100;y>=1;y--) if(!a[x-1][y] && !a[x][y-1]) a[x][y]=0;
            t++;
        }

        printf("Case #%d: %d\n",tc+1,t);
    }

    return 0;
}