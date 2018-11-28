#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<iostream>

using namespace std;
int main()
{
    FILE* f1;
    f1=fopen("opt.txt","w");
	int t,i,n=0;
	char map[26],tmp;
	char guglrse[200];
	char eng[200][200];
	int size=0;

	map[(int)'a'-97]='y';
	map[(int)'b'-97]='h';
	map[(int)'c'-97]='e';
	map[(int)'d'-97]='s';
	map[(int)'e'-97]='o';
	map[(int)'f'-97]='c';
	map[(int)'g'-97]='v';
	map[(int)'h'-97]='x';
	map[(int)'i'-97]='d';
	map[(int)'j'-97]='u';
	map[(int)'k'-97]='i';
	map[(int)'l'-97]='g';
	map[(int)'m'-97]='l';
	map[(int)'n'-97]='b';
	map[(int)'o'-97]='k';
	map[(int)'p'-97]='r';
	map[(int)'q'-97]='z';
	map[(int)'r'-97]='t';
	map[(int)'s'-97]='n';
	map[(int)'t'-97]='w';
	map[(int)'u'-97]='j';
	map[(int)'v'-97]='p';
	map[(int)'w'-97]='f';
	map[(int)'x'-97]='m';
	map[(int)'y'-97]='a';
	map[(int)'z'-97]='q';


	scanf("%d",&t);
	scanf("%c",&tmp);

	n=t;
	while(t--)
	{

		gets(guglrse);

		size=strlen(guglrse);

		i=0;
		while(i<size)
		{
			if(guglrse[i]!=' ')
				{
				    eng[n-t-1][i]=map[(int)guglrse[i]-97];
				}
			else
				{
					eng[n-t-1][i]=' ';
				}
			i++;
		}
		eng[n-t-1][i]='\n';

	}
	t=n;
	while(t--)
		fprintf(f1,"Case #%d: %s",n-t,eng[n-t-1]);
  fclose(f1);
  cin.sync();
  cin.get();

  return 0;

}









