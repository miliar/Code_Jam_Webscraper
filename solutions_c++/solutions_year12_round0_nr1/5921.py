#include<cstdio>
char crypt[]="yhesocvxduiglbkrztnwjpfmaq",arr[110];
int T,t;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	for(scanf("%d\n",&T),t=1; T--; t++){
		gets(arr);
		printf("Case #%d: ",t);
		for(int i=0; arr[i]; i++){
			if(arr[i]==' ') printf(" ");
			else printf("%c",crypt[arr[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}