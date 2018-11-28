#include<stdio.h>
#include<string.h>

int n,m,mark[1001];
char s[101][101],q[1001][101];

int main() {
	int cs,ct,i,j,k;
	scanf("%d",&cs);
	for (ct=1;ct<=cs;ct++) {
		scanf("%d",&n);
		gets(s[0]);
		for (i=0;i<n;i++) gets(s[i]);			
		scanf("%d",&m);
		gets(q[0]);
		for (i=0;i<m;i++) gets(q[i]);
		int ans=0,count=0;
		i=0;
		for (i=0;i<m;) {
			memset(mark,0,sizeof(mark));
			count = 0;
			while (i<m) {
				for (j=0;j<n;j++)
				if (!mark[j] && strcmp(q[i],s[j])==0) {
					mark[j]=1;
					count++;
					break;
				}
				i++;
				if (count==n) { 
					i--;
					break; 
				}
			}
			if (count>0) ans++;
		}
		if (ans>0) ans--;
		printf("Case #%d: %d\n",ct,ans);
	}
	return 0;
}
