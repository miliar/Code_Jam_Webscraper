#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

typedef long long ll;

ll r , k , n;
ll g[1010];
ll p[1010];
ll h[1010];
ll ans[1010];
ll s[1010];

int main()
{

	freopen("test.in" , "r" , stdin);
	freopen("test.out" , "w" , stdout);
	int t ,cas = 0;
	scanf("%d" , &t);
	while ( t-- )
	{
		cas ++;
		scanf("%lld %lld %lld" , &r , &k , &n);
		for (int i = 0 ; i < n ; i ++)
			scanf("%lld" , &g[i]);

		memset(s , 0 , sizeof(s));
		memset(ans , 0 , sizeof(ans));
	
		for (int i = 0 ; i < n ; i ++){
			
			int pos = i;
			ll tot = 0;
			while (1){
				if (tot + g[pos] > k)break;
				tot += g[pos];
				pos = (pos + 1) % n;
				if (pos == i)break;
			}
			p[i] = pos;
			s[i] = tot;
		
		}

		//for (int i = 0 ; i < n ; i ++){
		//	printf("p[ %d ] = %d ; s[ %d ] = %d\n" , i , p[i] , i , s[i]);
		//}

		memset(h , 0 , sizeof(h));
		memset(ans , 0 , sizeof(ans));
		
		ll ret = 0;
		int head = 0;
		int cnt = 1;
		h[ head ] = cnt;
		ans[ cnt ] = s[head];
		ret += s[head];
		int len = 0;
		ll rep = 0;
		r --;
		while (r --){
			
			cnt ++;
			head = p[ head ];
			
			if (h[ head ] ){
				r ++;
				len = cnt - h[ head ];
				rep = ans[cnt - 1] - ans[ h[head] ] + s[ head ];
				break;
			}
			
			ans[cnt] = ans[cnt - 1] + s[ head ];
			ret += s[ head ];
			h[ head ] = cnt;
		}

	
		if (len != 0){
			ret += r/len * rep;
			r = r % len;
		}


		if (r >= 0)
		while (r --){
	
			ret += s[ head ];
			head = p[ head ];

		}


		printf("Case #%d: %lld\n" , cas , ret);

	}

}