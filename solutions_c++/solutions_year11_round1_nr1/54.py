#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#define CLEAR(a) memset(a,0,sizeof(a))
#define ABS(a) ((a)>0?(a):-(a))
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
using namespace std;
typedef pair<int,int> pi;
typedef long long int lld;
typedef vector<int> vi;
typedef string ss;
typedef double lf;
typedef long double llf;

lld N;
int t, Pd, Pg, d, gamesD, testnr;

int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%lld %d %d",&N,&Pd,&Pg);
		d = __gcd(Pd, 100);
		gamesD = 100 / d;
		if(gamesD > N || (Pd != 100 && Pg == 100) || (Pd > 0 && Pg == 0)){
			printf("Case #%d: Broken\n", ++testnr);
		//	continue;
		}
		else{
			printf("Case #%d: Possible\n", ++testnr);
		}
	}	
}
