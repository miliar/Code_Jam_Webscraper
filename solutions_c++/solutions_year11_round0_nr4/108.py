#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
using namespace std;
double dp[1011];

int main(){
	int i, j, k, m, n, cas;
	freopen("D-large.in", "r", stdin);
	freopen("w.txt", "w", stdout);
	for(i = 2; i <= 1000; i++)
		dp[i] = i;
	scanf("%d", &cas);
	for(int ri = 1; ri <= cas; ri++){
		printf("Case #%d: ", ri);
		scanf("%d", &n);
		vector<int> a, b;
		for(i = 0; i < n; i++){
			scanf("%d", &k);
			a.push_back(k);
		}
		b = a;
		sort(b.begin(), b.end());
		for(i = 0; i < n; i++){
			for(j = 0; j < n; j++)
				if(a[i] == b[j])
					a[i] = j;
		}
		double tmp = 0;
		int v[1010] = {0};
		for(j = 0; j < n; j++){
			int u = 0;
			int next = j;
			while(!v[next]){
				u++;
				v[next] = 1;
				next = a[next];
			}
			tmp += dp[u];
		}
		printf("%.15lf\n", tmp);
	}
	scanf("%*d");
}
