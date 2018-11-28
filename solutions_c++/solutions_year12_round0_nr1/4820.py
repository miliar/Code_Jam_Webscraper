#include <cstdio>
using namespace std;

char s[1100];
char p[27] = "yhesocvxduiglbkrztnwjpfmaq";
//char pp[27] ="abcdefghijklmnopqrstuvwxyz";

void mod ()
{
	for (int i = 0; s[i]; ++i)
	{
		if ('a' <= s[i] && s[i] <= 'z')
			s[i] = p[s[i] - 'a']; 
	}
}
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	int n;
	scanf ("%d\n", &n);
	for (int i = 1; i <= n; ++i)
	{
		gets(s);
		mod();
		printf ("Case #%d: %s\n", i, s);
	}
}
