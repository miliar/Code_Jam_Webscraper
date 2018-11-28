#include<stdio.h>
#include<string.h>
#define INF 1<<29

char s[200][200];
int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		int m; scanf("%d",&m); 
		char ss[100]; gets(ss);
		for (int i=0; i<m; i++) gets(s[i]);
		int n; scanf("%d",&n); gets(ss);
		int a[200];
		for (int i=0; i<m; i++) a[i]=0;
		while (n--){
			char c[200]; gets(c);
			int k=0;
			for (int i=0; i<m; i++){
				if (strcmp(c,s[i])==0) k=i;
			}
			int b[200];
			for (int i=0; i<m; i++){
				if (k==i) b[i]=INF;
				else{
					b[i]=a[i];
					for (int j=0; j<m; j++){
						if (a[j]+1<b[i]) b[i]=a[j]+1;
					}
				}
			}
			for (int i=0; i<m; i++) a[i]=b[i];
		}
		int ans=INF;
		for (int i=0; i<m; i++){
			if (a[i]<ans) ans=a[i];
		}
		printf("Case #%d: %d\n",tt,ans);

	}
	return 0;
}
