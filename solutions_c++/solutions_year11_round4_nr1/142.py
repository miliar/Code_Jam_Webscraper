#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)


int main(){
	int tc;
	scanf("%d",&tc);
	FOR(tcc,1,tc+1){
		int L,v0,v1,t1,N;
		scanf("%d%d%d%d%d",&L,&v0,&v1,&t1,&N);
		map<int,int> mm = map<int,int>();
		int last = 0;
		FOR(i,0,N){
			int a,b,v;
			scanf("%d%d%d",&a,&b,&v);
			if(a>last)mm[0]+=a-last;
			mm[v]+=b-a;
			last = b;
		}
		mm[0]+=L-last;
		double rest = t1;
		double res = 0.0;
		FORIT(it,mm){
			double sp = it->first;
			double len = it->second;
			double p1 = len/(sp+v1);
			p1 = min(p1,rest);
			rest -= p1;
			res+=p1;
			len -=p1*(sp+v1);
			res+=len/(sp+v0);
		}
		printf("Case #%d: %.10lf\n",tcc,res);
	}
	return 0;
}
