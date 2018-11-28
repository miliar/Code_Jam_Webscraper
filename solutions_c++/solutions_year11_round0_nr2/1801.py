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
map<string, string> M;
map< string, map<string,bool> > C;

int a, b, c;
char s[ 555 ];

void get(){            
     scanf("%d", &a);
     M.clear();
     C.clear();
     while(a --){
         scanf("%s", s);                 
         char c = s[ 2 ];
         s[ 2 ] = 0;
         M[ s ] = c;
         swap( s[0], s[1]);
         M[ s ] = c;
     } 
     scanf("%d", &b);
     while(b --){
           scanf("%s", s);   
           string aa, bb;
           aa = "";
           bb = "";
           aa += s[0];
           bb += s[1]; 
           //cout << "aa = " << aa <<" bb = " << bb << endl;
           C[ aa ][ bb ] = true;
           C[ bb ][ aa ] = true;           
     } 
     scanf("%d", &c);
     scanf("%s", s);      
}
int cas = 0;
string ans;

void out(string s){
     //[E, A]
     int i;
     printf("[");
     for(i = 0; i < s.length(); ++ i){
           putchar( s[i] );
           if(i != s.length() - 1)
                printf(", ");
                else puts("]");      
     }
     if(s.length() == 0) puts("]");     
}

bool gao( string &s){
     //cout <<"s = " << s << endl;
     if(s.length() >= 2){
           string aa,bb;   
           aa = s[ s.length() - 2];   
           string slas;
           slas = aa + s[ s.length() - 1] ;
           int i, j;
           if(M.find(slas) != M.end()) {
                 s = s.substr( 0, s.length() - 2);
                 s += M[ slas];
                 return true;                          
           } 
           for(i = 0; i < s.length(); ++ i){
                 aa = "";
                 aa += s[i];
                 for(j = s.length() - 1; j > i; -- j) {
                       bb = "";
                       bb += s[ j ];
                       if(C[ aa ].find( bb ) != C[ aa ].end() ){
                             s = "";
                             return true;      
                       }      
                 }
           }
     }
     return false;     
}

void work(){
     ++ cas;
    ans = s;
    string tmp = "" ;
    int i;
    for(i = 0; i < ans.length(); ++ i) {
       tmp += s[ i ];
       while( gao( tmp ) );
      // cout <<"i = " << i <<" tmp = " << tmp << endl;
    }
    printf("Case #%d: ", cas);
    out ( ans = tmp );
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
