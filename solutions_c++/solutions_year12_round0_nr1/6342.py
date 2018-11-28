#include<stdio.h>
#include<string.h>

void main(){
	FILE *in,*out;;
	in=fopen("tounge.in","r");
	out=fopen("tounge.out","w");
	int x;
	char s[105];
	fscanf(in,"%d",	&x);
	fflush(stdin);
	for(int i=0;i<=x;i++)
	{
		fgets(s,sizeof(s),in);
		fflush(stdin);
		for(int a=0;a<strlen(s);a++)
		{
			switch (s[a])
			{
				case 'a' : s[a]='y';break;
				case 'b' : s[a]='h';break;
				case 'c' : s[a]='e';break;
				case 'd' : s[a]='s';break;
				case 'e' : s[a]='o';break;
				case 'f' : s[a]='c';break;
				case 'g' : s[a]='v';break;
				case 'h' : s[a]='x';break;
				case 'i' : s[a]='d';break;
				case 'j' : s[a]='u';break;
				case 'k' : s[a]='i';break;
				case 'l' : s[a]='g';break;
				case 'm' : s[a]='l';break;
				case 'n' : s[a]='b';break;
				case 'o' : s[a]='k';break;
				case 'p' : s[a]='r';break;
				case 'q' : s[a]='z';break;
				case 'r' : s[a]='t';break;
				case 's' : s[a]='n';break;
				case 't' : s[a]='w';break;
				case 'u' : s[a]='j';break;
				case 'v' : s[a]='p';break;
				case 'w' : s[a]='f';break;
				case 'x' : s[a]='m';break;
				case 'y' : s[a]='a';break;
				case 'z' : s[a]='q';break;
			}
		}
		if (i!=0) fprintf(out,"Case #%d: %s",i,s);
	}
	fclose(in);
	fclose(out);
}