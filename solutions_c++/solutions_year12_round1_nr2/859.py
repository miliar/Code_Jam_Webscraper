#include <cstdio>
#include <algorithm>
#define maxn 1100
#define inf 1000000

using namespace std;
pair<int, int> s[maxn];
int t, ans, n, stars;
bool found;

bool cmp(pair<int, int> a, pair<int, int> b){
	return a.second < b.second;
}

int main(){
	scanf("%d", &t);
	for (int j = 1; j <= t; j++){
		scanf("%d", &n);
		
		for (int i = 0; i < n; i++)
			scanf("%d%d", &s[i].first, &s[i].second);
			
		sort(s, s + n, cmp);
		
		ans = stars = 0;
		while (1){
			found = false;
			for (int i = 0; i < n; i++)
				if (s[i].second <= stars){
					if (s[i].first <= stars){
						stars += 2;
						s[i].first = s[i].second = inf;
					} else {
						stars++;
						s[i].second = inf;
					}
					
					found = true;
					ans++;
				}
			if (found){
				if (stars == n * 2){
					printf("Case #%d: %d\n", j, ans);
					break;
				}
				continue;
			}
			for (int i = n - 1; i >= 0; i--)
				if (s[i].first <= stars){
					s[i].first = inf;
					stars++;
					ans++;
					
					found = true;
					break;
				}
				
			if (!found){
				printf("Case #%d: Too Bad\n", j);
				break;
			} else
				if (stars == n * 2){
					printf("Case #%d: %d\n", j, ans);
					break;
				}
		}
	}
}
