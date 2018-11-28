#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<list>
#include<queue>
#include<set>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

int n,t,a,b;

int pot[12];
set<int> pom;

void wylicz(){
    pot[0]=1;
    FOR(i,1,10){
        pot[i]=pot[i-1]*10;
    }
}

int number(int s, int k){ //obroty s mniejse niz koniec
    pom.clear();
    int start=s;
    int tmp=s;
    int dig=0;
    int wynik=0;
    while (tmp>0) {
        dig++;
        tmp/=10;
    }
    REP(i,dig-1){
        tmp=s%10;
        s/=10;
        s=s+pot[dig-1]*tmp;
        if (s < k + 1 && s > start ) {
            if (pom.find(s)==pom.end()){
                wynik++;
                pom.insert(s);
            }
        }
    }
    return wynik;
}

int main(){
    wylicz();
    int odp;
    scanf("%d",&t);
    REP(i,t){
        scanf("%d%d",&a,&b);
        odp=0;
        FOR(j,a,b-1){
            odp+=number(j,b);
        }
        printf("Case #%d: %d\n",i+1,odp);
    }
}

