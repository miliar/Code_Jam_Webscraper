
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

double dp[2000];
int perm[2000];
int main(){
	dp[0]=0;
	dp[1]=0;
	FOR(n,2,1100){
		double nn = n;
		dp[n]=0;
		FOR(i,1,n){
			dp[n]+=dp[i]+max(dp[n-i],1.0);
		}
		dp[n]=(dp[n]+1.0)/(n-1);
	}
	int T,N;
	scanf("%d",&T);
	FOR(tc,1,T+1){
		scanf("%d",&N);
		double res = 0;
		FOR(i,0,N)scanf("%d",perm+i);
		FOR(i,0,N)--perm[i];
		FOR(i,0,N)if(perm[i]!=-1){
			int cur = i;
			int si = 0;
			while(perm[cur]!=-1){
				si++;
				int ne = perm[cur];
				perm[cur]=-1;
				cur = ne;
			}
			res += dp[si];
		}
		printf("Case #%d: %.6lf\n",tc,res);
	}
	return 0;
}
