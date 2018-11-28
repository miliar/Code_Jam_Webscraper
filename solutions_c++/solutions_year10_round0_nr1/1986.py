#include<cstdio>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a;i < b;++i)

typedef long long LL;

int main(){
	int test = GI;
	FOR(nt,1,test + 1){
		LL n = GI,k = GI;
		LL val = (1LL << n);

		k %= val;
		if(k==val-1)
			printf("Case #%d: ON\n",nt);
		else
			printf("Case #%d: OFF\n",nt);
	}

	return 0;
}
