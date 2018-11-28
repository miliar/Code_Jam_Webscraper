#include <cstdio>
#include <cstring>

char dy[26]=
{'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
//a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t  
char dy2[26];

int n;
char gao[1005], ch;

int main(){
	scanf("%d",&n);
	scanf("%c",&ch);
	for(int i = 0; i < 26; ++i)
		dy2[dy[i] - 'a'] = 'a' + i;
	for(int i = 1; i <= n; ++i){
		gets(gao);
		printf("Case #%d: ",i);
		int len = strlen(gao);
		for(int j = 0; j < len; ++j)
			if(gao[j] == ' ')printf(" ");
			else printf("%c",dy2[gao[j] - 'a']);
		puts("");
	}
}
