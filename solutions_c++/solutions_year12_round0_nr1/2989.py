
#include <cstdio>
#include <cstring>
using	namespace	std;
int map[26] = {24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
char s[100];
int main(){
	freopen("a1.in", "r", stdin);
    freopen("a1.out", "w", stdout);
	int t;
	scanf("%d\n",&t);

	for(int i =1;i <=t;i ++){
		gets(s);
		printf("Case #%d: ",i);
		for(int i = 0;i < strlen(s);i ++){
			if(s[i]==' ')
				printf(" ");
			else{
				char c = 'a' + map[s[i]-'a'];
				printf("%c",c);
			}
		}
		printf("\n");
	}
	return 0;
}