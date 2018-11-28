#include <stdio.h>
#include <string.h>
void main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt","w",stdout);
	int T, i, j, length;
	char s[120], g[120];
	char mapping[27] = "yhesocvxduiglbkrztnwjpfmaq";
	scanf("%d\n", &T);
	for(i=0;i<T;i++){
		//scanf("%[^\n]", &s);
		gets(s);
		length = strlen(s);
		for(j=0;j<length;j++){
			if(s[j]>='a' && s[j]<='z'){
				g[j] = mapping[s[j]-'a'];
			} else {
				g[j] = s[j];
			}
		}
		g[j] = '\0';
		printf("Case #%d: %s\n", i+1, g);
	}
}