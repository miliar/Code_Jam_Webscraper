#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int n,a[100];
char s[100][100];
int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		for (int i=0; i<n; i++){
			scanf("%s",s[i]);
			for (int j=0; j<n; j++) if (s[i][j]=='1') a[i]=j;
		}
		int ans=0;
		for (int i=0; i<n; i++){
			if (a[i]<=i) continue;
			int x; 
			for (x=i; a[x]>i; x++) ;
			int k=a[x];
			for (int j=x; j>i; j--){ ans++;  a[j]=a[j-1]; }
			a[i]=k;
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
