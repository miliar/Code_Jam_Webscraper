#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

int T, m, n, a[5000], b[5000];

int main(){
	scanf("%d", &T);
	for (int tt = 1; tt<=T; tt++){
		int cnt = 0;
		printf("Case #%d: ", tt);
		scanf("%d", &m);
		for (int i=0; i<m; i++)
			scanf("%d%d", &a[i], &b[i]);
		for (int i=0; i<m; i++)
			for (int j=i+1; j<m; j++)
				if ((a[i]>a[j] && b[i]<b[j]) || (a[i]<a[j] && b[i]>b[j]))
					cnt++;
		printf("%d\n", cnt);
	}
	return 0;
}
