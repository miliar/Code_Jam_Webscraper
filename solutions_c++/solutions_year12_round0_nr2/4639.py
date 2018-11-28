#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
int N, S, P;
#define NN 128
#define inf 123112412
int pd[NN][NN];
int v[NN];

int solve (int pos, int s){
    if (s < 0) return -inf;
    if (pos == N){
        if (s == 0) return 0;
        return -inf;
    }
    int& ret = pd[pos][s];
    if (ret != -1) return ret;
    ret = -inf;
    f (i, 0, 11){
        f (j, i, 11){
            int k = v[pos]-i-j;
            if (k < j || k > 10) continue;
            if (k-i > 2) continue;
            int aux = 0;
            if (k >= P) aux++;
            if (k-i == 2){
                ret = max (ret, aux+solve (pos+1, s-1));
            }
            else{
                ret = max (ret, aux+solve(pos+1,s));
            }
        }
    }
    return ret;
}



int main (){
    int test; cin >>test;
    f (t, 1, test+1){
        cin >> N >> S >> P;
        f (i, 0, N) cin >> v[i];
        clr (pd, -1);
        printf("Case #%d: %d\n", t, solve(0,S));
    }
   return 0;
}
