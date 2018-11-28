#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <iostream>
using namespace std;



int main()
{
	freopen("C-Large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
/*	freopen("in.txt", "r", stdin);*/

	int T, cases = 1;
	int a, b;

	scanf("%d", &T);
	while(cases <= T){
		set<pair<int, int>> myset;
		scanf("%d%d", &a, &b);
		
		if(b <= 9){
			printf("Case #%d: 0\n", cases);
			cases ++;
			continue;
		}

		int s, cnt;
		int t, tn;
		cnt = 0;
		s = 1;
		t = b;
		while(t >= 10){
			s *= 10;
			cnt ++;
			t /= 10;
		}

// 		if(b <= 99){
// 			s = 10;
// 			cnt = 1;
// 		}
// 		else if(b <= 999){
// 			s = 100;
// 			cnt = 2;
// 		}
// 		else{
// 			s = 1000;
// 			cnt = 3;
// 		}

		
		int ans = 0;
		for(int i=a; i<=b; ++i){
			tn = 0;
			t = i;
			while(tn < cnt){
				tn ++;
				t = t % 10 * s + t / 10;

				if(t > i && t <= b){
					//printf("%d %d\n", i, t);
					if(myset.count(make_pair(i, t)) == 0){
						myset.insert(make_pair(i, t));
						ans ++;
					}
				}
			}
		}

		printf("Case #%d: %d\n", cases, ans);
		cases ++;
	}
}