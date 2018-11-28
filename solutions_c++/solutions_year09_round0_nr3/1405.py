#include<cstdio>

char pat[] = "welcome to code jam";

const int len = sizeof(pat)/sizeof(char) - 1;

int w[len + 5];

char s[10005];

int main(){
	int d;
	scanf("%d\n",&d);
	for(int i=1;i<=d;i++){
		w[0] = 1;
		for(int j=1;j<=len;j++) w[j] = 0;
		gets(s);
		for(int j=0;s[j];j++){
			for(int k=len;k>=1;k--){
				if(s[j] == pat[k-1]){
					w[k] = (w[k-1] + w[k]) % 10000;
				}
			}
		}
		printf("Case #%d: %04d\n",i,w[len]);
	}
}
