#include <stdio.h>
#include <string.h>

char b[]="welcome to code jam\n";
char s[512];
int c[24][512];

int main(){
	int N,cas;
	int L,R;
	int i,j,t;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&N);
	getchar();
	for (cas=1;cas<=N;cas++){
		gets(s);
		L=strlen(s);
		if (s[L-1]!='\n'){
			s[L++]='\n';
		}
		R=strlen(b);
		memset(c,0,sizeof(c));
		c[0][0]=1;
		for (i=0;i<R;i++){
			t=0;
			for (j=0;j<L;j++){
				t=(t+c[i][j])%10000;
				if (b[i]==s[j]){
					c[i+1][j+1]=t;
//					printf("c[%d][%d]=%d\n",i+1,j+1,t);
				}
			}
		}
		t=0;
		printf("Case #%d: %04d\n",cas,c[R][L]);
	}
	return 0;
}

