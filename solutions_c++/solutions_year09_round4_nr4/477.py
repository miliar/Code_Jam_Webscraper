#pragma comment(linker,"/STACK:64000000")

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <sstream>
#include <cmath>
#include <ctime>

#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);++i)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);--i)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define LL long long
using namespace std;
typedef vector<int>    VI;
typedef vector<string> VS;
typedef pair<int ,int> PAR;

#define ass(s) \
if (!(s)) { \
	int ln = __LINE__;\
	char * s1 = __FILE__, * s2 = __FUNCTION__;\
	fprintf(stderr,"\n(!)ASSERTION FAILED: %s, %s, %d.\n",s1,s2,ln);\
	printf("\n(!)ASSERTION FAILED: %s, %s, %d.\n",s1,s2,ln);\
	cout.flush(), cerr.flush();\
	exit(1);\
}


int T;
int n;
int x[5], y[5], r[5];
void init()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	RE("%d",&T);
}
double len(double x1, double y1, double x2, double y2){
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}
double Try1(int a, int b, int c){
	return max((len(x[a],y[a],x[b],y[b]) + r[a] + r[b]) * 0.5, (double)r[c]);
}
double Try2(int a, int b){
	return max(r[a],r[b]);
}
double f(){	
	if (n==1) return r[1];
	if (n==2) return min(Try2(1,2), Try1(1,2,1));
	if (n==3) return min(min(Try1(1,2,3), Try1(1,3,2)), Try1(2,3,1));
	ass(false);
	return -1;
}
void sol(){
	int t, i, j;
	FOR(t,1,T){
		RE("%d",&n);
		FOR(i,1,n) RE("%d %d %d",&x[i],&y[i],&r[i]);
		WR("Case #%d: %.8lf",t,f());
		if (t<T) WR("\n");
	}
}
int main()
{
	init();
	sol();
	return 0;
}