#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <iostream>
#include <string>
#include <algorithm>
#define intine 0x1f1f1f1f

using namespace std;
#define MP make_pair
typedef pair<int,int> Pair;
typedef vector<int> Vector;

double a[1200];
double sum;
int L, C, N, t;

double save(double total,int l,int r,int k){
	if(k < l || k > r) return 0;  // save 0;
	double pre = total;
	if(pre >= t) return a[k];
	else if(pre + a[k]*2 <= t) return 0;
	else{
		double tmp = (t - pre)/2.0;
		return a[k]-tmp;
	}
}
double take(int k){
	double ttt = 0;
	for(int i = 0;i < k; ++i)ttt += a[i];
	ttt *= 2.0;
	return sum - save(ttt,0,N,k);
}
double tttt(int j,int k){
	double ttt = 0;
	for(int i = 0;i < j; ++i) ttt += a[i];
	double ss = save(ttt*2.0,0,N,j), tt = 0;
	for(int i = 0;i < k; ++i) tt += a[i];
	tt *= 2.0;
	return sum - ss - save(tt-ss,j+1,N,k);
	
}
int main()
{
	freopen("in.txt","r", stdin);
    freopen("out.txt","w", stdout);
	int T;
	scanf("%d",&T);
	for(int it = 1;it <= T; ++it){
		scanf("%d%d%d%d",&L,&t,&N,&C);
		printf("Case #%d: ",it);
		for(int i = 0;i < C; ++i){
			scanf("%lf",&a[i]);
		}
		for(int i = C;i < N; ++i){
			a[i] = a[i%C];
		}
		sum = 0.0;
		for(int i = 0;i < N; ++i){
			sum += a[i];
		}
		sum *= 2.0;
		if(L == 0) printf("%.0lf\n",sum);
		else if(L == 1){
			double ret = intine;
			for(int i = 0;i < N; ++i){
				int tmp = take(i);
				if(tmp < ret)  ret = tmp;
			}
			printf("%.0lf\n",ret);
		}else if(L == 2){
			double ret = intine;
			for(int i = 0;i < N; ++i)
				for(int j = i+1;j < N; ++j){
					int tmp = tttt(i,j);
					if(tmp < ret) ret = tmp;
				}
			printf("%.0lf\n",ret);
		}
	}
	
	
}
