#include <cstdio>
#include <algorithm>
using namespace std;

int n,m,l,f,AC,e[20][30];
char s[500],w[5005][20];

int main(){
	scanf("%d%d%d",&l,&n,&m);
		for (int i=1;i<=n;i++) scanf("%s",w[i]);
		for (int i=1;i<=m;i++){
		scanf("%s",s);
		memset(e,0,sizeof(e));
			for (int k=0,x=0;k<l;k++){
				if (s[x]=='('){
				x++;
					while (s[x]!=')') e[k][s[x++]-'a']=1;
				x++;
				}
				else e[k][s[x++]-'a']=1;
			}
		AC=0;
			for (int k=1;k<=n;k++){
			f=1;
				for (int j=0;j<l&&e;j++)
					if (!e[j][w[k][j]-'a']) f=0;
			AC+=f;
			}
		printf("Case #%d: %d\n",i,AC);
		}
	return 0;
}
