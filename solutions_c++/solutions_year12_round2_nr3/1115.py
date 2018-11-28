#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>

//DS
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>

#define LL          long long int
#define UL          unsigned long long int
#define MAX_INT     0x7fffffff
#define MOD         1000000007
#define LOCAL       1
#define DEBUG       1
#define REP(i,n)    for(int i = 0; i < (n); i++)
#define FOR(i,a,b,k)for(int i = (a); i < (b); i+=k)

#define PB push_back
#define F first
#define S second
#define PI pair<int,int>
#define MP(a,b) make_pair(a,b)
#define VI vector<int>
#define VPI vector<PI>

using namespace std;

int ni(){
    int v;
    scanf("%d", &v);
    return v;
}

int N;
int a[20];
int sum[10000000];

void preprocess(){

}

bool input(){
    N = ni();
    REP(i,N){
        a[i] = ni();
    }
    memset(sum, 0, sizeof(sum));
}

int getSum(int mask){
    int ret = 0;
    REP(i,N){
        if(mask & (1<<i)){
            ret += a[i];
        }
    }
    //cout << mask << " " << ret << endl;
    return ret;
}

void printSubset(int mask){
    REP(i,N){
        if(mask &(1<<i)){
            printf("%d ", a[i]);
        }
    }
    printf("\n");
}

void solve(){
    int Max = 1 << N;
    FOR(i,1,Max,1){
        int val = getSum(i);
        if(sum[val] == 0){
            sum[val] = i;
        }
        else{
            printSubset(sum[val]);
            printSubset(i);
            break;
        }
    }
}

int main(){
    #if LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    preprocess();
    int t = ni();
    REP(i,t){
        input();
        printf("Case #%d:\n", i+1);
        solve();
    }
    return 0;
}
