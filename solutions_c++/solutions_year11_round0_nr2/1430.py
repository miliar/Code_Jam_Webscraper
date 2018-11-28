#include <stdio.h>
#include <string.h>
#include <string>
#define maxn 110
using namespace std;
int a[maxn][maxn];
int b[maxn][maxn];
int n;
int tn,casen;
int m;
char ans[1000];
int main(){
	int i,j,k;
	for (scanf("%d",&tn),casen=1;casen<=tn;casen++){
		memset(a,-1,sizeof(a));
		for (scanf("%d",&k);k>0;k--){
			char s[10];
			scanf("%s",s);
			a[s[0]-'A'][s[1]-'A']=s[2]-'A';
			a[s[1]-'A'][s[0]-'A']=s[2]-'A';
		}
		memset(b,0,sizeof(b));
		for (scanf("%d",&k);k>0;k--){
			char s[10];
			scanf("%s",s);
			b[s[0]-'A'][s[1]-'A']=1;
			b[s[1]-'A'][s[0]-'A']=1;
		}
		scanf("%d",&n);
		char s[1000];
		m=0;
		scanf("%s",s);
		for (i=0;i<n;i++){
			if (m>0){
				if (a[ans[m-1]-'A'][s[i]-'A']>-1){
					ans[m-1]=a[ans[m-1]-'A'][s[i]-'A']+'A';
				}else{
					k=0;
					for (j=m-1;j>=0;j--)
						if (b[ans[j]-'A'][s[i]-'A']){
							m=0;
							k=1;
							break;
						}
					if (!k) ans[m++]=s[i];
				}
			}else ans[m++]=s[i];
		}
		printf("Case #%d: [",casen);
		for (i=0;i<m;i++){
			if (i>0) printf(", ");
			printf("%c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}
