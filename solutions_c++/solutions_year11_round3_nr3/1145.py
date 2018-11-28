#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <inttypes.h>
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef unsigned long long int ll;  

/*
int gcd(int a, int b){
    for (;;){
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
        }
    }

int lcm(int a, int b){
    int temp = gcd(a, b);
    return temp ? (a / temp * b) : 0;
    }

int main(){
    int arr[] = { 5, 7, 9, 12 };

    int result = std::accumulate(arr, arr + 4, 1, lcm);

    std::cout << result << '\n';
}
*/

void run(int casenr) {
     vector<int> v_f;
     int flag,f,n,l,h,i1; scanf("%d %d %d",&n,&l,&h);
     FORE (i,1,n){ 
          scanf("%d",&f);
          v_f.push_back(f);
          }
     flag=1;
     for (i1=l;i1<=h;i1++){
         flag=0;
         REPSZ (j,v_f){
               if (v_f[j]%i1!=0&&i1%v_f[j]!=0){
                   flag=1;
                   break;
                   }
               }              
         if (flag==0)break; 
         }
     if (i1<=h)
        printf("Case #%d: %d\n",casenr,i1);
        else
            printf("Case #%d: NO\n",casenr,i1);
     }

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}

 
