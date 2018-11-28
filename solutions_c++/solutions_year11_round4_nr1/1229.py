#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long ll;
#define INF 0x3f3f3f3f
#define CLR(a, b) (memset(a, b, sizeof(a)))
#define N 1010
int ps[N], pe[N], pv[N];
double sum[110];

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int cas; scanf("%d", &cas);
	for(int ct = 0; ct < cas; ct++){
		int x, s, r, t, n, i;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		for(i = 0; i < 110; i++)
			sum[i] = 0.0;
		int cnt = 0;
		for(i = 0; i < n; i++){
			scanf("%d%d%d", &ps[i], &pe[i], &pv[i]);
			sum[pv[i]] += pe[i] - ps[i];
			cnt += pe[i] - ps[i];
		}
		sum[0] += x - cnt;
//		for(int i = 0; i < 3; i++){
//			printf("%.3lf  ", sum[i]);
//		}
		double tt = (double)t, ttt = (double)t;
		for(i = 0; i < 110; i++){
			if(tt > 0 && (tt * (i + r) > sum[i])){
				tt -= sum[i] / (i + r);
			}
			else if(tt > 0){
				sum[i] -= tt * (i + r);
				tt = 0.0; break;
			}
			else break;
		}
//		printf("   ###%d    ", i);
		for(int j = i; j < 110; j++){
			ttt += sum[j] / (j + s);
		}
		if(tt > 0) printf("Case #%d: %.8lf\n", ct + 1, ttt - tt);
		else printf("Case #%d: %.8lf\n", ct + 1, ttt);
	}
	return 0;
}
