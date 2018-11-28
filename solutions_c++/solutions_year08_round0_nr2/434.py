#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
struct trip{
	int st,et;
	bool go;
	bool operator > (const trip &a)const{ return st>a.st; }
	bool operator < (const trip &a)const{ return st<a.st; }
};
trip a[300];
bool vis[300];
int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		int rt; scanf("%d",&rt);
		int na,nb; scanf("%d%d",&na,&nb);
		for (int i=0; i<na+nb; i++){
			int hh,mm;
			scanf("%d:%d",&hh,&mm); a[i].st=hh*60+mm;
			scanf("%d:%d",&hh,&mm); a[i].et=hh*60+mm+rt;
			a[i].go=i<na;
		}
		int ans[2]={0,0},n=na+nb;
		sort(a,a+n);
		memset(vis,0,sizeof(vis));
		for (int i=0; i<n; i++){
			if (vis[i]) continue;
			bool dir=a[i].go;
			ans[!dir]++;
			int t=a[i].st;
			for (int j=i; j<n; j++){
				if (t>a[j].st || dir!=a[j].go || vis[j]) continue;
				vis[j]=true;
				t=a[j].et;
				dir=!dir;
			}
		}
		printf("Case #%d: %d %d\n",tt,ans[0],ans[1]);
	}
	return 0;
}
