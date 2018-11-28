#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
#include<istream>
#include<string>
#include<sstream>
using namespace std;
vector< pair< string, int > >  order;
vector<int> A, B;

string op;
int pos;
int pA, pB;
int n;

void get(){
     scanf("%d", &n);
     order.clear();
     A.clear();
     B.clear();
     int i;
     for(i = 0; i < n; ++ i){
           cin >> op >> pos;
           order.push_back( make_pair( op, pos) );   
           if(op == "O") A.push_back( pos);
           else B.push_back( pos );   
     }               
}
int cas = 0;

void work(){
    pA = pB = 1;
    int ans = 0;
    int i = 0;
    int fA, fB;
    int gA = 0, gB = 0;
    int a, b;
    fA = fB = 0;
    a = b = 0;
    if( A.size() ) {
        if(A[0] > 1) gA = 1;
        if(A[0] < 1) gA = - 1;    
    }
    if( B.size() ) {
        if(B[0] > 1) gB = 1;
        if(B[0] < 1) gB = - 1;    
    }
    ++ cas;
    while( i < order.size() ){
        ++ ans;
        pA += gA;
        pB += gB;
        if(a < A.size() && pA == A[a]) {
             if( gA)
                 gA = 0;
             else 
                  fA = 1;
        }
        if(b < B.size() && pB == B[b]) {
             if( gB)
                 gB = 0;
             else 
                  fB = 1;
        }
        if(order[ i ].first == "O"){
               if(pA == order[ i ].second) {
                     if(! fA) fA = 1, gA = 0;
                     else {
                         ++ a;
                         if(a < A.size() ) {
                              gA = 0;
                              if(A[a] > pA) gA = 1;
                              if(A[a] < pA) gA = - 1;   
                         }
                         ++ i;
                         fA = 0;      
                     }      
               }             
        }else {
                //cout <<"pb = " << pB <<" ans = " << ans <<" fB = " << fB << endl;
                if(pB == order[ i ].second) {
                     if(! fB) fB = 1, gB = 0;
                     else {
                         ++ b;
                         if(b < B.size() ) {
                              gB = 0;
                              if(B[b] > pB) gB = 1;
                              if(B[b] < pB) gB = - 1;     
                         }
                         ++ i;
                         fB = 0;      
                     }      
               }    
        }
    }
    printf("Case #%d: %d\n", cas, ans);
}
int main(){
    //freopen("D:\\in.txt","r",stdin);
   // freopen("D:\\out.txt","w",stdout);
    int T;
    cin >> T;
    while(T --){
     get();
     work();
    }
    //while(  1) ;
    return 0;
}
