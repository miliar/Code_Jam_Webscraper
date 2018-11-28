#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<deque>
#include<map>
#include<algorithm>
using namespace std;

const int maxn = 2000+10;
int T,X,S,R,t,N;
int b[ maxn ],e[maxn],w[maxn];

int main( void ) {
    freopen("a.in","r",stdin);
    freopen("out.out","w",stdout);
    int Cas;
    cin>>T;
    for( Cas = 1; Cas <= T; Cas ++ ) {
         cin>>X>>S>>R>>t>>N;
         int x=1;
         b[0]=0,e[0]=0;
         for(int i=1;i<=N;i++) {
                 int bb,ee,ww; 
                 cin>>bb>>ee>>ww;
                 if( bb==e[x-1] ) {
                     b[ x ] = bb, e[x]=ee,w[x]=ww;
                     x++;
                 }
                 else {
                      b[x]=e[x-1],e[x]=bb,w[x]=-1;
                      x++;
                      b[x] = bb,e[x]=ee,w[x]=ww;
                      x++;
                 }
         }
         if( e[ x-1 ] != X ) {
             b[x]=e[x-1],e[x]=X,w[x]=-1;
             x++;
         }
         int used[  maxn ];
         for(int i=0;i<maxn;i++) used[ i ]=0;
         int a,bb,c,pos;
         double ans = 0;
         double mt = t;
         for(int i=1;i<x;i++) {
                 pos = -1;   
                 for(int j=1;j<x;j++) {
                         if( used[ j ] ) continue;
                         if( pos == -1 ) {
                             pos=j;
                             a = b[j]; 
                             bb=e[j]; 
                             c=w[j];
                             if( c==-1 ) c=S;
                             else c+=S;
                         }
                         else {
                              int a2 = b[j], b2=e[j],c2=w[j];
                              if( c2 == -1 ) c2= S;
                              else c2 = w[j]+S;
                              if( c2 < c ) {
                                  pos = j;
                                  a = a2;
                                  bb = b2;
                                  c = c2;
                              }
                         }
                 }
                 //cout<<"                       "<< pos <<" "<< a <<" "<< bb<<" "<< c<<endl;
                 used[ pos ] = 1;
                 if( mt > 1e-12 ) {
                     double xt =1.*( bb - a )/( c-S+R) ;
                     if( xt > mt ) {
                        //cout<<"    "<< xt << mt <<endl;
                         double dd=1.*mt * (c-S+R);
                         double ttt= 1.*(bb-a - dd) / c;
                         
                         //cout<<"       "<< ttt <<endl;
                         
                         
                         ans += ttt + mt;mt = 0;
                     }
                     else {
                          ans += xt ;
                          mt -= xt;
                     }
                 }
                 else {
                      double ttt =1.* ( bb-a )/c;
                      ans += ttt;
                 }
                 //cout<<"ans         "<<ans<<endl;
         }
         printf("Case #%d: %.10lf\n",Cas,ans );
    }
    //system("pause");
    return 0;
}
                         
                             
