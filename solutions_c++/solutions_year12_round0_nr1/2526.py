#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

char mp[100]="yhesocvxduiglbkrztnwjpfmaq";
char s[300];
int main()
{
	freopen("A-small.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	gets(s);
	for (int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		gets(s);
		int len=strlen(s);
		for (int i=0;i<len;i++)
		{
			if (s[i]>='a' && s[i]<='z') putchar(mp[s[i]-'a']);
			else putchar(' ');
		}
		puts("");
	}
}
