#include <iostream>
#include <string>
#include <map> 
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>


using namespace std;

#define sqr(x) ((x)*(x))
#define PB(a) push_back(a)
#define MP(a) make_pair(a)
#define ll long long

int gcd(int a, int b) {
	while (b) b^=a^=b^=a%=b;
	return a;
}

const int maxn=10010;

int n,x;
int d[maxn],l[maxn];
int g[maxn];
int k[maxn];
bool vis[maxn];

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tests;
	scanf("%d",&tests);
	for (int test=0; test<tests; test++) {
		bool ans=false;
		scanf("%d",&n);
		for (int i=0; i<n; i++) 
			scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&x);

		for (int i=0; i<n; i++)
			g[i]=k[i]=0;
		/*for (int i=0; i<n; i++) {
			if (l[i]-(d[i]-d[0])>g[0]) {
				g[0]=l[i]-(d[i]-d[0]);
				k[0]=i;
			}
		}*/
		g[0]=d[0];


		for (int i=0; i<n; i++) {
			if (g[i]+d[i]>=x) {
				ans=true; break;
			}
			for (int j=i+1; j<n; j++) {
				if (g[i]>=d[j]-d[i])
					g[j]=max(g[j],min(d[j]-d[i],l[j]));
			}
		}

		
		printf("Case #%d: ",test+1);
		printf((ans?"YES":"NO"));
		printf("\n");
	}

	return 0;
}