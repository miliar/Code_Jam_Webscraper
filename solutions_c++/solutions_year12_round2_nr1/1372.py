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
int J[1000];
int Sum = 0;


void preprocess(){

}

bool input(){
    N = ni();
    REP(i,N){
        J[i] = ni();
        Sum += J[i];
    }

}

void solve(){
    double lim = 2*Sum;
    lim/=N;

    int nNew = 0;
    int sNew = 0;
    REP(i,N){
        if(J[i] <= lim){
            nNew++;
            sNew += J[i];
        }
    }
    double limNew = Sum + sNew;
    limNew/= nNew;

    REP(i,N){
        double ans = 100;
        if(J[i] <= lim){
            ans = ans*(limNew-J[i]);
            ans /= Sum;
        }
        else{
            ans = 0.0;
        }
        printf("%.6lf ", ans);
    }
    printf("\n");

}

int main(){
    #if LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    preprocess();
    int t = ni();
    REP(i,t){
        Sum = 0;
        input();
        printf("Case #%d: ", i+1);
        solve();
    }
    return 0;
}
