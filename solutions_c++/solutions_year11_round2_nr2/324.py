// B.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> a;
int n, d;

bool Check(double val)
{
	double pre = -1e100;
	for(int i = 0; i<n; ++i){
		if(pre + d <= a[i]-val){
			pre = a[i]-val;
		}else if(pre + d <= a[i]+val){
			pre = pre + d;
		}else{
			return false;
		}
	}
	return true;
}

double Solve()
{
	a.clear();
	int m;
	scanf("%d%d", &m, &d);
	n = 0;
	for(int i = 0; i<m; ++i){
		int x, y;
		scanf("%d%d", &x, &y);
		n += y;
		while(y--)
			a.push_back(x);
	}
	sort(a.begin(), a.end());
	if(Check(0))
		return 0;
	double l, r, mid;
	l = 0;
	r = 1;
	while(!Check(r))
		r += r;
	while(r-l >= 1e-4){
		mid = (l+r)/2;
		if(Check(mid))
			r = mid;
		else
			l = mid;
	}
	return (l+r)/2;
}

int main()
{
//  	freopen("B-small-attempt0.in", "r", stdin);
//  	freopen("B-small.out", "w", stdout);
// 
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: %.4f\n", i, Solve());
	}
	return 0;
}

