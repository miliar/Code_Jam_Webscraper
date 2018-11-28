#include<stdio.h>
#include<string.h>
#include<cmath>
#include<algorithm>
#include<queue>
#include<iostream>
using namespace std;
typedef long long LL;
typedef double db;
const int maxn = 1005;
#define mp make_pair
const db EPS = 1e-8;
int cas = 0;
db X, S, R, t;
inline int sign( db x){return x < - EPS ? - 1 : x > EPS;}
int N;
db L[ maxn ], r[ maxn ], w[ maxn ];
pair< db, pair<db,db> > P[ maxn ];
pair< db, db> Seg[ maxn ];
int Plen;

void get(){
     scanf("%lf%lf%lf%lf%d", &X, &S, &R, &t, &N);
     int i;
     Plen = 0;
     for(i = 0; i < N; ++ i){
           scanf("%lf%lf%lf", L + i, r + i, w + i); 
           if( L[i] > X) continue;
           if(r[i] > X) r[i] = X;
           P[ Plen ] .first = w[ i ];
           P[ Plen ].second = mp( L[i], r[i]) ;
           Seg[ Plen ] = mp( L[i], r[i]) ;
           ++ Plen;    
     }     
}

void work(){
     ++ cas;
     db ans = 0.0;
     if( Plen == 0) {
         db run_dis = R * t;
         if( run_dis > X + EPS) ans = X / R;
         else {
              ans += t;
              X -= run_dis;
              ans += X / S;     
         } 
     }else {
         int i;
         sort( Seg, Seg + Plen );
         db plt = X, pre = 0.0;
         int oPlen = Plen;
         for(i = 0;i  < oPlen; ++ i){
               db nowl = Seg[ i ].first;
               db nowr = Seg[ i ].second;
               if( fabs(nowl - pre) < EPS ) {
                   pre = nowr;
                   continue;
               }      
               P[ Plen ].first = 0.0;
               P[ Plen ].second = mp( pre, nowl);
               Plen ++;
               pre = nowr;
         }
         if( fabs(pre - X) > EPS) {
               P[ Plen ].first = 0.0;
               P[ Plen ].second = mp( pre, X);
               Plen ++;   
         }
         sort( P, P + Plen);
         for(i = 0; i < Plen; ++ i) plt -= P[ i ].second.second - P[ i ].second.first;
        // for(i = 0; i < Plen; ++ i) cout << P[ i ].second.first << '_' << P[ i ].second.second << endl;
         for(i = 0; i < Plen; ++ i){
               db my_dis = P[ i ].second.second - P[ i ].second.first;
               db my_time = my_dis / ( R + P[ i ].first) ;
               db real_time;
               //cout << "my_time =  " << my_time << endl;
               if( sign(my_time - t ) <= 0) {
                   t -= my_time;
                   ans += my_time;
               }else{
                   ans += t;
                   db rem_dis = my_dis - t * (  R  + P[ i ].first) ;
                   rem_dis /= (  S + P[ i ].first );
                   ans += rem_dis;
                   for( ++ i; i < Plen; ++ i) {
                         my_dis = P[ i ].second.second - P[ i ].second.first;
                         ans +=  my_dis / (  S + P[ i ].first );   
                   }
                   break;
               }     
         }
     }
     printf("Case #%d: %.6f\n", cas, ans);    
}

int main(){
    freopen("D:\\A-small-attempt0.in","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    int T;
    cin >> T;
    while(T --){
         get();
         work();           
    }
	return 0;
}
