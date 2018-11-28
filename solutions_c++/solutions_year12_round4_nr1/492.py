#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

#define DEBUG 0
#define max_n 10000
#define eps 0.0000001

int N;
int d[max_n];
int l[max_n];
int D;
int najnizej[max_n];

int main(){
    int z; scanf("%d",&z);
    FOR(Z,1,z+1){
        scanf("%d",&N);
        FOR(i,0,N){
            scanf("%d%d",&d[i],&l[i]);
        }
        scanf("%d",&D);
        najnizej[0]=d[0];
        FOR(i,1,N) najnizej[i]=0;
        FOR(i,1,N){
            FOR(j,0,i){
                if(najnizej[j]>=d[i]-d[j]){
                    najnizej[i] = max(najnizej[i], d[i]-d[j]);
                    najnizej[i] = min(najnizej[i],l[i]);        
                }
            }
        }
        bool flaga = false;
        FOR(i,0,N){
            if(najnizej[i]+d[i]>=D) flaga = true;
        }

        printf("Case #%d: ",Z);
        if(flaga) printf("YES\n");
        else printf("NO\n");
    }
}
