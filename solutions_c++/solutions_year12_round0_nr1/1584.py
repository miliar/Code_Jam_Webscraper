#include<stdio.h>
#include<string.h>
char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char cod[101];
int main(){
	int t,i,j,len;
	freopen("A-small-attempt3.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	getchar();
	for(i=1;i<=t;i++){
		gets(cod);
		len=strlen(cod);
		for(j=0;j<len;j++){
			if(cod[j]>='a'&&cod[j]<='z')
				cod[j]=map[cod[j]-'a'];
		}
		printf("Case #%d: ",i);
		for(j=0;j<len;j++)
			printf("%c",cod[j]);
		printf("\n");
	}
	return 0;
}		