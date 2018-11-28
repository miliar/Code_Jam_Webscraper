/*
  Name:
  Author:
  Date: 06-04-12 21:47
  Description:
  Time Limit:
*/

#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define REP(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define AND(a,b) ((a) & (b))
#define OR(a,b) ((a) | (b))
#define XOR(a,b) ((a) ^ (b))
#define sqr(x) ((x) * (x))

#define PI 3.1415926535897932385
#define INF 1000111222
#define EPS 1e-7
#define MAXN 1000

#define INP "B-small-attempt0.in"
#define OUT "B-small-attempt0.out"

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

int a, b, c, d, e, f, g, h;
int T, N, S, p, M[MAXN];

string SS[15][15][15];

int getMax(int score, int s){
    if(!s){
        if(score % 3 == 0) return score/3;
        else return score/3 + 1;
        }
    if(s){
        if(score >= 29 || score <= 2) return -1;
        if(score % 3 == 2) return score/3 + 2;
        else return score/3 + 1;
        }
    }

int getCount(string SS){
    int res = 0;
    FOR(i, 1, N){
        int s = SS[i] - '0';
        int tmp = getMax(M[i], s);
        //cout << "getmax " << M[i] << "  " << s << " "<< tmp << endl;
        if(tmp >= p) res++;    
    }
    return res;
}

void solve(){
    int res = 0, l = SS[N][S][1][0] - '0';
    FOR(i, 1, l){
        int tmp = getCount(SS[N][S][i]);
        //cout << SS[N][S][i] << endl << tmp << endl;
        res = max(res, tmp);
    }
        
    printf("%d\n", res);
    return;
    }
    
void Gen(){
    SS[1][1][1] = "11";
    SS[1][0][1] = "10";
    SS[2][1][1] = "201";
    SS[2][1][2] = "210";
    SS[2][0][1] = "100";
    SS[2][2][1] = "111";
    SS[3][0][1] = "1000";
    SS[3][3][1] = "1111";
    SS[3][1][1] = "3100";
    SS[3][1][2] = "3010";
    SS[3][1][3] = "3001";
    SS[3][2][1] = "3110";
    SS[3][2][2] = "3101";
    SS[3][2][3] = "3011";
    }

int main () {
    freopen(INP, "r", stdin); freopen(OUT, "w", stdout);
    Gen();
    scanf("%d", &T);
    FOR(i, 1, T){
        scanf("%d %d %d", &N, &S, &p);
        FOR(j, 1, N) scanf("%d", &M[j]);
        printf("Case #%d: ", i);
        solve();    
    }
    return 0;
    }
