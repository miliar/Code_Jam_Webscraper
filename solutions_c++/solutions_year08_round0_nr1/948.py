// By mirosuaf
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 



int main() {
int ile;
scanf("%d",&ile);
REP(iile,ile) {
int n,m,tab[2000];
scanf("%d",&n);
map<string,int> mapa;
char tmp[200];
string st;
gets(tmp);

REP(i,n) {
    gets(tmp);
    st=tmp;
    mapa[st]=i;
    }
scanf("%d",&m);
gets(tmp);

REP(i,m) {
    gets(tmp); st=tmp;
    tab[i]=mapa[st];
    }
    

//REP(i,m) cout << tab[i] << " "; cout << endl;
int wh,start,changes=0,maxio;

start=0;
tab[m]=-1;
while (start!=m) {
maxio=-1;
    REP(kolor,n) {
	wh=start;
	while (tab[wh]!=kolor && tab[wh]!=-1) wh++;
	
	if (wh>maxio) maxio=wh;
	}

if (maxio!=m) changes++;
    start=maxio;
}
printf("Case #%d: %d\n",iile+1,changes);
}


return 0;
}
