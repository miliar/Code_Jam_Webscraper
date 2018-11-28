#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
int main()
{
	char tab[2000];
	int a;
	scanf("%d\n",&a);
	int i;
	for (i=0;i<a;i++)
	{
		gets(tab);
		
		int j=0;
		while (tab[j]!=0)
		{
			if(tab[j]=='a')
			tab[j]='y';
			else if (tab[j]=='b')
			tab[j]='h';
			else if (tab[j]=='c')
			tab[j]='e';
			else if (tab[j]=='o')
			tab[j]='k';
			else if (tab[j]=='d')
			tab[j]='s';
			else if (tab[j]=='e')
			tab[j]='o';
			else if (tab[j]=='f')
			tab[j]='c';
			else if (tab[j]=='g')
			tab[j]='v';
			else if (tab[j]=='h')
			tab[j]='x';
			else if (tab[j]=='i')
			tab[j]='d';
			else if (tab[j]=='j')
			tab[j]='u';
			else if (tab[j]=='k')
			tab[j]='i';
			else if (tab[j]=='l')
			tab[j]='g';
			else if (tab[j]=='m')
			tab[j]='l';
			else if (tab[j]=='n')
			tab[j]='b';
			else if (tab[j]=='p')
			tab[j]='r';
			else if (tab[j]=='q')
			tab[j]='z';
			else if (tab[j]=='r')
			tab[j]='t';
			else if (tab[j]=='s')
			tab[j]='n';
			else if (tab[j]=='t')
			tab[j]='w';
			else if (tab[j]=='u')
			tab[j]='j';
			else if (tab[j]=='v')
			tab[j]='p';
			else if (tab[j]=='w')
			tab[j]='f';
			else if (tab[j]=='x')
			tab[j]='m';
			else if (tab[j]=='y')
			tab[j]='a';
			else if (tab[j]=='z')
			tab[j]='q';
			
			
			
			
			j++;
		}
		printf("Case #%d: ",i+1);
		cout<<tab<<endl;
		
		
		
	}
	
	return 0;





}
