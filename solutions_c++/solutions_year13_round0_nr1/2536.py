#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
 
using namespace std;
 
#define s(n)                                 scanf("%d",&n)
#define sl(n)                                   scanf("%lld",&n)
#define sf(n)                                   scanf("%lf",&n)

#define EPS                                             1e-9
 
#define FOR(i,a,b)                              for(int i=a;i<b;i++)
#define REP(i,n)                                FOR(i,0,n)
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
 
#define mp                                              make_pair
#define pb                                              push_back
 
#define FF                                              first
#define SS                                              second
 
#define tri(a,b,c)                              mp(a,mp(b,c))
#define XX                                              first
#define YY                                              second.first
#define ZZ                                              second.second
 
/*Important ones*/
#define fill(a,v)                               memset(a,v,sizeof a)     //Works properly only for v = 0 or -1
#define all(x)                                  x.begin(),x.end()
 
#define SZ(v)                                   ((int)(v.size()))
#define DREP(a)                                 sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)                  (lower_bound(all(arr),ind)-arr.begin())
 
//typedefs. Use if you feel comfortable
typedef pair<int,int> PII;
typedef pair<long long,long long> PLL;
typedef pair< long long, PLL > TRI;

typedef vector<int> VI;
typedef long long LL;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;
 
typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;

#define MAX 1000010

int grd[4][4], x, y, tp, X, O, tests;

int main(){
	
	char t;
	
	s(tests);
	
	FOR(testcase,0,tests){
		X = O = 0;
		FOR(i,0,4)
			FOR(j,0,4){
				cin>>t;
				switch(t){
					case 'X':	grd[i][j] = 1;
								break;
					case 'O':	grd[i][j] = -1;
								break;
					case 'T':	grd[i][j] = 0;
								x = i;	y = j;
								break;
					case '.':	grd[i][j] = 0;
								break;
				}
			}
		grd[x][y] = 1;
		FOR(i,0,4)
			if(grd[i][0]+grd[i][1]+grd[i][2]+grd[i][3] == 4)
				++X;
		FOR(i,0,4)
			if(grd[0][i]+grd[1][i]+grd[2][i]+grd[3][i] == 4)
				++X;
		tp = 0;
		FOR(i,0,4)
			FOR(j,0,4)
				if(i == j)
					tp += grd[i][j];
		if(tp == 4)
			++X;
		tp = 0;
		FOR(i,0,4)
			FOR(j,0,4)
				if(i+j == 3)
					tp += grd[i][j];
		if(tp == 4)
			++X;
		
		grd[x][y] = -1;
		FOR(i,0,4)
			if(grd[i][0]+grd[i][1]+grd[i][2]+grd[i][3] == -4)
				++O;
		FOR(i,0,4)
			if(grd[0][i]+grd[1][i]+grd[2][i]+grd[3][i] == -4)
				++O;
		tp = 0;
		FOR(i,0,4)
			FOR(j,0,4)
				if(i == j)
					tp += grd[i][j];
		if(tp == -4)
			++O;
		tp = 0;
		FOR(i,0,4)
			FOR(j,0,4)
				if(i+j == 3)
					tp += grd[i][j];
		if(tp == -4)
			++O;
		tp = 1;
		FOR(i,0,4)
			FOR(j,0,4)
				tp *= grd[i][j];
		if(X)
			X = 1;
		if(O)
			O = 1;
		cout<<"Case #"<<testcase+1<<": ";
		if(X==O && tp)
			cout<<"Draw\n";
		else if(X)
			cout<<"X won\n";
		else if(O)
			cout<<"O won\n";
		else
			cout<<"Game has not completed\n";
	}
	
	return 0;
	
}
