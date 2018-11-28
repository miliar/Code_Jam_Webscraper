#include<iostream>
#include<cstdio>

using namespace std;

char r[] = "yhesocvxduiglbkrztnwjpfmaq";

char s[101];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T;
	cin>> T;
	getchar();
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		gets(s);
		for(int i=0;s[i];i++)
		{
			putchar(s[i]==32?' ':r[s[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}
