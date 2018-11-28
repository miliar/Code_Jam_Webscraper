#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<stdlib.h>
#include<fstream.h>
void main()
{
	int num,i=0,l[32],j=0;
	char str[32][102];
	clrscr();
	FILE *fi=fopen("inp.txt","r");
	while(!feof(fi))
	{
		fgets(str[i],102,fi);
		i++;
	}
	fclose(fi);
	num=atoi(str[0]);
	for(i=1;i<=num;i++)
	{
		l[i]=strlen(str[i]);
	}
	for(i=1;i<=num;i++)
	{
		for(j=0;j<l[i];j++)
		{
			switch(str[i][j])
			{
				case 'a': str[i][j]='y';
					  break;
				case 'b': str[i][j]='h';
					  break;
				case 'c': str[i][j]='e';
					  break;
				case 'd': str[i][j]='s';
					  break;
				case 'e': str[i][j]='o';
					  break;
				case 'f': str[i][j]='c';
					  break;
				case 'g': str[i][j]='v';
					  break;
				case 'h': str[i][j]='x';
					  break;
				case 'i': str[i][j]='d';
					  break;
				case 'j': str[i][j]='u';
					  break;
				case 'k': str[i][j]='i';
					  break;
				case 'l': str[i][j]='g';
					  break;
				case 'm': str[i][j]='l';
					  break;
				case 'n': str[i][j]='b';
					  break;
				case 'o': str[i][j]='k';
					  break;
				case 'p': str[i][j]='r';
					  break;
				case 'q': str[i][j]='z';
					  break;
				case 'r': str[i][j]='t';
					  break;
				case 's': str[i][j]='n';
					  break;
				case 't': str[i][j]='w';
					  break;
				case 'u': str[i][j]='j';
					  break;
				case 'v': str[i][j]='p';
					  break;
				case 'w': str[i][j]='f';
					  break;
				case 'x': str[i][j]='m';
					  break;
				case 'y': str[i][j]='a';
					  break;
				case 'z': str[i][j]='q';
					  break;
				case ' ':
					  break;
				//default:printf("INVALID ENTRY");
			}
		}
	}

	FILE *fo=fopen("output.txt","w");
	for(i=1;i<=num;i++)
	fprintf(fo,"%s%d%s %s","Case #",i,":",str[i]);
	fclose(fo);

getch();
}

