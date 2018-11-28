#include<cstdio>
#include<cstring>
#define L 1000

using namespace std;

char p[20]="welcome to code jam",s[L];
int n,i,tot,opt[L],T,j,tmp,I;

int main(){
	scanf("%d",&T);gets(s);
	while (T--){
		gets(s+1);
		n=strlen(s+1);
		opt[0]=1;
		for (i=0;i<19;++i){
			tot=0;
			for (j=0;j<=n;++j){
				if (s[j]==p[i]) tmp=tot;
				else tmp=0;
				tot+=opt[j];
				tot%=10000;
				opt[j]=tmp;
			}
		}
		tot=0;
		for (j=0;j<=n;++j){
			tot+=opt[j];
			tot%=10000;
		}
		printf("Case #%d: %04d\n",++I,tot);
	}
}
