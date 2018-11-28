#include <stdio.h>
#include <string.h>

int L,D,N;

char s[5000][16];
char base[5000];

char e[16][26];

void setbase(){
	int i,k,l;
	l=strlen(base);
	for (i=0,k=0;k<L;k++){
		if (base[i]=='('){
			i++;
			while (base[i]!=')'){
				e[k][base[i]-'a']=1;
				i++;
			}
			i++;
		}else{
			e[k][base[i]-'a']=1;
			i++;
		}
	}
}

int main(){
	int i,k,cas,ret;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for (i=0;i<D;i++) scanf("%s",s[i]);
	for (cas=1;cas<=N;cas++){
		memset(e,0,sizeof(e));
		scanf("%s",base);
		setbase();
		ret=0;
		for (i=0;i<D;i++){
			for (k=0;k<L;k++) if (!e[k][s[i][k]-'a']) break;
			if (k==L) ret++;
		}
		printf("Case #%d: %d\n",cas,ret);
	}
	return 0;
}

