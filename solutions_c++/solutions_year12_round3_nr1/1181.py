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
VI v[1000];
bool ans;
int visited[1000];

void preprocess(){

}

bool input(){
    N =  ni();

    REP(i,N){
        int M = ni();
        //cout << M << endl;
        REP(j,M){
            int X = ni()-1;
            v[i].PB(X);
        }
    }
    return true;
}

void BFS(int start){
    REP(i,N){
        visited[i] = false;
    }

    queue<int> q;
    q.push(start);
    visited[start] = true;

    while(!q.empty()){
        int curr = q.front();
        q.pop();

        REP(i,v[curr].size()){
            int next = v[curr][i];
            if(visited[next]){
                ans = true;
                return;
            }
            else{
                visited[next] = true;
                q.push(next);
            }
        }
    }
}

void solve(){
    ans = false;
    REP(i,N){
        BFS(i);
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
        solve();
        REP(j,N){
            v[j].clear();
        }
        if(ans){
            printf("Case #%d: Yes\n",i+1);
        }
        else{
            printf("Case #%d: No\n", i+1);
        }
    }
    return 0;
}
