#include<cstdio>
#include<cmath>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<vector>
#include<deque>
#include<algorithm>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long  

const int maxn = 100005;
int i , j , n , m , T , t_case;
double first[maxn] , good[maxn];


int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	
	scanf("%d",&T);
	
	for(t_case = 1; t_case <= T; ++t_case) {
		
		scanf("%d %d",&n,&m);
		
		double ans = 1000 * 1000 * 1000;
		
		for(i = 1; i <= n; ++i)
			scanf("%lf",&good[i]);
		
		first[1] = good[1];
		
		for(i = 2; i <= n; ++i)
			first[i] = first[i - 1] * good[i];
		
		ans = min(ans , first[n] * (m - n + 1) + (1 - first[n]) * (m - n + m + 2));
		ans = min(ans , (double)(m + 2));
		
		for(i = 1; i < n; ++i)
			ans = min(ans , first[i] * (m - n + 1 + 2 * (n - i)) + (1 - first[i]) * (m - n + 1 + 2 * (n - i) + m + 1));
		
		printf("Case #%d: %lf\n",t_case,ans);
	}
		
	
	
return 0;
}