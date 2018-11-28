// Codejam2012.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fpi;
	FILE *fpo;
	int nT;
	char sG[30][101];
	char output[30][101];
	memset(output, 0, 30*101*sizeof(char));
	int i,j;
	char dic[25];
	dic['a'-'a']='y';
	dic['b'-'a']='h';
	dic['c'-'a']='e';
	dic['d'-'a']='s';
	dic['e'-'a']='o';
	dic['f'-'a']='c';
	dic['g'-'a']='v';
	dic['h'-'a']='x';
	dic['i'-'a']='d';
	dic['j'-'a']='u';
	dic['k'-'a']='i';
	dic['l'-'a']='g';
	dic['m'-'a']='l';
	dic['n'-'a']='b';
	dic['o'-'a']='k';
	dic['p'-'a']='r';
	dic['q'-'a']='z';
	dic['r'-'a']='t';
	dic['s'-'a']='n';
	dic['t'-'a']='w';
	dic['u'-'a']='j';
	dic['v'-'a']='p';
	dic['w'-'a']='f';
	dic['x'-'a']='m';
	dic['y'-'a']='a';
	dic['z'-'a']='q';

	fpi = fopen("A-small-attempt0.in","r");
	if (!fpi) exit(0);

	fscanf(fpi, "%d\n", &nT);
	i = 0;
	while (i < nT)
	{
		j = 0;
		fscanf(fpi, "%c", &sG[i][j]);
		while ((sG[i][j] >= 'a') && (sG[i][j] <= 'z') || (sG[i][j] == ' '))
		{
			if (sG[i][j] == ' ')
			{
				output[i][j] = sG[i][j];
			}
			else
			{
				output[i][j] = dic[sG[i][j]-'a'];
			}
			j = j+1;
			fscanf(fpi, "%c", &sG[i][j]);
		}
		sG[i][j] = 0;
		output[i][j] = 0;
		i = i + 1;
	}
	fclose(fpi);

	fpo = fopen("A-small-attempt0.out","w");
	if (!fpo) exit(0);
	
	for (i=0; i<nT; i++)
	{
		fprintf(fpo, "Case #%d: ", i+1);
		fprintf(fpo, "%s\n", output[i]);
	}

	fclose(fpo);	
	return 0;
}

