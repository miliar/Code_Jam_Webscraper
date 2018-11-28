
/* Author: Mahesh */

#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <string.h>
#include <memory.h>
#include <cassert>
#include <climits>
#include <cfloat>
#include <sstream>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof((a).begin()) i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define SORT(v)                 sort(all(v))
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

/* Program Body starts here */

class Score{
    public:
        int a, b, c;
        Score(int a, int b, int c){
            this->a = a;
            this->b = b;
            this->c = c;
        }
        int min() {
            return std::min(std::min(a, b), c);
        }
        int max() {
            return std::max(std::max(a, b), c);
        }
        int isSurprising(){
            return max() == min() + 2;
        }
        int isGood(int p){
            return max() >= p;
        }

};


V<Score> getScores(int n) {
    V<Score> v;
    if (n%3==0){
        v.pb(Score(n/3, n/3, n/3));
    }
    if (n>=3 && n%3==0){
        v.pb(Score(n/3-1, n/3, n/3+1));
    }
    if (n%3==1){
        v.pb(Score(n/3, n/3, n/3+1));
    }
    if (n%3==2){
        v.pb(Score(n/3, n/3, n/3+2));
        v.pb(Score(n/3, n/3+1, n/3+1));
    }
    if (n>=4 && n%3==1) {
        v.pb(Score(n/3-1, n/3+1, n/3+1));
    }
    return v;

}

int dp[101][101];
int arr[101];
int N, SR, P;

int solve(int n, int s) {
    if (s<0) return -1;
    if (n==0){
        return -(s!=0);
    }
    int& ans = dp[n][s];
    if (ans!=-1) return ans;

    V<Score> v = getScores(arr[N-n]);
    ans = 0;
    rep(i, si(v)){
        if (v[i].max() <= 10){
            ans = max(ans, v[i].isGood(P) + solve(n-1, s-v[i].isSurprising()));
        }
    }
    return ans;
}

int ans;
int brute(int x, int s, int c) {
    if (x==N){
        if (s==SR){
            ans = max(c, ans);
        }
    }
    else{
        V<Score> v = getScores(arr[x]);
        rep(i, si(v)) {
            if (v[i].max()<=10)
                brute(x+1, s+v[i].isSurprising(), c+v[i].isGood(P));
        }
    }
}

int main()
{
    freopen("in.in", "r", stdin);
    freopen("o.txt", "w", stdout);
    int T=SS;
    rep(t, T) {
        N = SS, SR = SS, P = SS;
        rep(i, N) arr[i] = SS;
        fill(dp, -1);
        printf("Case #%d: %d\n", t+1, solve(N, SR));
    }
}




