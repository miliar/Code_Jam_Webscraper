#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

#define pii complex<int>


int cnt;

struct node {
    map <string, node*> next;
};

node *root;

void add(node *cur, string tmp, int idx) {
    if (tmp[idx] && tmp[idx] == '/') idx++;
    string next;
    while(tmp[idx] != '/' && tmp[idx]) {
        next += tmp[idx];
        idx++;
    }
    if (next.size() == 0) return;
    if (cur->next[next] == 0) {
        cnt++;
        cur->next[next] = new node();
    }
    add(cur->next[next], tmp, idx);
}

void solve() {
    int n, m;
    scanf("%d%d", &n, &m);
    db(n<<" "<<m);
    root = new node();
    rep (i, n) {
        char buf[111];
        scanf("%s", buf);
        db(buf);
        add(root, buf, 1);
    }
    cnt = 0;

    rep (i, m) {
        char buf[111];
        scanf("%s", buf);
        db(buf);
        add(root, buf, 1);
    }

    printf("%d", cnt);
}

int main(int argc, char ** argv) {
    //freopen("1.in","r",stdin); 
    //freopen("2.in","r",stdin); 
    //freopen("3.in","r",stdin); 

    //freopen("../A-small-attempt0.in","r",stdin);freopen("../A-small-attempt0.out","w",stdout);
    //freopen("../A-small-attempt1.in","r",stdin);freopen("../A-small-attempt1.out","w",stdout);
    //freopen("../A-small-attempt2.in","r",stdin);freopen("../A-small-attempt2.out","w",stdout);

    freopen("../A-large.in","r",stdin); freopen("../A-large.out","w",stdout);

    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    db(t);
    fo (i, 1, t) {
        cerr << "i"<< " " << i << endl;
        printf("Case #%d: ", i);
        solve();
        printf("\n");
        fflush(stdout);
        cerr.flush();
    }
	return 0;
}

