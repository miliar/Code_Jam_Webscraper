#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 1000;
int i, ans, n, s, p; 
int a[N];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int test = 1; test <= t; test++){
		scanf("%d%d%d",&n,&s,&p);
		for (i = 0; i < n; i++)
			scanf("%d",&a[i]);
		sort(a, a + n);
		reverse(a, a + n);
		ans = 0;
		for (i = 0; i < n; i++){
			if (a[i] >= 3 * p - 2){
				ans ++;
				continue;
			}
			if (s && a[i] >= 3 * p - 4 && p >= 2){
				ans ++;
				s --;
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}