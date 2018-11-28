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

int i , j , k , cnt , a, b , t , n;
vector <pair <int , int > > v;

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&t);
	for(k = 1  ; k <= t ;  ++k) {
		scanf("%d",&n);
		cnt = 0;
		for( ; n -- ; ) {
			scanf("%d %d",&a,&b);
			v.pb(mp(a,b));
		}
		
		for( i = 0 ; i < v.size() ; ++i ) 
			for( j = i + 1 ; j < v.size() ; ++j )
				if ( ((v[i].f - v[j].f)> 0) != ((v[i].s - v[j].s) > 0)) cnt++;
		v.clear();
		printf("Case #%d: %d\n",k ,cnt);
	}
	

	
	
return 0;
}
	