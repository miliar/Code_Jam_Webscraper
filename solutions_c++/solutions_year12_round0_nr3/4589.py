#include <iostream>
#include <math.h>
#include <cstdio>
#include <cassert>


using namespace std;

int firstdigit(int x) {
    while (x>=10) x/=10;
    return x;
}

int lg(int x) {
    int res=1;
    while (res<=x)
        res*=10;
    return res;
}

static bool vis[100010];


int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tests;
    cin >> tests;
    //cout << tests << endl;
    for (int test=0; test<tests; test++) {
        int ans=0,a,b;
        cin >> a >> b;
        for (int i=a; i<=b; i++) {
            int x=i, p=10;
            vis[i]=true;
            int lgg=lg(i);
            for (int j=0; j<lgg-1; j++) {
                x*=p;
                x+=x/lgg;
                x%=lgg;
                assert(x>=0);
                if (i>x && x<=b && x>=a && !vis[x]) {
                    ans++;

                }
                vis[x]=true;
            }
            p=10; x=i;
            for (int j=0; j<lgg-1; j++) {
                x*=p;
                x+=x/lgg;
                x%=lgg;
                vis[x]=false;
            }
            vis[i]=false;
        }
        cout << "Case #" << test+1 << ": " << ans << endl;
    }

    return 0;
}
