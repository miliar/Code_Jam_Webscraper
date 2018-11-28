#include<stdio.h>
#include<string.h>
#include<cmath>
#include<algorithm>
#include<queue>
#include<iostream>
using namespace std;
typedef long long LL;
const int maxn = 1000005;
bool ss[ maxn ] = { 1,1 };
int p[ maxn >> 1], plen = 0;

void pre(){
     int i,j;
     for(i = 2; i * i < maxn; ++ i)
           if(! ss[i])
           for(j = i; j * i < maxn; ++ j) ss[i * j] = 1;
     for(i = 2; i < maxn; ++ i) if(! ss[i])
     p[plen++] = i;
     //cout << plen << endl;   
}
int cas = 0;
LL n;
int get_ki(LL pp, LL n){
    int ans = 0;
    LL v = pp;
    pp = 1;
    for(; pp <= n; ++ ans, pp *= v);
    //cout << v <<'_' << n << endl;
    return max( 0, ans - 1 );
}

void get(){
     cin >> n;
}

void work(){
     ++ cas;
     if(n == 1) {
          printf("Case #%d: 0\n", cas);
          return ;     
     }
     LL tot = 1;
     int i;
     for(i = 0; i < plen && p[i] <= n; ++ i) tot += (LL)get_ki( (LL)p[i], n ) - 1;
     printf("Case #%d: ", cas);
     cout << tot << endl;
}

int main(){
    freopen("D:\\C-large.in","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    int T;
    pre();
    cin >> T;
    while(T --){
         get();
         work();           
    }
	return 0;
}
