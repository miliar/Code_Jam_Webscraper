#include<cstdio>
#include<algorithm>

using namespace std;

const int maxn = 1e4+7;

int d[maxn], l[maxn], h[maxn];
int n, i,j,dist;

void testcase(){
	scanf("%d",&n);
	for(i=0;i<n;++i)
		scanf("%d %d", d+i, l+i);
	scanf("%d", &dist);
	
	h[0] = d[0];
	if(dist <= d[0]+h[0]){
		printf("YES\n");
		return;
	}

	for(i=1;i<n;++i){
		h[i] = 0;
		for(j=0;j<i;++j){
			if(d[j] + h[j] >= d[i] && min(d[i]-d[j], l[i]) > h[i])
				h[i] = min(d[i] - d[j], l[i]);
		}
		if(d[i]+h[i] >= dist){
			printf("YES\n");
			return;
		}
	}

//	for(i=0;i<n;++i)
//		printf("%d (%d, %d) " , h[i], d[i], l[i]);
//	printf("\n");
	printf("NO\n");
}

int t, ti;

int main(){
	scanf("%d", &t);
	for(ti=0;ti<t;++ti){
		printf("Case #%d: ", ti+1);
		testcase();
	}
	return 0;
}
