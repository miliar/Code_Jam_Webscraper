#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;
char to[]={"yhesocvxduiglbkrztnwjpfmaq"};
char a[1001000];
int _,ca,i;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d\n",&_);
	for(ca=1;ca<=_;ca++)
	{
		gets(a);
		printf("Case #%d: ",ca);
		for(i=0;a[i];i++)
		if(a[i]==' ')printf(" ");
		else printf("%c",to[a[i]-'a']);
		puts("");
	}
}
