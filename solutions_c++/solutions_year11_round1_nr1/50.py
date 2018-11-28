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


ll gcd(ll a, ll b){
	if(b==0)return a;
	return gcd(b,a%b);
}
int main(){
	int tc;
	scanf("%d",&tc);
	FOR(tcc,1,tc+1){
		ll N,p1,p2;
		cin>>N>>p1>>p2;
		printf("Case #%d: ",tcc);
		ll q1 =100,q2=100;
		if(p2==0&&p1!=0){
			printf("Broken\n");
		} else if(p2==100&&p1!=100){
			printf("Broken\n");
		} else {
			ll gc = gcd(p1,q1);
			q1/=gc;
			if(q1<=N)printf("Possible\n");
			else printf("Broken\n");
		}
	}
	return 0;
}
