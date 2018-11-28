#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

const double eps = 1e-9;

int b[1000005], e[1000005], b1[1000005], e1[1000005], h[1000005], h1[1000005];
double w[1000005], w1[1000005];
double x, s, r, t;
int n;

double game(){
	double ans = 0, ost;
	int i;
	for (i = 0;i < n;i++){
		if (b[i] != e[i]){
			if (t > 0){
				if (t * (w[i] - s + r) > (e[i] - b[i]) + eps){
					t -= (e[i] - b[i]) / (w[i] - s + r);
					ans += (e[i] - b[i]) / (w[i] - s + r);
				}else
				{
					ans += t;
					ost = (e[i] - b[i]) - t * (w[i] - s + r);
					ans += ost / w[i];
					t = 0;
				}
			}else
			{
				ans += (e[i] - b[i]) / w[i];
			}
		}
	}
	return ans;
}

bool cmp(int d1, int d2){
	return (b[d1] < b[d2]);
}

bool cmpw(int d1, int d2){
	return (w[d1] < w[d2]);
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t1, i;
	scanf("%d",&test);
	for (t1 = 0;t1 < test;t1++){
		if (t1)
			printf("\n");
		printf("Case #%d: ",t1 + 1);
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		for (i = 0;i < n;i++){
			h[i] = i;
			scanf("%d%d%lf",&b[i],&e[i],&w[i]);
			w[i] += s;
		}
		sort(h, h + n, cmp);
		for (i = 0;i < n;i++){
			b1[i] = b[h[i]];
			e1[i] = e[h[i]];
			w1[i] = w[h[i]];
		}
		for (i = 0;i < n;i++){
			b[i] = b1[i];
			e[i] = e1[i];
			w[i] = w1[i];
		}
		int sh = n;
		if (b[0] != 0){
			b[n] = 0;
			e[n] = b[0];
			w[n] = s;
			sh++;
		}
		for (i = 1;i < n;i++){
			if (e[i - 1] != b[i]){
				b[sh] = e[i - 1];
				e[sh] = b[i];
				w[sh] = s;
				h[sh] = sh;
				sh++;
			}
		}
		if (e[n - 1] != x){
			b[sh] = e[n - 1];
			e[sh] = x;
			w[sh] = s;
			h[sh] = sh;
			sh++;
		}
		n = sh;
		for (i = 0;i < n;i++){
			h[i] = i;
		}
		sort(h, h + n, cmpw);
		for (i = 0;i < n;i++){
			b1[i] = b[h[i]];
			e1[i] = e[h[i]];
			w1[i] = w[h[i]];
		}
		for (i = 0;i < n;i++){
			b[i] = b1[i];
			e[i] = e1[i];
			w[i] = w1[i];
		}
		printf("%.10lf",game());
	}
	return 0;
}