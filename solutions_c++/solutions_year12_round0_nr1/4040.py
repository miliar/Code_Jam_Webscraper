#include <iostream>
#include <cstdio>
using namespace std;

const char key[] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 
'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
int cnt,T;
char s[1000],map[27];

int main()
{
	freopen("a.in","r",stdin);freopen("a.out","w",stdout);
	
	for (int i=0;i<26;i++) map[int(key[i]-'a')]=char(i+'a');
	for (scanf("%d\n",&T);T;T--)
	{
		gets(s);//printf("%s\n",s);
		printf("Case #%d: ",++cnt);
		for (int i=0;i<strlen(s);i++) 
			if (s[i]>='a' && s[i]<='z')printf("%c",map[int(s[i]-'a')]);
			else printf("%c",s[i]);
		printf("\n");
	}
	
	return 0;
}
