/*
ID: duongthan4
LANG: C++
TASK: test
*/
#include <iostream>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <bitset>
#define FOR(i,n) for (int i=0;i<n;i++)
#define FORF(i,a,n) for (int i=a;i<=n;i++)
#define FORR(i,n,a) for (int i=n;i>=a;i--)
#define RI(a) scanf("%d", &a);
#define RS(a) scanf("%s", &a);
#define RC(a) scanf("%c", &a);
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(a) a.begin(),a.end()
#define pii pair<int,int>
#define piii pair<pair<int,int>,int>
#define INFY 1000000000
#define MAXN 10001
using namespace std;
typedef long long LL;

int d[MAXN];
int l[MAXN];
vector<int> a[MAXN];

void solve(){
    int n, D;
    RI(n);
    FOR(i, n){
        a[i].clear();
        RI(d[i]);
        RI(l[i]);
    }
    
    RI(D);
    a[0].pb(d[0]);
    FORF(i, 1, n-1){
        FOR(j, i){
            FOR(k, a[j].size()){
                if(d[i]-d[j] <= a[j][k]){
                    a[i].pb(min(d[i]-d[j], l[i]));
                    break;
                }
            }
            if(a[i].size()>0) break;
        }
    }
    FOR(i, n){
        FOR(k, a[i].size()){
            if(D-d[i] <= a[i][k]){
                cout<<"YES";
                return;
            }
        }
    }
    cout<<"NO";
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TestCase;
    RI(TestCase);
    FOR(i, TestCase){        
        cout<<"Case #"<<i+1<<": ";
        solve();
        printf("\n");
    }
    return 0;
}
