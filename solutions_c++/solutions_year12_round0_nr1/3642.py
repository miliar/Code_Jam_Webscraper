#include<stdio.h>
#include<string.h>
char p[10005];
int main()
{
	int t,cas=0;
	int l,i;
	char s[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	freopen("A-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	gets(p);
	while(t--)
	{
		cas++;
		gets(p);
		l=strlen(p);
		for(i=0;i<l;++i)
		{
			if(p[i]>='a'&&p[i]<='z')
				p[i]=s[p[i]-'a'];
		}
		printf("Case #%d: %s\n",cas,p);
	}
}