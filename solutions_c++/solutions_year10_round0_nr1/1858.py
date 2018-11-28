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
int i , t , n , k;
int a[1000] , b[1000];

inline bool solve ( int n , int K ) {
	return ((K & ((1 << n) - 1)) == ((1 << n) - 1));
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&t);
	
	for(i = 1 ; i <= t ; ++i ) {
		scanf("%d %d",&n,&k);
		printf("Case #%d: ",i);
		if ( solve(n,k) ) printf("ON\n");
			else printf("OFF\n");
	}
	
return 0;
}