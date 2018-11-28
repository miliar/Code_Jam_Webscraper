#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <queue>
#include <bitset>
#include <cmath>
#include <stack>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <cassert>
#include <iomanip>
using namespace std;
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define E 1e-9
#define FOR(i,ini,fin) for(int i=(int)ini;i<(int)fin;i++)

#define M 1000000000
#define P 100.0000000

typedef long long L;
typedef double D;
typedef pair<int,int>par;

struct triple{
    int x,y,z, may, sur;
};
int valor(int x, int y,int  z){
    return max(abs(x-y),max(abs(x-z),abs(y-z)));
}

int n,s,p, x[120];
vector<triple>v[32];
int dp[110][110];

int optimo(int ind, int usa){
    if(ind>=n){     //no avanzo mas
        if(usa==s)return 0; //caso base
        return -10000000;   //invalido
    }
    if(usa>s)return -1000000;
    if(dp[ind][usa]!=-1)return dp[ind][usa];
    int mejor=0, sw, m;
    FOR(i,0,v[x[ind]].size()){
        sw= (v[x[ind]][i].sur==1)?1:0;
        m= (v[x[ind]][i].may>=p)?1:0;
        mejor=max(mejor, m + optimo(ind+1, usa+sw));
    }
    return dp[ind][usa]=mejor;
}

int main(){
    triple t;
    FOR(i,0,11){
        FOR(j,0,11){
            FOR(k,0,11){
                int val=valor(i,j,k);
                if(val<=2){
                    t.x=i, t.y=j, t.z=k, t.may=max(i,max(j,k));
                    if(val>1)t.sur=1;
                    else t.sur=0;
                    v[i+j+k].pb(t);
                }
            }
        }
    }

    int casos;
    scanf("%d",&casos);
    FOR(i,0,casos){
        scanf("%d%d%d",&n,&s,&p);
        FOR(j,0,n)scanf("%d",&x[j]);
        memset(dp,-1,sizeof(dp));
        cout<<"Case #"<<i+1<<": "<<optimo(0,0)<<endl;;
    }
    return 0;
}


