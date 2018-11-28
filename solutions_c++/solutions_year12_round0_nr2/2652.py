#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int t, n , k, s, ans, ar[105];
pair<int,int> p[105];


int main()
{
	freopen("dance.in","r",stdin); freopen("dance.out","w",stdout);
	int i, tc;
	scanf("%d", &t);
	for (tc = 0; tc < t; tc++)
	{
		ans = 0;
		scanf("%d %d %d", &n, &s, &k);
		for (i = 0; i < n; i++) scanf("%d", &ar[i]);
		sort( ar, ar+n);
		reverse( ar, ar+n);
		for (i = 0; i < n; i++) 
		{
			p[i] = make_pair( ar[i]/3 + ar[i] % 3, ar[i]%3 );
			if ( p[i].first > 10 ) { p[i].first = 10; p[i].second = 1; }
			
			if ( s > 0 && p[i].first + 1 == k && p[i].second == 0) 
			{ 
				++ans; --s; 
			}
			
			if ( p[i].second == 2 && s == 0) --p[i].first;

			if ( p[i].second == 2 && s > 0) --s;
			
			if ( p[i].first >= k ) ++ans;
			//printf("%d %d\n", ans, s);
		}
		printf("Case #%d: %d\n", tc+1, ans);
	}
}