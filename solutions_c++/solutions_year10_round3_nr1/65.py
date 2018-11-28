#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
#define	out(x) 		(cout << #x << ": " << x << endl)
#define	MM(m,what)	(memset(m, what, sizeof(m)))
template<class T>void show(T a, int l){for(int i = 0; i < l; ++i)cout << a[i] << ' '; cout << endl;}
template<class T>void show(T a, int l, int r){for(int i = 0; i < l; ++i)show(a[i], r); cout << endl;}
const int MAXN = 1010;
int a[MAXN], b[MAXN];

int main(){
	freopen("A-large.in", "r", stdin);	freopen("large.txt", "w", stdout);
	int T, n;
	scanf("%d", &T);
	for(int ks = 1; ks <= T; ++ks){
		scanf("%d", &n);
		int i, j, sum = 0;
		for(i = 0; i < n; ++i){
			scanf("%d%d", &a[i], &b[i]);
		}
		for(i = 0;i < n; ++i)
			for(j = i+1; j < n; ++j){
				if(a[i] > a[j] && b[i] < b[j])	++sum;
				else if(a[i] < a[j] && b[i] > b[j])	++sum;
			}
		printf("Case #%d: %d\n", ks, sum);
	}
	return 0;
}
