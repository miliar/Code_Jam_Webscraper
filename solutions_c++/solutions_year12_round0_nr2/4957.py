#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <algorithm>
#include <climits>
#include <cmath>
#include <ctime>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORQ(x,y,z) for(int (x)=(y);(x)<=(z);(x)++)
#define FORD(x,y,z) for(int (x)=(y);(x)>(z);(x)--)
#define FORDQ(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define REP(x,z) for(int (x)=1;(x)<=(z);(x)++)
#define UNIQUE(x) sort(ALL((x))); (x).resize(unique(ALL((x)))-(x).begin());
#define PB push_back
#define MP make_pair
#define ALL(x) (x).begin(),(x).end()
#define F first
#define S second
#define PII pair<int,int>
#define PACKS(Z,IdzieSobieBladWielbladMaWrotkiNaKopytachJESTNIENORMALNY) int Z;scanf("%d",&Z);FORQ(IdzieSobieBladWielbladMaWrotkiNaKoptyachJESTNIENORMALNY,1,Z)
//#define NODEBUG
#ifdef NODEBUG
        #define debug(...) /*fprintf(stderr,__VA_ARGS__);*/
#else
        #define debug(...) fprintf(stderr,__VA_ARGS__);
#endif
using namespace std;
int n,s,p;
int tab[200];
int main(){
    int cases;
    scanf("%d",&cases);
    FORQ(Case,1,cases){
        scanf("%d%d%d",&n,&s,&p);
        int out=0;
        FOR(i,0,n)scanf("%d",tab+i);
        FOR(i,0,n){
            int x=int(ceil((double(tab[i])/3.0)));
            if(x>=p)out++;
            if(x==p-1&&s>0&&tab[i]>=2&&tab[i]%3!=1){s--;out++;}
        }
        printf("Case #%d: %d\n",Case,out);
    }
    return 0;
}
