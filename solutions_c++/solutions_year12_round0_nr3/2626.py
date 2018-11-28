#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
#include <list>
#include <vector>
#include <cassert>

#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FOREACH(i,x) for (__typeof((x).begin())i=(x).begin(); i!=(x).end(); ++i)
#define S(t,i) scanf("%"#t, &i)
#define SI(i) scanf("%d", &i)
#define LL long long

using namespace std;

inline int log10(int v){
    return (v >= 1000000) ? 7 : (v >= 100000) ? 6 : (v >= 10000) ? 5 : 
    (v >= 1000) ? 4 : (v >= 100) ? 3 : (v >= 10) ? 2 : 1;
}

int digitable[]={0,1,10,100,1000,10000,100000,1000000,10000000};
int counted[2000000+10];
int countedtest[2000000+10];

int main() {
    
    int t;
    SI(t);
    REP(i,t){
        int count=0;
        int a,b;
        SI(a); SI(b);
        
        int da=log10(a);
//        int db=log10(b);
        int digits=da;
        int numm=a+1;
        
        for (;numm<=b;numm++){
            if (numm==digitable[digits+1]) {
                digits++;
            }
            int numn=numm;
            for (int di=0;di<digits-1;di++){
                int lastdigit=numn%10;
                numn=numn/10+lastdigit*digitable[digits];
                if (numn<numm && numn>=a) {
                    if (counted[numn]!=numm || countedtest[numn]!=i+1) {
                        countedtest[numn]=i+1;
                        counted[numn]=numm;
                        count++;
                    }
                }
            }
        }
        
        printf("Case #%d: %d\n",i+1,count);
    }
    
	return 0;
}
