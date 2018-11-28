#include <stdio.h>
#include <string.h>
int a[5000][20];

int main(){
	int T;
	scanf("%d\n", &T);
	char c[]="welcome to code jam";
	int len=strlen(c);
	for(int TT=1;TT<=T;TT++){
		char d[5100];
		gets(d);
		int l=strlen(d);
		memset(a,0,sizeof(a));
		a[0][0]=1;
		if(d[0] == c[0]){
			a[0][1]=1;
		}
		for(int i=1;i<l;i++){
			a[i][0]=1;
			for(int j=1;j<=len;j++){
				a[i][j]=a[i-1][j];
			}
			for(int j=0;j<len;j++){
				if(c[j] == d[i]){
					a[i][j+1]+=a[i-1][j];
					if(a[i][j+1]>10000)
						a[i][j+1]-=10000;
				}
			}
		}
		printf("Case #%d: %.4d\n",TT,a[l-1][len]);
	}
}