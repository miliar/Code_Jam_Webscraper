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
#define N 10024
pii v[N];
int n, D;
int pd[N];

int solve (int pos){
    if (pos == 0){
        return 2*v[0].fst;
    }
    int& ret = pd[pos];
    if (ret != -1) return ret;
    ret = 0;
    f (i, 0, pos){
        int x = solve (i);
        if (x >= v[pos].fst){
            ret = max (ret,min(v[pos].snd,v[pos].fst-v[i].fst)+v[pos].fst);
        }
    }
    return ret;
}



int main (){
    int t; cin >> t;
    f (test, 1, t+1){
        scanf("%d", &n);
        f (i, 0, n) scanf("%d %d", &v[i].fst, &v[i].snd);
        scanf("%d", &D);
        clr (pd, -1);
        int ans = 0;
        f (i, 0, n) ans = max (ans, solve(i));
        if (ans < D) ans = -1;
        printf("Case #%d: ", test);
        if (ans != -1) printf("YES\n");
        else printf("NO\n");
    }    

    return 0;
}
