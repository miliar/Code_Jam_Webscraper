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

int perm[12];
ll gcd(ll a, ll b){
	if(b==0)return a;
	return gcd(b,a%b);
}
int prime[1000000];
int main(){
	memset(prime,-1,sizeof(prime));
	FOR(p,2,1000000){
		if(prime[p]==-1){
			prime[p]=p;
			for(ll i = p*(ll)p; i<1000000; i+=p)prime[(int)i]=p;
		}
	}
	int tc;
	scanf("%d",&tc);
	FOR(tcc,1,tc+1){
		ll N;
		cin >> N;
		int res = 1;
		if(N==1)res = 0;
		FOR(i,2,min(1000000LL,N+1)){
			if(prime[i]==i){
				ll cur = i;
				while(cur*i<=N){
					res++;
					cur*=i;
				}
			}
		}
		printf("Case #%d: %d\n",tcc,res);
	}
/*	while(true){
		int N;
		cin >> N;
		if(N==0)break;
		FOR(i,0,N)perm[i]=i+1;
		int lv = oo, hv = 0;
		do{
			ll cur = perm[0];
			int res = 1;
			FOR(i,1,N){
				ll gc = gcd(cur,perm[i]);
				if(gc==perm[i])continue;
				perm[i]/=gc;
				cur*=perm[i];
				perm[i]*=gc;
				res++;
			}
			lv = min(lv,res);
			hv = max(hv,res);
		}while(next_permutation(perm,perm+N));
		cout << lv << " " << hv << endl;
	}*/
	return 0;
}
