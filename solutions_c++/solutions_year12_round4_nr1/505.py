#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<sstream>
#include<stack>
#include<queue>
#include<deque>
#include<iostream>
using namespace std;
#define sz(X) (int)X.size()
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define ll long long
#define pii pair<int,int>

int n, D;
int d[10010], l[10010], r[10010];

int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
			scanf("%d %d",&d[i],&l[i]);
		scanf("%d",&D);
		memset(r,0,sizeof(r));
		r[1] = d[1];
		for(int i=2;i<=n;i++){
			for(int j=1;j<i;j++){
				if(d[j] + r[j] >= d[i]){
					r[i] = max(r[i], min(l[i],d[i]-d[j]));
				}
			}
		}
		int i;
		for(i=1;i<=n;i++)
			if(d[i] + r[i] >= D)
				break;
		if(i<=n)
			printf("Case #%d: YES\n",caso);
		else printf("Case #%d: NO\n",caso);
	}
	return 0;
}
