#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
//	freopen("A0.in","r",stdin);
//	freopen("A0.txt","w",stdout);
	char a[200]="";
	char p[50]={};

	char b[10][200]={};
	strcpy(b[0],"ejp mysljylc kd kxveddknmc re jsicpdrysi");
	strcpy(b[1],"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	strcpy(b[2],"de kr kd eoya kw aej tysr re ujdr lkgc jv");
	char c[10][200]={};
	strcpy(c[0],"our language is impossible to understand");
	strcpy(c[1],"there are twenty six factorial possibilities");
	strcpy(c[2],"so it is okay if you want to just give up");
	int k[10];
	for(int i=0;i<3;i++)
	{
		k[i]=strlen(b[i]);
	}
			p['a'-'a']='y';
			p['o'-'a']='e';
			p['z'-'a']='q';
			p['q'-'a']='z';

	for(int i=0;i<3;i++)
	{
		for(int j=0;j<k[i];j++)
		{
			if(b[i][j]==' ')
				continue;
			p[b[i][j]-'a']=c[i][j];
		}
	}
	int T;
	scanf("%d\n",&T);
	for(int i=0;i<T;i++)
	{
		gets(a);
		int kol=strlen(a);
		for(int i=0;i<kol;i++)
		{
			if(a[i]==' ')
				continue;
			a[i]=p[a[i]-'a'];
		}
		printf("Case #%d: ",i+1);
		puts(a);
	}
	return 0;
}