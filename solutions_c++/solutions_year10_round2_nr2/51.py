#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;

#define fore(i,n) for(int i = 0; i < (n); i++)
#define fort(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

#define err(...) fprintf(stderr, __VA_ARGS__)

#define maxn 55

int x[maxn], v[maxn];

void test()
{
	int n,k,b,t,res=0;
	scanf("%d%d%d%d", &n, &k, &b, &t);
	fore(i,n) scanf("%d", &x[i]);
	fore(i,n) scanf("%d", &v[i]);
	for(int i = n-1; i >= 0; i--)
	{
		if(k == 0) break;
		if(b-x[i] <= t * v[i]) k--;
		else res += k;
	}
	if(k > 0) printf("IMPOSSIBLE\n");
	else printf("%d\n", res);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		test();
	}
}
