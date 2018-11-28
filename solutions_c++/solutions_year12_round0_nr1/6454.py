
#include <cstdio>
#include <string.h>

int main() {
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);

	char toValues[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char cadena[110];
	int n;
	scanf("%d\n",&n);
	for(int i=1; i<=n; i++){
		gets(cadena);
		//int aux = strlen(cadena);
		int j=0;
		printf("Case #%d: ",i);
		while(cadena[j]!='\0'){
			if(cadena[j]!=' '){
				printf("%c",toValues[cadena[j]-'a']);
			}else{
				printf(" ");
			}
			j++;
		}
		printf("\n");
	}

	return 0;
}
