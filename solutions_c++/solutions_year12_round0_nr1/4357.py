#include<stdio.h>
#include<string.h>

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("a_codejam.out","w",stdout);

	int cas,cc,i;
	int len;
	char str[200];
	char set[500];

	//precalculation using program
	set['a']='y';
	set['b']='h';
	set['c']='e';
	set['d']='s';
	set['e']='o';
	set['f']='c';
	set['g']='v';
	set['h']='x';
	set['i']='d';
	set['j']='u';
	set['k']='i';
	set['l']='g';
	set['m']='l';
	set['n']='b';
	set['o']='k';
	set['p']='r';
	set['q']='z';
	set['r']='t';
	set['s']='n';
	set['t']='w';
	set['u']='j';
	set['v']='p';
	set['w']='f';
	set['x']='m';
	set['y']='a';
	set['z']='q';
	set['A']='Y';
	set['B']='H';
	set['C']='E';
	set['D']='S';
	set['E']='O';
	set['F']='C';
	set['G']='V';
	set['H']='X';
	set['I']='D';
	set['J']='U';
	set['K']='I';
	set['L']='G';
	set['M']='L';
	set['N']='B';
	set['O']='K';
	set['P']='R';
	set['Q']='Z';
	set['R']='T';
	set['S']='N';
	set['T']='W';
	set['U']='J';
	set['V']='P';
	set['W']='F';
	set['X']='M';
	set['Y']='A';
	set['Z']='Q';

	//processing
	scanf("%d",&cas);

	//dummy input
	gets(str);

	for(cc=1;cc<=cas;cc++)
	{
		gets(str);

		len=strlen(str);

		printf("Case #%d: ",cc);
		for(i=0;i<len;i++)
		{
			if(str[i]==' ')
			{
				printf(" ");
			}
			else
			{
				printf("%c",set[str[i]]);
			}

		}
		printf("\n");
	}


	return 0;
}
