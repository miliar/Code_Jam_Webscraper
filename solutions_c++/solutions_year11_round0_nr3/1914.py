#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
#include<istream>
#include<string>
#include<sstream>
#include<map>
using namespace std;
int a[ 1005 ];
int n;
int s;

void get(){   
     s = 0;
     cin >> n;
     int i;
     for(i = 0; i < n; ++ i) cin >> a[ i ], s ^= a[ i ];
     sort( a, a + n );
}
int cas = 0;

void work(){
    ++ cas;
    printf("Case #%d: ", cas);
    if(s) puts("NO");
    else {
         s = 0;
         int i;
         for(i = 1; i < n; ++ i) s += a[ i ];
         cout << s << endl;     
    }
}
int main(){
    //freopen("D:\\in.txt","r",stdin);
    //freopen("D:\\out.txt","w",stdout);
    int T;
    cin >> T;
    while(T --){
     get();
     work();
    }
    //while(  1) ;
    return 0;
}
