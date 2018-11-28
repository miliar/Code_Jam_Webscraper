#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define LL long long
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1
#define MID ((l+r)>>1)
#define BUG1 puts("BUG11\n")
#define LgLg long long
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a>b?b:a)
#define two(x)            ((LL)1<<(x))
#define include(a,b)        (((a)&(b))==(b))
#define FOR(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define FF(i,a) for(int i=0;i<a;i++)
#define FD(i,a,b) for(int i=a;i>=b;i--)
#define STOP  int stop;scanf("%d", &stop)
#define PD(x) printf("%d",(x))
#define PP printf(" ")
#define SD(x) scanf("%d", &(x))
#define SF(x) scanf("%lf", &(x))
#define SET(x,y) memset(x,y,sizeof(x))
#define LN printf("\n");
#define SWAP(a,b) a=a xor b;b= a xor b;a=a xor b;
#define EPS 1e-8
#define PI acos(-1.0)
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
#define read            freopen("in.in","r",stdin)
#define write           freopen("out.out","w",stdout)
const int maxn= 10505;

//int a[maxn];
//int f[maxn][505];
//int g[maxn][505];
//
//int main(){
//    int n, m;
//    SET(f,0);
//    SET(a,0);
//    SD(n); SD(m);
//    FOR(i,1,n){
//        SD(a[i]);
//    }
//    FOR(i,0,n-1){
//        f[i+1][0]= MAX(f[i+1][0],f[i][0]);
//        FOR(j,0,lim){
//            f[i+1][j+1]= MAX(f[i][j]+a[i], f[i+1][j+1]);
//            f[i+j][0]= MAX(f[i][j],f[i+j][0]);
//        }
//
//    }
//    PD(f[n][0]);LN;
//
//    STOP;
//
//    FOR(i,1,n){
//        int t;
//        SD(t);
//        FOR(j,1,m)
//            f[i][j]= MAX(f[i-1][j-1],g[i-1][0])+t;
//        FOR(j,0,m)
//            g[i][j]=MAX(g[i-1][0],MAX(g[i-1][j+1],f[i-1][j+1]) );
//    }
//    PD(g[n][0]);LN;
//
//}
bool find(int x, int y){
    int len=1;
    int cnt= 0;
    if (y<10){
        len= 1;
    } else if (y<100){
        len= 10;
        cnt= 1;
    } else if (y<1000){
        len= 100;
        cnt= 2;
    } else if (y<10000){
        len= 1000;
        cnt= 3;
    }
    int sb= y;
    do{
        int mod= sb%10;
        int div= sb/10;
        sb= mod*len+div;
        cnt--;
        if (sb==x)  return true;
    }while(cnt>0);
    return false;

}


int main(){
    read;
    write;
    int n;
    SD(n);
    FOR(nca,1,n){
        int x, y;
        SD(x); SD(y);
        int cnt= 0;
        FOR(i,x,y){
            FOR(j,i+1,y){
                if (find(i,j)){
                    cnt++;
                }
            }
        }
        printf("Case #%d: ",nca);PD(cnt); LN;
    }

}



