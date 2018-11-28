#include<cstdio>
char a[1000];
int b[1000];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++){
		
		int n;
		scanf("%d",&n);
//		printf("n=%d\n",n);
		for (int i=1;i<=n;i++){
			for (a[i]=getchar();a[i]!='O'&&a[i]!='B';a[i]=getchar());
			scanf("%d",&b[i]);
		}
		int x=1,y=1,s=1,t=1,now=1,ans=0;
		while (s<=n&&a[s]!='O')s++;
		while (t<=n&&a[t]!='B')t++;
		while (s<=n||t<=n){
//			printf("%d %d %d %d %d\n",x,y,s,t,now);
			int tmp=now;
			if (s<=n){
				if (s==now&&x==b[s]){
					now++;s++;
					while (s<=n&&a[s]!='O')s++;
				}else if (x<b[s])x++;
				else if (x>b[s])x--;
			}
			if (t<=n){
				if (t==tmp&&y==b[t]){
					tmp++;t++;
					while (t<=n&&a[t]!='B')t++;
				}else if (y<b[t])y++;
				else if (y>b[t])y--;
			}
			if (tmp>now)now=tmp;
			ans++;
		}
//		printf("%d %d %d %d\n",x,y,s,t);
		printf("Case #%d: %d\n",TT,ans);
	}
	return 0;
}
