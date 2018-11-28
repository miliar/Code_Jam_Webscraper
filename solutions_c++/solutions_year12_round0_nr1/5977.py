#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char txt[]="yhesocvxduiglbkrztnwjpfmaq";
char s[200];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int i,n,t=1,len;
	scanf("%d",&n);
	getchar();
	while(n--)
	{
		
		gets(s);
		printf("Case #%d: ",t++);
		len=strlen(s);
		for(i=0;i<len;++i)
			if(s[i]!=' ')
			{
				s[i]=txt[s[i]-'a'];
			}
		puts(s);
	}	
	return 0;
}