#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;

#define MAXN 1020000
int parent[MAXN], rank[MAXN];

void init(int n) {
    FOR(i, n) {
        rank[i] = 0;
        parent[i] = -1;
    }
}

int find(int vertex) {
    if(parent[vertex] == -1) return vertex;
    else {
        int store = find(parent[vertex]);
        parent[vertex] = store;
        return store;
    }
}

inline void join(int a, int b) {
    int ap, bp;
    ap = find(a);
    bp = find(b);

    if(ap == bp) return;
    if(rank[ap] > rank[bp]) parent[bp] = ap;
    else if(rank[bp] > rank[ap]) parent[ap] = bp;
    else {
        parent[bp] = ap;
        rank[ap]++;
    }
}

bool prime[2000000];
bool burnt[MAXN];

int main() {
    FOR(i, 2000000) prime[i] = true;
    prime[0] = prime[1] = false;
    for(int i = 2; i < 2000000; i++) {
        if(prime[i]) {
            for(int j = 2; i * j < 2000000; j++) {
                prime[i*j] = false;
            }
        }
    }

    int tests;
    cin >> tests;
    FOT(_t, 1, tests+1) {
        ll A, B, P;
        cin >> A >> B >> P;
        int n = B - A + 1;
        init(n);
        FOR(i, n) burnt[i] = false;
        for(int p = P; p < 2000000; p++) {
            if(prime[p]) {
             //   cerr << p << endl;
                for(ll m = A / p; m * p <= B; m++) {
                    ll what = m * p;
                    if(what >= A && what <= B) {
                        burnt[what-A] = true;
                        if(what + p <= B) join(what-A, what-A+p);
                    }
                }
            }
        }
     //   cerr << "here" << endl;
    int sets = 0;
    FOR(i, n) if(parent[i] == -1) sets++;
    cout << "Case #" << _t << ": " << sets << endl;
    }
    return 0;
}




