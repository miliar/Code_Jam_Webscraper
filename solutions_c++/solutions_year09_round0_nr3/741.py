#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef int *pint;

int solve(char *line)
{
	int nWELCOME_TO_CODE_JAM = 0;
	int nELCOME_TO_CODE_JAM = 0;
	int nLCOME_TO_CODE_JAM = 0;
	int nCOME_TO_CODE_JAM = 0;
	int nOME_TO_CODE_JAM = 0;
	int nME_TO_CODE_JAM = 0;
	int nE_TO_CODE_JAM = 0;
	int n_TO_CODE_JAM = 0;
	int nTO_CODE_JAM = 0;
	int nO_CODE_JAM = 0;
	int n_CODE_JAM = 0;
	int nCODE_JAM = 0;
	int nODE_JAM = 0;
	int nDE_JAM = 0;
	int nE_JAM = 0;
	int n_JAM = 0;
	int nJAM = 0;
	int nAM = 0;
	int nM = 0;
	int i;
	size_t l = strlen(line);
	for (i=(int)l-1;i>=0;--i)
	{
		switch(line[i])
		{
		case 'w':
			nWELCOME_TO_CODE_JAM += nELCOME_TO_CODE_JAM;
			nWELCOME_TO_CODE_JAM %= 10000;
			break;
		case 'e':
			nELCOME_TO_CODE_JAM += nLCOME_TO_CODE_JAM;
			nELCOME_TO_CODE_JAM %= 10000;
			nE_TO_CODE_JAM += n_TO_CODE_JAM;
			nE_TO_CODE_JAM %= 10000;
			nE_JAM += n_JAM;
			nE_JAM %= 10000;
			break;
		case 'l':
			nLCOME_TO_CODE_JAM += nCOME_TO_CODE_JAM;
			nLCOME_TO_CODE_JAM %= 10000;
			break;
		case 'c':
			nCOME_TO_CODE_JAM += nOME_TO_CODE_JAM;
			nCOME_TO_CODE_JAM %= 10000;
			nCODE_JAM += nODE_JAM;
			nCODE_JAM %= 10000;
			break;
		case 'o':
			nOME_TO_CODE_JAM += nME_TO_CODE_JAM;
			nOME_TO_CODE_JAM %= 10000;
			nO_CODE_JAM += n_CODE_JAM;
			nO_CODE_JAM %= 10000;
			nODE_JAM += nDE_JAM;
			nODE_JAM %= 10000;
			break;
		case 'm':
			nME_TO_CODE_JAM += nE_TO_CODE_JAM;
			nME_TO_CODE_JAM %= 10000;
			++nM;
			nM %= 10000;
			break;
		case ' ':
			n_TO_CODE_JAM += nTO_CODE_JAM;
			n_TO_CODE_JAM %= 10000;
			n_CODE_JAM += nCODE_JAM;
			n_CODE_JAM %= 10000;
			n_JAM += nJAM;
			n_JAM %= 10000;
			break;
		case 't':
			nTO_CODE_JAM += nO_CODE_JAM;
			nTO_CODE_JAM %= 10000;
			break;
		case 'd':
			nDE_JAM += nE_JAM;
			nDE_JAM %= 10000;
			break;
		case 'j':
			nJAM += nAM;
			nJAM %= 10000;
			break;
		case 'a':
			nAM += nM;
			nAM %= 10000;
			break;
		default:
			break;
		}
	}
	return nWELCOME_TO_CODE_JAM;
}

void main()
{
	FILE *fin,*fout;
	int n;
	int i,j;
	char c = 0;
	fopen_s(&fin, "C-large.in", "rt");
	fopen_s(&fout, "C-large.out", "wb");

	fscanf_s(fin,"%d\n",&n);
	for (i=0;i<n;++i)
	{
		char line[1024];
		c = fgetc(fin);
		j=0;
		while (c!=0x0D && c!=0x0A && !feof(fin))
		{
			switch(c)
			{
			case 'w':
			case 'e':
			case 'l':
			case 'c':
			case 'o':
			case 'm':
			case ' ':
			case 't':
			case 'd':
			case 'j':
			case 'a':
				{
					if (c=='w' || j>0)
					line[j++] = c;	
				}
				break;
			default:
				break;
			}
			c = fgetc(fin);
		}
		fscanf_s(fin, "\n");
		line[j] = 0;
		int nSolution = 0;
		if (j>0)
			nSolution = solve(line);
		fprintf(fout, "Case #%d: %04d\n", i+1, nSolution);
	}

	fclose(fin);
	fclose(fout);
}