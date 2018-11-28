#include <cstdio>
#include <cstdlib>
#include <cstring>

int t,len,i,id;
char st[200];

int main()
{
//	freopen("A-small-attempt2.in","r",stdin);
//	freopen("A-small-attempt2.out","w",stdout);
	scanf("%d\n",&t);
	for (id=1;id<=t;id++)
	{
		gets(st);
		printf("Case #%d: ",id);
		len=strlen(st);
		for (i=0;i<len;i++)
		{
			if (st[i]=='a')printf("y");
			else if (st[i]=='b')printf("h");
			else if (st[i]=='c')printf("e");
			else if (st[i]=='d')printf("s");
			else if (st[i]=='e')printf("o");
			else if (st[i]=='f')printf("c");
			else if (st[i]=='g')printf("v");
			else if (st[i]=='h')printf("x");
			else if (st[i]=='i')printf("d");
			else if (st[i]=='j')printf("u");
			else if (st[i]=='k')printf("i");
			else if (st[i]=='l')printf("g");
			else if (st[i]=='m')printf("l");
			else if (st[i]=='n')printf("b");
			else if (st[i]=='o')printf("k");
			else if (st[i]=='p')printf("r");
			else if (st[i]=='q')printf("z");//
			else if (st[i]=='r')printf("t");
			else if (st[i]=='s')printf("n");
			else if (st[i]=='t')printf("w");
			else if (st[i]=='u')printf("j");
			else if (st[i]=='v')printf("p");
			else if (st[i]=='w')printf("f");
			else if (st[i]=='x')printf("m");
			else if (st[i]=='y')printf("a");
			else if (st[i]=='z')printf("q");//bz
			else printf("%c",st[i]);
		}
		printf("\n");
	}
	return 0;
}

/*
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/