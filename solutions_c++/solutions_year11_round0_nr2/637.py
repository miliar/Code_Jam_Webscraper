#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
char a[200][200];
bool b[200][200];
char ans[110];
int len;
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++){
		memset(a,0,sizeof a);
		memset(b,0,sizeof b);
		memset(ans,0,sizeof ans);
		len=0;
		int C,D,n;
		scanf("%d",&C);
		for (int i=1;i<=C;i++){
			char s[10];
			scanf("%s",s);
			a[s[0]][s[1]]=a[s[1]][s[0]]=s[2];
		}
		scanf("%d",&D);
		for (int i=1;i<=D;i++){
			char s[10];
			scanf("%s",s);
			b[s[0]][s[1]]=b[s[1]][s[0]]=true;
		}
		scanf("%d",&n);
		char s[110];
		scanf("%s",s);
		for (int i=0;i<n;i++){
			ans[len++]=s[i];
			if (len>=2){
				if (a[ans[len-2]][ans[len-1]]>0){
					ans[len-2]=a[ans[len-2]][ans[len-1]];
					len--;
				}
			}
			for (int j=0;j<len-1;j++)if (b[ans[j]][ans[len-1]]){
				len=0;
				break;
			}
		}
		printf("Case #%d: [",TT);
		for (int i=0;i<len-1;i++)printf("%c, ",ans[i]);
		if (len>0)printf("%c",ans[len-1]);
		printf("]\n");
		
	}
	return 0;
}
