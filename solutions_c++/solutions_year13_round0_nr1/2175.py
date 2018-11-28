#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <ctime>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <cmath>
#include <list>
#include <vector>
#include <iomanip>
#include <cctype>
#include <complex>
#include <iterator>
#include <ostream>
#include <bitset>
#define all(a) a.begin(),a.end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define clx complex<long double>
typedef long long ll;
typedef long double ldb;
typedef unsigned long long ull;

using namespace std;
int _bufint;
inline int in(){
    scanf("%d", &_bufint);
    return _bufint;
}
const ll LINF=~((1ll)<<63);
const int INF=~(1<<31);
struct pl{
    ll x,y,z;
    ll dx,dy,dz;
    ll nx, ny, nz;
    ll left, right;
    pl(int xx, int yy, int zz, int dxx, int dyy, int dzz){
        x=xx;
        y=yy;
        z=zz;
        dx=dxx;
        dy=dyy;
        dz=dzz;
        nx=x;
        ny=y;
        nz=z;
        left=-1, right=-1;
    }
    void step(int n){
        nx=x+dx*n;
        ny=y+dy*n;
        nz=z+dz*n;
    }
    ull dist(){
        return (ull)(nx*nx)+ull(ny*ny)+ull(nz*nz);
    }
};
/*
struct node{
    vector<int> cur;
    node(int a){
        cur.pb(a);
    }
    node(){
    }
};
const int maxn=1000000*4+100;
node tree[maxn];
node merge(node a, node b){
    node c;
    c.cur.assign(a.cur.size()+b.cur.size(),0);
    merge(a.cur.begin(), a.cur.end(), b.cur.begin(), b.cur.end(), c.cur.begin());
    return c;
}
int query(int v, int tl, int tr, int l, int r, int cr){
    if(l>r) return 0;
    if(tr==r && tl==l){
        return (upper_bound(tree[v].cur.begin(), tree[v].cur.end(), cr) - tree[v].cur.begin() - 1);
    }
    int tm=tl+(tr-tl)/2;
    return query(2*v, tl, tm, l, min(r, tm), cr) + query(2*v+1, tm+1, tr, max(l, tm+1), r, cr);
}
*/
int main(){
#ifdef SSU
    freopen("in1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    srand(time(0));

    int T=in();
    for(int t=1;t<=T;++t){
        int res=0;
        printf("Case #%d: ", t);
        vector<string> a;
        for(int i=0;i<4;++i){
            string s;
            cin>>s;
            a.pb(s);
        }
        char c='X';
        for(int i=0;i<4;++i){
            bool f=1;
            for(int k=0;k<4;++k){
                if(a[i][k]==c || a[i][k]=='T') continue;
                f=0;
                break;
            }
            if(f){
                res=1;
                break;
            }
            f=1;
            for(int k=0;k<4;++k){
                if(a[k][i]==c || a[k][i]=='T') continue;
                f=0;
                break;
            }
            if(f){
                res=1;
                break;
            }
        }
        bool ff=1;
        for(int i=0;i<4;++i){
            if(a[i][i]==c || a[i][i]=='T') continue;
            ff=0;
            break;
        }
        if(ff){
            res=1;
        }
        ff=1;
        for(int i=0;i<4;++i){
            if(a[i][3-i]==c || a[i][3-i]=='T') continue;
            ff=0;
            break;
        }
        if(ff){
            res=1;
        }
        //
        c='O';
        for(int i=0;i<4;++i){
            bool f=1;
            for(int k=0;k<4;++k){
                if(a[i][k]==c || a[i][k]=='T') continue;
                f=0;
                break;
            }
            if(f){
                res=2;
                break;
            }
            f=1;
            for(int k=0;k<4;++k){
                if(a[k][i]==c || a[k][i]=='T') continue;
                f=0;
                break;
            }
            if(f){
                res=2;
                break;
            }
        }
        ff=1;
        for(int i=0;i<4;++i){
            if(a[i][i]==c || a[i][i]=='T') continue;
            ff=0;
            break;
        }
        if(ff){
            res=2;
        }
        ff=1;
        for(int i=0;i<4;++i){
            if(a[i][3-i]==c || a[i][3-i]=='T') continue;
            ff=0;
            break;
        }
        if(ff){
            res=2;
        }
        if(res==0){
            bool r=1;
            for(int i=0;i<4;++i) for(int j=0;j<4;++j){
                if(a[i][j]=='.'){
                    r=0;
                    break;
                }
            }
            if(!r) res=3; //not complete
            else res=4;// draw
        }
        if(res==1){
            puts("X won");
        }
        if(res==2){
            puts("O won");
        }
        if(res==3){
            puts("Game has not completed");
        }
        if(res==4){
            puts("Draw");
        }

    }



    return 0;
}
