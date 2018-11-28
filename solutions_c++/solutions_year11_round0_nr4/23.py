#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
const int maxn = 1000+5;
int n, a[maxn];

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D.out","w",stdout);

	int TextNum, Num = 0;
	scanf("%d",&TextNum);
	while (TextNum--) {
		printf("Case #%d: ",++Num);
		double S = 0;
		scanf("%d",&n);
		for (int i = 0; i != n; ++i) {
			scanf("%d",&a[i]);
			if (a[i] != i+1) S = S+1;
		}
		printf("%.6lf\n",S);
	}
	return 0;
}