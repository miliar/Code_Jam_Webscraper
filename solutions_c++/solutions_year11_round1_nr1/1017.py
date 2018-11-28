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
typedef long long LL;
int cas = 0;
int gcd(int a, int b){return b ? gcd(b, a % b) :a;}

int main(){
    freopen("D:\\in.txt","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    int T;
    cin >> T;
    int i;
    //for(i = 1; i <= 9; ++ i) cout << 100 * i % 80 <<' '<< 100 * i % 56 << endl;
    while(T --){
       ++ cas;
       LL N;
       int PD, PG;
       cin >> N >> PD >> PG;
       printf("Case #%d: ", cas);
       //if( cas == 32) cout << N <<' '<< PD <<' '<< PG << endl;
       /*int D, G;
       int flg = 0;
       for(D = 1; D <= N && !flg; ++ D){
             for(G = D; G <= 2000000 && !flg; ++ G){
                   if(D * PD % 100) continue;
                   if(G * PG % 100) continue;
                   int x, y;
                   x = D * PD / 100;
                   y = G * PG / 100;
                   if(x <= y && y <= G - D + x) flg =  1, cout << D <<' '<< G << endl;    
             }      
       } 
       printf("%s\n", flg ? "Possible" : "Broken");*/
       if(PG == 0) {
             if(PD)puts("Broken");
             else  puts("Possible");
             continue;      
       }
       if(PD == 0){
             if(PG == 100)puts("Broken");
             else  puts("Possible");
             continue;       
       }
       if(PG == 100) {
             if(PD != 100)puts("Broken");
             else  puts("Possible");
             continue;
       }
       int lcm = PD;
       int mi_d = 100 / gcd( 100, lcm);
       if( mi_d <= N) {
           puts("Possible");
       }
       else  puts("Broken");
    }
    //while( 1 ) ;
	return 0;
}

