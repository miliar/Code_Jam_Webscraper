#include <cstdio>
#include <cstring>
int d[1111][1111];
char *goal = "welcome to code jam";
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		char s[1111];
		scanf("%[^\n]\n",s);
		memset(d,0,sizeof(d));
		int len = strlen(s);
		for(int i=0; i<len; i++){
			if(s[i]=='w')
				d[0][i]=1;
		}
		for(int i=1; i<=18; i++){
			for(int j=i; j<len; j++){
				if(s[j]==goal[i]){
					for(int k=0; k<j; k++){
						d[i][j]+=d[i-1][k];
						d[i][j] %= 10000;
					}
				}
			}
		}
		int ans = 0;
		for(int i=0; i<len; i++)
			ans += d[18][i];
		ans %= 10000;
		printf("Case #%d: %04d\n",tc,ans);
	}
}
	