#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#define MP make_pair

using namespace std;
typedef pair<int,int> Pair;
typedef vector<int> Vector;
typedef long long LL;
LL gcd(LL a,LL b){
	if(b == 0) return a;
	return gcd(b,a%b);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	LL n;
	int  pd, pg;
	bool flag;
	scanf("%d",&T);
	for(int it = 1;it <= T; ++it){
		scanf("%lld%d%d",&n,&pd,&pg);
		printf("Case #%d: ",it);
		if(pg == 100){
			if(pd == 100) flag = true;
			else flag = false;
		}else if(pg == 0){
			if(pd == 0) flag = true;
			else flag = false;
		}else{
			LL t = gcd(pd,100L);
			LL tt = (100L)/t;
			if(tt > n) flag = false; 
			else flag = true; 
		}
		if(flag) puts("Possible");
		else puts("Broken");
	}
	
}
