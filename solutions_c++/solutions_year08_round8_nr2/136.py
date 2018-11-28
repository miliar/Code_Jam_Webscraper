#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int nmax = 11;

struct el{
	string col;
	int l,r;
};

el a[nmax];

bool check(int k,int n){
	int num = 0,ma = 0;
	string color[nmax];

	for (int i = 0;i < n; ++i)
		if ((k & (1 << i)) > 0){
			int t = -1;
			for (int j = 0;j < num; ++j)
				if (a[i].col == color[j]) {
					t = 0;
					break;
				}
			if (t == -1) color[num++] = a[i].col;

			if (num > 3) return false;
			if (a[i].l > ma + 1) return false;
			ma = max(ma,a[i].r);
		}
	return ma >= 10000;	
}

int num(int k,int n){
	int sum = 0;
	for (int i = 0;i < n; ++i)
		if ((k & (1 << i)) > 0) ++sum;
	return sum;
}

void rec(int n){
	int best = 10000;

	for (int i = 0;i < (1 << n); ++i)
		if (check(i,n)){
			int cur = num(i,n);
			if (cur  < best) 
				best = cur;
		}
	if (best < 10000) cout << best << endl;
	else cout << "IMPOSSIBLE" << endl;
}

bool cmp(el a,el b){
	return a.l < b.l;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int test;
	cin >> test;

	for (int t = 1;t <= test; ++t){
		int n;
		cout << "Case #" << t << ": ";
		cin >> n;
		for (int i = 0;i < n; ++i) cin >> a[i].col >> a[i].l >> a[i].r;
		sort(a,a+n,cmp);
		rec(n);
	}


	return 0;
}