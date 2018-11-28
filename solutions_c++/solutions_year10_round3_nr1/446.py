#include<stdio.h>
#include<algorithm>
using namespace std;
struct point{
	int a,b;
}line[1005];
bool cmp(const point &a,const point &b){
	return a.a<b.a;
}
int main(){
	int n;
	int T;
	int i,j;
	int ans;
	int cases=0;
	freopen("e:\\A-large.in","r",stdin);
	freopen("e:\\A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d %d",&line[i].a,&line[i].b);
		}
		sort(line,line+n,cmp);
		ans=0;
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				if(line[i].b>line[j].b) ans++;
			}
		}
		printf("Case #%d: %d\n",++cases,ans);
	}
	return 0;
}