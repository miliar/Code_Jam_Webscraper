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

char przyp[50]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
    int cases;
    cin >> cases;
    while(getchar()!='\n'){}
    FORQ(Case,1,cases){
        string in;
        getline(cin,in);
        string out;
        FOR(i,0,in.size())out.push_back(in[i]!=' '?przyp[in[i]-'a']:' ');
        cout<< "Case #"<<Case<<": "<<out<<endl;
    }
    
}

