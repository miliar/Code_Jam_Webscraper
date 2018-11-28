#include<stdio.h>
#include<string.h>
int n;
char s[42];
int p[42];
void solve()
{
	int ans = 0;
	for(int i=1; i <= n; i++){
		if(p[i]>i){
			for(int j=i+1; j <=n; j++){
				if(p[j]<=i){
					ans += j-i;
					int t = p[j];
					for(int k = j; k > i; k--)p[k] = p[k-1];
					p[i] = t;
					break;
				}
			}
		}
	}
	//for(int i=1;i<=n;i++)printf("%d ", p[i]);
	printf("%d\n",ans);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A1.out","w",stdout);
	int tcase;
	scanf("%d",&tcase);
	for(int i =1; i <= tcase; i++){
		scanf("%d",&n);
		for(int j = 1; j <= n; j++){
			scanf("%s",s+1);
			p[j] = 	0;
			for(int k = n; k >= 1; k--)
				if(s[k]=='1'){
					p[j] = k;
					break;
				}	
		}
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
