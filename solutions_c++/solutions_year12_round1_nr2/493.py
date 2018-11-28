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

const int maxn = 1005;
int i , j , n , m , T , t_case , ans , current, a , b;
vector <pair<int , int > > v;
bool mark[maxn];

inline bool cmp(pair<int , int> A , pair<int , int> B) {
	if(A.first == B.first)
		return A.second > B.second;
	return A.first < B.first;
}

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	
	scanf("%d",&T);
	
	for(t_case = 1; t_case <= T; ++t_case) {
		
		scanf("%d",&n);
		v.clear();
		
		for(i = 1; i <= n; ++i) {
			scanf("%d %d",&a,&b);
			v.pb(mp(b,a));
			//v2.pb(mp(a,i));
		}
		
		bool ok = false;
		memset(mark , 0 , sizeof(mark));
		current = 0;
		ans = 0;
		printf("Case #%d: ",t_case);
		
		sort(v.begin() , v.end() , cmp);
		//sort(v2.begin() , v2.end());
		
		for(i = 0; i < n; ) {
			
			int needed = v[i].first - current;
			
			for(j = n - 1; j >= i && needed;--j)
				if(v[j].second <= current && !mark[j]) {
					ans++;
					needed--;
					mark[j] = true;
					current++;
					j = n;
				}
				
			if(needed) {
				printf("Too Bad\n");
				ok = true;
				break;
			}
			
			//current = max(current , v[i].first);
			current = v[i].first;
			
			for(;v[i].first <= current && i < n;) {
				if(mark[i])
					current++;
				else
					current += 2;
				mark[i] = true;
				++i;
				ans++;
			}
		}
		
		if(!ok)
			printf("%d\n",ans);
	}
	
		
	
	
return 0;
}