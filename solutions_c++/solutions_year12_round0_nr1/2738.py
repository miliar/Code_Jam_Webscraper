#include<cstdio>
#include<cstring>

char s[] = "yhesocvxduiglbkrztnwjpfmaq";
char c[200];

int main(){
//	freopen("in.txt" , "r" , stdin);
//	freopen("out.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	gets(c);
	for(int ii = 1;ii <= t;ii++){
		gets(c);
		int n = strlen(c);
		for(int i = 0;i < n;i++){
			if(c[i] != ' ')
				c[i] = s[c[i] - 'a'];
		}
		printf("Case #%d: %s\n" , ii, c);
	}
	return 0;
}