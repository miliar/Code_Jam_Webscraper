#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> now, sorted;

int main(){
	int t, n;
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d", &n);
		now.resize(n);
		for (int j = 0; j < n; j++)
			scanf("%d", &now[j]);
		sorted = now;
		sort(sorted.begin(), sorted.end());
		int s = 0;
		for (int j = 0; j < n; j++)
			s += sorted[j] != now[j];
		printf("Case #%d: %.06lf\n", i + 1, double(s));
	}
}
