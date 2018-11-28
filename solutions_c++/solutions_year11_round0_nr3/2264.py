#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,ti;
	int n;
	scanf("%d",&T);
	for(ti=1;ti<=T;ti++){
		scanf("%d",&n);
		int m=1e8;
		int x=0,t,s=0;
		for(int i=0;i<n;i++){
			scanf("%d",&t);
			x^=t;
			s+=t;
			if(m>t)m=t;
		}
		printf("Case #%d: ",ti);
		if(x==0)printf("%d\n",s-m);
		else printf("NO\n");
	}
	return 0;
}
