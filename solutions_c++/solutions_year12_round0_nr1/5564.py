#include<stdio.h>
int main()
{
	char st[500],buf;
	int i,t,j;
	scanf("%d",&t);
	scanf("%c",&buf);
	for(i=1;i<=t;i++)
	{   
		gets(st);
		printf("Case #%d:",i);
		for(j=0;st[j]!='\0';j++)
		{  if(st[j]==' ')
		    { printf(" "); }
		    else if(st[j]=='a')
		    printf("y");
		     else if(st[j]=='b')
		    printf("h");
		     else if(st[j]=='c')
		    printf("e");
		     else if(st[j]=='d')
		    printf("s");
		     else if(st[j]=='e')
		    printf("o");
		     else if(st[j]=='f')
		    printf("c");
		     else if(st[j]=='g')
		    printf("v");
		     else if(st[j]=='h')
		    printf("x");
		     else if(st[j]=='i')
		    printf("d");
		     else if(st[j]=='j')
		    printf("u");
		     else if(st[j]=='k')
		    printf("i");
		     else if(st[j]=='l')
		    printf("g");
		     else if(st[j]=='m')
		    printf("l");
		     else if(st[j]=='n')
		    printf("b");
		     else if(st[j]=='o')
		    printf("k");
		     else if(st[j]=='p')
		    printf("r");
		     else if(st[j]=='q')
		    printf("z");
		     else if(st[j]=='r')
		    printf("t");
		     else if(st[j]=='s')
		    printf("n");
		     else if(st[j]=='t')
		    printf("w");
		     else if(st[j]=='u')
		    printf("j");
		     else if(st[j]=='v')
		    printf("p");
		     else if(st[j]=='w')
		    printf("f");
		     else if(st[j]=='x')
		    printf("m");
		     else if(st[j]=='y')
		    printf("a");
		     else 
		    printf("q");
		}
		printf("\n");
		
	}
	return 0;
}
