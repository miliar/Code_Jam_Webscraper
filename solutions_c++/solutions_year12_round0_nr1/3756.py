#include<stdio.h>
#include<string.h>
#include<math.h>
char s[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	freopen("ininin.in","r",stdin);
    freopen("small.txt","w",stdout);
	int t,k=1;
	scanf("%d",&t);
	getchar();
	while(t--)
	{
		char c[200];
		int i;
		int len;
		gets(c);
		len=strlen(c);
		printf("Case #%d: ",k++);
		for(i=0;i<len;i++)
		{
			if(c[i]>='a'&&c[i]<='z') printf("%c",s[c[i]-'a']);
			else if(c[i]==' ') printf("%c",c[i]);
		}
		printf("\n");
	}
	return 0;
}
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
 */
