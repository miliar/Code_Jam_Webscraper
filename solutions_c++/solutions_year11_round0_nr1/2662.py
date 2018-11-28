#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

bool visa[101];
bool visb[101];

bool analiza( int ct , vector<int> &e , int w){
    int r = e[ct];
    if( w == 0 ) if( visa[ r ] ) return 1;
    if( w == 1 ) if( visb[ r ] ) return 1;
    return 0;
}

void doit(int test){
    int n;
    scanf("%d",&n);
    vector<int> v, o, b , visi;
    memset( visa , 0 , sizeof(visa) );
    memset( visb , 0 , sizeof(visb) );
    int res = 0;
    for(int i = 0 ; i < n ; i++){
        char p;
        int a;
        cin >> p >> a;
        v.push_back(a);
        if(p == 'O'){
            visi.push_back(0);
            o.push_back(a);
        }
        else{
            visi.push_back(1);
            b.push_back(a);
        }
    }
    visi.push_back(0);
    visi.push_back(0);
    o.push_back(0);
    b.push_back(0);
    int cont = 0;
    int busca = v[cont] , x = 1 , y = 1  , ct = 0 , ct1 = 0;
    while(1){
        if( cont==v.size()) break;
        if( busca == o[ct] && visi[cont] == 0 ){
            if( x == o[ct] ){
                visa[ o[ct] ] = 1;
                ct++;
                cont++;
                busca = v[cont];
                /*while( 1 ){
                    if(analiza( ct , o , 0  ) ){ ct++; }
                    else break;
                }*/
            }
            else{
                if( x < o[ct] ) x++;
                if( x > o[ct] ) x--;
            }
            /*while(1){
                if(analiza( ct1 , b , 1 ) ){  ct1++;  }
                else break;
            }*/
            if( y < b[ct1] ) y++;
            if( y > b[ct1] ) y--;
        }
        else{
            if( y == b[ct1] ){
                visb[ b[ct1] ] = 1;
                ct1++;
                cont++;
                busca = v[cont];
                /*while( 1 ){
                    if(analiza( ct1 , b , 1 ) ){  ct1++; }
                    else break;
                }*/
            }
            else{
                if( y < b[ct1] ) y++;
                if( y > b[ct1] ) y--;
            }
            /*while(1){
                if(analiza( ct , o , 0 ) ){  ct++; }
                else break;
            }*/
            if( x < o[ct] ) x++;
            if( x > o[ct] ) x--;
        }
        res++;
        /*for(int i = 0 ; i < v.size() ; i++){
            if( visa[v[i]] == 0 && visb[v[i]] == 0 ) goto x;
        }
        break;
        x:;*/
    }
    printf("Case #%d: %d\n",test,res);
}

int main(){
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++) doit(i);
}
