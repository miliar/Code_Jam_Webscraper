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
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int i,j,n,m,k,t,x,y;
	scanf("%d",&t);
	for(j=1;j<=t;j++){
		scanf("%d",&n);
		m = 0; k = INF;	y = 0;
		for(i=1;i<=n-1;i++){
			scanf("%d",&x);
			m += x;
			k = min(k,x);
			y = y ^ x;
		}
		scanf("%d",&x);
		m += x;
		k = min(k,x);
		printf("Case #%d: ",j);
		if(y == x) printf("%d\n",m-k); 
		else printf("NO\n");
	}		
	fclose(stdin);
	fclose(stdout);
	return 0;
}

