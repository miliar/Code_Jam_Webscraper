#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  

int n;
int keo[1010];
int D[1010];

int duyet(int i){
    D[i] = 0;    
    if (i == n - 1) {
       int sum1 = 0, sum2 = 0;   
       REP(j,n) sum1 += D[j];
       if(sum1 == 0) return -1;
       
       sum1 = 0;
       REP(j,n) 
           if (D[j] == 0) sum1 ^= keo[j]; else sum2 ^= keo[j];
       if (sum1 != sum2)    return -1;
       sum1 = 0; sum2 = 0;
       REP(j,n) 
           if (D[j] == 0) sum1 += keo[j]; else sum2 += keo[j];       
       if (sum1 > sum2) return sum1; else return sum2;           
    }
    
    int d0 = duyet(i+1);
    D[i] = 1;
    int d1 = duyet(i+1);    
    if (d0 > d1) return d0; else return d1;
}

int main()
{
    int ntest, test = 0;
    cin >> ntest;
    while(test < ntest){
        test++;
        

        
        cin >> n;
        REP(i,n) {
           cin >> keo[i];
           D[i] = 0;
        }
        
        int ans = duyet(0) ;
        if (ans > 0)
        cout << "Case #" << test << ": " << ans << endl;
        else cout << "Case #" << test << ": NO" << endl;
    }
    return 0;
}
