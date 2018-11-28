// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 

LL ruchy[110][110];
int h,w,r;

int kam[20][2];

int main() {
int ile;
scanf("%d",&ile);
FOR(iile,1,ile) {

scanf("%d%d%d",&h,&w,&r);
REP(i,r) {
	scanf("%d%d",&kam[i][0],&kam[i][1]);
	kam[i][0]--; kam[i][1]--;
}
REP(i,110) REP(j,110) ruchy[i][j] = 0;
REP(i,r) ruchy[kam[i][0]][kam[i][1]] = -1;


ruchy[0][0] = 1;
REP(i,h) REP(j,w) if (ruchy[i][j]!=-1){
	if ((i-1>=0) && (j-2>=0)) if (ruchy[i-1][j-2]!=-1) ruchy[i][j]+=ruchy[i-1][j-2];
	if ((i-2>=0) && (j-1>=0)) if (ruchy[i-2][j-1]!=-1) ruchy[i][j]+=ruchy[i-2][j-1];
	ruchy[i][j]%=10007;
}

if (ruchy[h-1][w-1] == -1) ruchy[h-1][w-1] = 0;

printf("Case #%d: %d\n",iile, ruchy[h-1][w-1]);
}
return 0;
}

