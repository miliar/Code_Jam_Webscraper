#include <cstdio>
#include <map>

using namespace std;

int t, a, b, p[2000001], c;
map<int, int> m;

int min(int n){
	int k = n;
	int o = 1;
	while(o < n) o *= 10;
	for(int i = 0, j = n; i < 10; i++){
		j = (j * 10) % o + j * 10 / o;
		if (j < k && j * 10 >= o) k = j;
	}
	return k;
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("\n");
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		scanf("%d%d", &a, &b);
		for(int j = a, k; j <= b; j++){
			m[min(j)]++;
		}
		c = 0;
		for(map<int, int>::iterator j = m.begin(); j != m.end(); j++){
			c += (j->second) * (j->second - 1) / 2;
		}
		printf("%d\n", c);
		m.clear();
	}
	return 0;
}

