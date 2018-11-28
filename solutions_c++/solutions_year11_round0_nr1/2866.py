using namespace std;
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <iostream>
#include <memory.h>
#define FOR(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FORab(i,a,n) for(__typeof(n) i=(a);i<=(n);i++)
#define FOR1(i,n) FORab(i,1,n)
#define pb push_back
#define ms(n,p) memset(n, (p), sizeof(n))
#define ms0(n) ms(n, 0)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
#define ABS(a) ((a)<0?(-(a)):(a))
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;cin>>t;
    FOR1(cno, t) {
        int time = 0;
        int now[2] = {1, 1};
        int leftTime[2] = {0, 0};
        int x;cin>>x;
        while(x--) {
            char a;int b;
            int r;
            cin>>a>>b;
            if(a == 'B') { r = 1; }
            else { r = 0; }
            int need = ABS(b-now[r]) - leftTime[r];
            if(need  < 0) need = 0;
            time += need+1;
            leftTime[r] = 0;
            leftTime[!r] += need+1;
            now[r] = b;
        }
        cout<<"Case #"<<cno<<": "<<time<<endl;
    }
    return 0;
}

