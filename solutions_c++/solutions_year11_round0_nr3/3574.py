#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main(){
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i =0;i<n;i++){
		int a;
		scanf("%d",&a);
		int c[1010];
		int m = 0;
		for(int j=0;j<a;j++)scanf("%d",&c[j]);
		sort(c,c+a);
		for(int x=0;x<a-1;x++){
			int ra = 0;int rb = 0;int fa= 0;int fb = 0;
			for(int y=0;y<x+1;y++){
				ra += c[y];
				fa  = fa ^ c[y];
			}
			for(int y=x+1;y<a;y++){
				rb += c[y];
				fb = fb ^ c[y];
			}
			if(fa==fb && ra>m)m=max(ra,rb);
		}
		if(m>0)printf("Case #%d: %d\n",i+1,m);
		else printf("Case #%d: NO\n",i+1);
	}
	return 0;
}