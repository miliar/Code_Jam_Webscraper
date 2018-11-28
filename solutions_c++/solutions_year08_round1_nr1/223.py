#include <stdio.h>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>

#define S(t,z) scanf("%"#t,&z)
#define P(t,z) printf("%"#t,z)
#define PLN(t,z) printf("%"#t"\n",z)
#define PS(t,z) printf("%"#t" ",z)

#define Z(t,n) memset(t,0,sizeof(t[0])*n)
#define MCP(d,s,n) memcpy(d,s,sizeof(s[0])*n)

#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)

#define LL long long

using namespace std;

int i,j,x,w,v,k,m,n;
int CT;
LL res;
vector <int> v1;
vector <int> v2;
int main(){
   int T;
   S(d,T);
   CT=0;
   while (CT++,T--) {
     S(d,n);
     v1.clear();v2.clear();
     for (int i=0;i<n;i++) {
        S(d,x);
	v1.push_back(x);
     }
     for (int i=0;i<n;i++) {
        S(d,x);
	v2.push_back(x);
     }
     sort(v1.begin(),v1.end());
     sort(v2.rbegin(),v2.rend());
     
     res = 0;
    
     for (int i=0;i<n;i++) {
        res = res + v1[i]*v2[i];
	
     }
    
     cout <<"Case #"<<CT<<": "<<res<<endl;
   }
    return 0;
}

