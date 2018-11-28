#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;

const char q[]="yhesocvxduiglbkrztnwjpfmaq";

char s[1024];
int T,l;

int main()
{
	scanf("%d\n",&T);
	for (int test=1;test<=T;++test)
	{
		gets(s); int l=strlen(s);
		printf("Case #%d: ",test);
		for (int i=0;i<l;++i)
			if (s[i]==' ') printf(" ");
			else printf("%c",q[s[i]-'a']);
		cout << endl;
	}
	return 0;
}
