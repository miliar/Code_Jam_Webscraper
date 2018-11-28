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
#define MAXN 1000
using namespace std;
typedef long long LL;

int rx[MAXN];
int ry[MAXN];

struct E{
    int r, i;
} e[MAXN];

bool cmp(E a, E b){
    return a.i < b.i;
}

void solve(){
    int n, w, l;
    cin >> n >> w >> l;
    FOR(i, n){
        cin >> e[i].r;
        e[i].i = i;
        e[i].r *= 2;
    }
    int x=0, y=0, b=0, t;
    while(1){
        std::random_shuffle(e, e+n);        
        b = 0;
        FOR(i, n){
            x = -e[i].r/2;
            y = 0;
            int k;
            FORF(j, i, n-1){
                if((x+e[j].r/2) > w) break;
                x += e[j].r;           
                y = max(y, e[j].r);
            }
            x = -e[i].r/2;
            FORF(j, i, n-1){
                if((x+e[j].r/2) > w) break;
                rx[e[j].i] = x+e[j].r/2;
                x += e[j].r;
                if(b==0) ry[e[j].i] = b;
                else{
                    ry[e[j].i] = b+y/2;
                }
                k = j;
            }
            i = k;
            t = b;
            if(b==0) b += y/2;
            else b+=y;
        }
        if(t<=l){    
            /*FOR(i, n)   {
                if(rx[i]<0 || rx[i]>w) {
                    cout<<"NOX";
                    return;
                }
                if(ry[i]<0 || ry[i]>l) {
                    cout<<"NOY";
                    return;
                }
            }     
            FOR(i, n)
            FORF(j, i+1, n-1){
                
            }
            cout<<"YES";*/
            FOR(i, n){
                if(i<n-1) cout<<rx[i]<<" "<<ry[i]<<" ";
                else cout<<rx[i]<<" "<<ry[i];
            }
            return;
        }
    }
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
