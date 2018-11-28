#include<stdio.h>
#include<string.h>

const int maxn = 100;
const int maxm = 1000;
int n, m;
char s[maxn][103];
char q[maxm][103];
bool kick[maxn];

int main() {
	//freopen("a2.in","r",stdin);
	//freopen("a.out","w",stdout);
	int cs;
	scanf("%d",&cs);
	int step = 1;
	while(cs--){
		int i,j,k;
		scanf("%d",&n);
		gets(s[0]);
		for(i=0;i<n;i++){
			gets(s[i]);			
		}
		scanf("%d",&m);
		gets(q[0]);
		for(i=0;i<m;i++){
			gets(q[i]);
		}
		int ans = 0;
		int count = 0;
		i=0;		
		while(i<m){
			memset(kick, 0, sizeof(kick));
			count = 0;
			while(i<m){
				for(j=0;j<n;j++)if(!kick[j] && strcmp(s[j], q[i])==0){
					kick[j] = 1;
					count++;
					break;
				}
				i++;
				if(count==n) {i--; break;}
			}
			if(count>0) ans ++;
		}
		if(ans>0) ans--;
		printf("Case #%d: %d\n", step++, ans);
	}
	return 0;
}