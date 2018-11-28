#include<stdio.h>
#include<string.h>
#define MAXN 10005
int n, l, h;
int v[MAXN];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int tcase;
	scanf("%d", &tcase);
	for(int ts = 1; ts <= tcase; ts++){
		scanf("%d%d%d",&n,&l,&h);
		for(int i = 0; i < n; i++){
			scanf("%d",&v[i]);
		}
		int ans = -1;
		for(int i = l; i <= h; i++){
			int flag = 1;
			for(int j = 0; j < n; j++){
				if(!(i%v[j] == 0 || v[j]%i == 0)){
					flag = 0;
					break;
				}
			}
			if(flag){
				ans = i;
				break;
			}
		} 
		printf("Case #%d: ", ts);
		if(ans == -1)
			printf("NO\n");
		else
			printf("%d\n",ans);
	}	
	return 0;
}
