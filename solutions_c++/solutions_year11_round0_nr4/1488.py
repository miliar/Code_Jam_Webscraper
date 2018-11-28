#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <queue>
#define EPS 1e-8
#define INF 100000000
#define MAXN 100050
#define PI 3.141592653
using namespace std;

int main() {
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int i,j,n,x,ans,t;
	scanf("%d",&t);
	for(j=1;j<=t;j++){
		scanf("%d",&n);
		ans = 0;
		for(i=1;i<=n;i++){
			scanf("%d",&x);
			if (x!=i) ans++;
		}
		printf("Case #%d: ",j);
		printf("%d.000000\n",ans); 
	}		
	fclose(stdin);
	fclose(stdout);
	return 0;
}

