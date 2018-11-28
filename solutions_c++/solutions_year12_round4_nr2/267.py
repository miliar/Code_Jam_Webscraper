#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	
	scanf("%d", &t);
	
	for(int time = 1; time <= t; ++time) {
	
		int n, w, h;
		pair<int, int> r[1000];
		pair<int, int> ans[1000];
		
		scanf("%d%d%d", &n, &w, &h);
		for(int i = 0; i < n; ++i) {
			int temp;
			scanf("%d", &temp);
			r[i].first = -temp;
			r[i].second = i;
		}
		
		sort(r, r + n);
		
		int x = 0, y = 0;
		int py = -r[0].first;
		
		
		for(int i = 0; i < n; ++i) {
		
			ans[r[i].second] = make_pair(x, y);
			
			if(i < n - 1) {
			
				int cr = -r[i].first;
				int nr = -r[i + 1].first;
			
				x += cr + nr;
				if(x > w) {
				
					y += cr + py;
					x = 0;
					py = cr;
				}
				
				if(y > h) {
				
					printf("[Error]\n");
				}
			}
		}
		
		printf("Case #%d:", time);
		for(int i = 0; i < n; ++i)
			printf(" %d.0 %d.0", ans[i].first, ans[i].second);
		printf("\n");
	}
	
	return 0;
}