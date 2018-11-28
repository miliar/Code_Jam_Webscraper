#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);
	char s[]="yhesocvxduiglbkrztnwjpfmaq";
	int t;
	char str[100010];
	gets(str);
	sscanf(str,"%d",&t);
	for(int k = 1; k <= t; k++) {
		gets(str);
		printf("Case #%d: ",k);
		for(int i=0;str[i];i++)
			if(str[i] == ' ' ) printf(" ");
			else printf("%c",s[str[i]-'a']);
		printf("\n");
	}
	return 0;
}
