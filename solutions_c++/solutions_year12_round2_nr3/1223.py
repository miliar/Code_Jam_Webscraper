#include<iostream>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<set>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<cassert> 
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;


#define debug(x) cout << #x << " = " << x << "\n";
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i=0;i<n;i++)
#define fr2(i, a, n) for(i=a;i<n;i++)
#define mem(a, n) memset(a, n, sizeof(a))
typedef vector<int> VI;

void print(VI &v) {
	int l= v.sz;
	int i;
	fr(i, l) {
		printf("%d", v[i]);
		if(i!=l-1) {
			printf(" ");
		}
		else
			printf("\n");
	}
		
}
bool b;
void solve(int *a, int n, VI &x, VI &y, int id = 0, int s1 = 0 , int s2 = 0 ) {
	if(b)
		return;
	if(id==n)
		return;
	if(s1!=0 && s1==s2) {
		b = 1;
		print(x);
		print(y);
		return;		
	}
	solve(a, n, x, y, id + 1, s1, s2);
	x.push_back(a[id]);
	solve(a, n, x, y, id + 1, s1 + a[id], s2);
	x.pop_back();
	y.push_back(a[id]);
	solve(a, n, x, y, id + 1, s1, s2 + a[id]);
	y.pop_back();
	
	return;
}

void subsets(int *a, int n) {
	b = 0;
	VI x, y;
	solve(a, n, x, y);
	if(b==0)
		printf("Impossible\n"); 
}

int main() {
	int t;
	scanf("%d", &t);
	int n, m;
	for(int k=1;k<=t;k++) {
		scanf("%d", &n);
		int a[n];
		for(int i=0;i<n;i++) {
			scanf("%d", &a[i]);//cin >> a[i];
		}
		printf("Case #%d:\n", k);
		subsets(a, n);

	}
}
