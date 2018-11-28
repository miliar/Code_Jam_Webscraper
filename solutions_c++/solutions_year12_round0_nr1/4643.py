#include<stdio.h>  
#include<string.h>

char s[100]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char ss[1100];
int main()
{
	freopen("r.in","r",stdin);
	freopen("w.txt","w",stdout);
	int n,i,len,ii=0;

	scanf("%d",&n);

	getchar();
	while(n--)
	{
		gets(ss);
		len=strlen(ss);

		for(i=0;i<len;i++)if(ss[i]==' ')
			;
		else
			ss[i]=s[ss[i]-'a'];
		printf("Case #%d: ",++ii);
		printf("%s\n",ss);
	}
}