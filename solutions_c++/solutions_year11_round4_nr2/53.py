#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

const int maxn = 1010;
int a[maxn][maxn];
int64 dx[maxn][maxn];
int64 dy[maxn][maxn];
int64 m[maxn][maxn];

int main(){
    int T; cin >> T;
    for (int _ = 0; _ < T; _++){
        Eo(_);
        printf("Case #%d: ",_+1);
        int h,w,d; cin >> h >> w >> d;
            string s;
        for (int i = 0; i < h; i++){
            cin >> s;
            for (int j = 0; j < w; j++){
                a[i][j] = s[j]-'0'+d;
            }
        }
        for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                dx[i+1][j+1] = a[i][j]*j-dx[i][j]+dx[i+1][j]+dx[i][j+1];
                dy[i+1][j+1] = a[i][j]*i-dy[i][j]+dy[i+1][j]+dy[i][j+1];
                m[i+1][j+1] = a[i][j]-m[i][j]+m[i+1][j]+m[i][j+1];
            }
        }
        int q = min(h,w);
        bool done = false;
        for (;!done && q>=3;q--){
        //    Eo(q);
            int64 num = (q*q)-4;
            for (int i = 0;!done&& i+q <= h; i++){
                for (int j = 0; !done&&j+q <= w; j++){
 //                   Eo(i);Eo(j);
                    int64 mass = m[i+q][j+q]+m[i][j]-m[i+q][j]-m[i][j+q]
                        -a[i][j]
                        -a[i+q-1][j]
                        -a[i][j+q-1]
                        -a[i+q-1][j+q-1];
//                    Eo(mass); Eo(m[i][j]); Eo(m[i+q][j+q]); Eo(m[i][j+q]); Eo(m[i+q][j]);
                    int64 x = dx[i+q][j+q]+dx[i][j]-dx[i+q][j]-dx[i][j+q]
                        -a[i][j]*j
                        -a[i+q-1][j]*j
                        -a[i][j+q-1]*(j+q-1)
                        -a[i+q-1][j+q-1]*(j+q-1);
                    int64 y = dy[i+q][j+q]+dy[i][j]-dy[i+q][j]-dy[i][j+q]
                        -a[i][j]*i
                        -a[i+q-1][j]*(i+q-1)
                        -a[i][j+q-1]*i
                        -a[i+q-1][j+q-1]*(i+q-1);
                    int64 xshouldbe,yshouldbe;
                    if (q&1){
                        xshouldbe = (j+(q/2))*2;
                        yshouldbe = (i+(q/2))*2;
                    } else {
                        xshouldbe = (j+(q/2))*2-1;
                        yshouldbe = (i+(q/2))*2-1;
                    }
//                    Eo(x);Eo(y); Eo(xshouldbe);Eo(yshouldbe); Eo(real(x)/real(mass)); Eo(real(y)/real(mass));
                    if (2*x!=xshouldbe*mass || 2*y != yshouldbe*mass){
                        continue;
                    }
                    done = true;
                    break;
                }
                if(done)break;
            }
            if (done)break;
        }
        if (!done){
            puts("IMPOSSIBLE");
            continue;
        }
        printf("%d\n",q);
    }
	return 0;
}

