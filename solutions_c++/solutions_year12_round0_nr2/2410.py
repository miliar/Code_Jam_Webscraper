#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<list>
#include<queue>
#include<set>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int MAXN=110;

int n,p,s,c;
int t[MAXN];

int licz(int n,int s,int p){
    int w=0;
    REP(i,n){
        if (3*p-2 <= t[i]){
            w++;
        }
        else if (s>0 && 3*p-4 <= t[i] && t[i] >= 2){
            w++;
            s--;
        }
    }
    return w;
}

int main(){
    scanf("%d",&c);
    REP(i,c){
        scanf("%d%d%d",&n,&s,&p);
        REP(j,n){
            scanf("%d",&t[j]);
        }
        printf("Case #%d: %d\n",i+1,licz(n,s,p));
    }
}
