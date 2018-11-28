#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define eps 1e-8

struct node{
	int l, w;
}a[1005];

bool cmp(const node& lm, const node& rm){
	return lm.w < rm.w;
}
int main(){
	freopen("A-large.in","r", stdin);
	freopen("a.out", "w", stdout);
	int T; cin >>T;
	for (int cas = 1; cas <= T; cas++){
		int X, S, R, t, N;
		cin >>X>>S>>R>>t>>N;
		int i, j;
		int sum = 0;
		for (i = 1; i <= N; i++){
			int bi, ei;
			scanf("%d%d%d", &bi, &ei, &a[i].w);
			a[i].l = ei - bi;
			sum += a[i].l;
		}
		a[0].l = X - sum;
		a[0].w = 0;
		sort(a, a + N + 1, cmp);
		double tt = t;
		double Y = 0;
		for (i = 0; i <=N && tt > eps; i++){
			if (a[i].l *1.0/(a[i].w + R) + eps <= tt)
			{
				double tmp = a[i].l * 1.0 / (a[i].w+R);
				tt-=tmp;
				Y+=tmp;
			}else
				break;
		}
		if (i <= N && tt > eps){
			double tmp = (a[i].w + R)*tt;
			Y+=tt;
			Y+=(a[i].l*1.0-tmp) / (a[i].w+S);
			i++;
		}
		for (; i <= N; i++)
			Y+=(a[i].l*1.0)/(a[i].w+S);
		printf("Case #%d: %.7lf\n", cas, Y);
	}
	return 0;
}
