#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

using namespace std;

int T;

struct Tp{
	double l,w;

	bool operator<(const Tp & B)const{
		return w < B.w;
	}
} a[22222];


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		
		double x,s,t,r;
		int n;

		cin >> x >> s >> r >> t >> n;

		double tl = 0;
		for(int i=0;i<n;i++){
			double b,e;
			cin >> b >> e >> a[i].w;
			a[i].l =  e - b;
			a[i].w += s;
			tl += a[i].l;
		}
		a[n].l = x - tl;
		a[n].w = s;
		sort(a, a + n + 1);

		double ans = 0;
		for(int i=0;i<=n;i++){
			if(  a[i].l / (r - s + a[i].w)  <= t){
				double tt = a[i].l / (r - s + a[i].w);
				t -= tt;
				ans += tt;
			}else{
				ans += (a[i].l - (t * (r - s + a[i].w))) / a[i].w + t;
				t = 0;
			}
		}
		
		cout.precision(7);
		printf("Case #%d: ",_);
		cout << fixed << ans << endl;
	}
	return 0;
}
