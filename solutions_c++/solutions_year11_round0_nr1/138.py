#include<stdio.h>
#include<string.h>
#define MAXN_PRESS 105
#define abs(a) ((a)<0?-(a):(a))
struct Press{
	int robot;
	int button;
}press[MAXN_PRESS];

int solve(int n)
{
	int ans = 0;
	int p0 = 1;
	int p1 = 1;
	int t = 0;
	for(int i = 1; i <= n; i++){
		if(press[i].robot == 0){
			int addt = abs(p0-press[i].button)+1;
			t += addt;
			p0 = press[i].button;
			for(int j = i+1; j <= n; j++){
				if(press[j].robot == 1){
					if(press[j].button > p1){
						p1 += addt;
						p1 = (p1 > press[j].button?press[j].button:p1);	
					}else{
						p1 -= addt;
						p1 = (p1 < press[j].button?press[j].button:p1);	
					}
					break;
				}
			}
		}else{
			int addt = abs(p1-press[i].button)+1;
			t += addt;
			p1 = press[i].button;
			for(int j = i+1; j <= n; j++){
				if(press[j].robot == 0){
					if(press[j].button > p0){
						p0 += addt;
						p0 = (p0 > press[j].button?press[j].button:p0);	
					}else{
						p0 -= addt;
						p0 = (p0 < press[j].button?press[j].button:p0);	
					}
					break;
				}
			}
		}
	}
	return t;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T, x, n;
	char str[10];
	scanf("%d",&T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d",&n);
		for(int i = 1; i <= n; i++){
			scanf("%s %d",str,&x);
			press[i].robot = (str[0]=='B' ? 0 : 1);
			press[i].button = x;
		}
		printf("Case #%d: %d\n", t, solve(n));
	}
	return 0;
}
