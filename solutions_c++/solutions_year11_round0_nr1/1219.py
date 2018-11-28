#include <cstdio>
#include <algorithm>

using namespace std;

typedef pair<bool, int> pbi;

pbi a[111];

int main(){
	int t, n, p[2], x[2], now_on, ans;
	char tmp;
	scanf("%d", &t);
	bool u[2];
	
	for (int j = 1; j <= t; j++){
		p[0] = p[1] = 1;
		now_on = 0;
		ans = 0;
		x[0] = x[1] = -1;
		scanf("%d", &n);
		
		for (int i = 0; i < n; i++){
			scanf(" %c%d", &tmp, &a[i].second);
			a[i].first = (tmp == 'B');
			if (x[a[i].first] == -1)
				x[a[i].first] = a[i].second; 
		}
		
		while (now_on != n){
			u[0] = u[1] = false;

			if (p[a[now_on].first] == a[now_on].second){
				u[a[now_on].first] = true;
				for (int i = now_on + 1; i < n; i++)
					if (a[i].first == a[now_on].first){
						x[a[now_on].first] = a[i].second;
						break;
					}
				now_on++;
			}
			
			if (!u[0]){
				if (p[0] < x[0]) p[0]++;
				if (p[0] > x[0]) p[0]--;
			}
			
			if (!u[1]){
				if (p[1] < x[1]) p[1]++;
				if (p[1] > x[1]) p[1]--;
			}
			
			ans++;
		}
		
		printf("Case #%d: %d\n", j, ans);
	}
}
