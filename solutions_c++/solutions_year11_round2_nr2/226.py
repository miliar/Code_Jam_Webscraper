#include<iostream>
#include<algorithm>
#include<ctime>
#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>
#include<cmath>
#include<string>
#include<queue>
#include<sstream>
using namespace std;

const int maxn = 205;

pair<int,int> P[ maxn ];
typedef double db;
int n, m;
const db EPS = 1e-8;
const db inf = 1e20;
bool ok( db t){
     int i, j;
     db pre, now;
     pre = - inf;
     for(i = 0; i < n; ++ i){
           for(j = 0; j < P[i].second; ++ j){
                 now=max(pre+m,P[i].first- t);
                 pre=now;   
                 if(now > P[i].first + t + EPS) return false;   
           }
     }
     return true;
}
db gao(){
    db l, r, mid;
    l = 0.0;
    r = 1e13;
    while( fabs(l - r) > EPS) {
           mid = (l + r) * 0.5;
           if( ok(mid) ) r = mid;
           else l = mid;       
    }         
    return mid;
}

void get(){
     scanf("%d%d", &n, &m);
     int i;
     for(i = 0; i < n; ++ i){
           scanf("%d%d", &P[i].first, &P[i].second);      
     }     
     sort( P, P + n);
}
int cas = 0;

void work(){
     ++ cas;
     db tmp;
     printf("Case #%d: %.10f\n", cas, tmp = gao()); 
     cerr<< cas <<':'<< tmp << endl;
}

int main(){
    freopen("D:\\b.in","r",stdin);
    freopen("D:\\b.out","w",stdout);
    int T;
    cin >> T;
    while(T --){
         get();
         work();           
    }
    //while( 1 ) ;
	return 0;
}
