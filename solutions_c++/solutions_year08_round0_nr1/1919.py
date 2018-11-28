#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))

int cas;

int a[2000][200];
int v[2000], n;

char name[200][200], str[200];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&cas);
	int lv,i, j, s, q, ans;
	for(lv=1;lv<=cas;lv++) {
		scanf("%d",&s); gets(str);
		for(i=0;i<s;i++) gets(name[i]); //printf("%s\n", name[i]); } //printf("\n");
		scanf("%d",&q); gets(str);
		for(n=i=0;i<q;i++) {
			gets(str);
			for(j=0;j<s;j++) if(strcmp(name[j],str)==0) { v[n++]=j; break; } 
		}
		for(j=0;j<s;j++) a[0][j]=0;
		int k;
		for(i=0;i<n;i++) {
			k=v[i]; a[i+1][k]=q+1;
			for(j=0;j<s;j++) if(j!=k) {
				a[i+1][j]=min(a[i][j],a[i][k]+1);
			}
		}
		ans=n;
		for(i=0;i<s;i++) if(a[n][i]<ans) ans=a[n][i];
		
		printf("Case #%d: %d\n", lv, ans);
	}
	return 0;
}