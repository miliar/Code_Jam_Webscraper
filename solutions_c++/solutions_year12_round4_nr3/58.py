#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAXN = 2000 + 10;
const double eps = 1e-5;

int n;
int a[MAXN];
int y[MAXN];

bool solve( int l, int r, double k ){
//    printf("solve(%d,%d,%.5lf)\n",l,r,k);
    if ( l + 1 >= r ) return true;

    for( int i = l+1; i <= r-1; i++ )
        if ( a[i] <= i || a[i] > r ) return false;
    
    int last = l;
    for( int i = l+1; i <= r-1; i++ ) if ( a[i] == r ) {
        double uy = y[r] - k*(r-i) - eps;
        uy = floor(uy);
        y[i] = uy;
        k = ( double(y[r] - y[i]) ) / ( r-i );
        if (!solve(last,i,k))return false;
        last = i;
    }
    
    return true;
}

bool solve(){
    int h = 1000000000;
    y[1] = h;
    for( int i = 1; i < n ; ){
        int j = a[i];
        y[j] = h;
        if ( !solve(i,j,0) ) return false;
        i = j;
    }

    return true;
}

void solve(int Case){
    scanf("%d",&n);
    for( int i = 1; i < n ; i++ ) scanf("%d",a+i);
    
    printf("Case #%d:",Case);
    if ( solve() ){
        for( int i = 1; i <= n; i++ ) printf(" %d",y[i]);
        puts("");
    }else{
        puts(" Impossible");
    }
}
int main(){
    int T; scanf("%d",&T);
    for( int Case = 1; Case <= T; Case++ ){
        solve(Case);
    }
}
