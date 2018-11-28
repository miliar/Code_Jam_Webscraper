#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int i, j, k, m, n, l, p, cnt, curr;
int a[101], q[10001];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt, tn;
	cin >> tn;

	F1(tt,tn) {
		printf("Case #%d: ", tt);
		cnt=0;n=1;
		cin >> p >> k >> l;
		//printf("%d %d %d\n", p,k,l);
		F0(i,l) cin >> a[i];
		while (1){
			j=0;
			F0(i,l) {if (a[i]==0) {j++;}}
			if (j==l) break;
			m=k;
			while (m>0){
			curr=0;
			F0(i,l) {if (a[i]>curr) {curr=a[i];j=i;}}
			//printf("%d\n", cnt);
			cnt=cnt+curr*n;a[j]=0;
			m--;
			}
			n++;
			}
		printf("%d\n", cnt);
	}

	return 0;
}
