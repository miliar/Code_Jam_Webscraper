#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;
 
int a[300];
char x[3][60]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char y[3][60]={"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
char z[10000];
bool u[300];
int main()
{
	a['a'-'a']='y'-'a';u[0]=1;
	a['o'-'a']='e'-'a';u['o'-'a']=1;
	a['z'-'a']='q'-'a';u['z'-'a']=1;
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<strlen(x[i]);j++)
		{
			if(x[i][j]!=' ')
			{
				a[x[i][j]-'a']=y[i][j]-'a';
				u[x[i][j]-'a']=1;
			}
		}
	}
	freopen("A-small-attempt7.in","r",stdin);
	freopen("out.out","w",stdout);
	int C;
	scanf("%d",&C);
	getchar();
	for(int i=1;i<=C;i++)
	{
		gets(z);
		printf("Case #%d: ",i);
		for(int j=0;j<strlen(z);j++)
		{
			if(z[j]=='q')printf("z");
			else if(z[j]!=' ')
				printf("%c",a[z[j]-'a']+'a');
			else printf("%c",z[j]);
		}
		printf("\n");
	}
	return 0;
}
	
