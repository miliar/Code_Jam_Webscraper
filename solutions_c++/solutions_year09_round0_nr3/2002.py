#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char wtc[] = "welcome to code jam";
const int len = 19;

int let[19];

unsigned long long num;

char *loc(char *s, int l)
{
	char a = wtc[l];
	while(*s && *s != a) s++;
    return s;
}

void cuenta(char *s, int l)
{
	while(*s != 0)
	{
		s = loc(s, l);
		if(*s == 0) 
		{
			let[l] = 0;
			return;
		}

		char a = wtc[l];
		char b = wtc[l + 1];
		char *t = s;
		int seg = 0;
		for(;*t; t++)
		{
			if(*t == a)
			{
        		seg++;
			}
			else if(*t == b)
			{
				break;
			}
		}

		let[l] = seg;

		if(l < len - 1)
		{
			cuenta(t, l + 1);
		}
		else
		{
			unsigned long long tmpnum = 1;
			for(int m = 0; m < len; m++) tmpnum *= let[m];
			num += tmpnum;		
		} 
		s = t;
	}
}

void main(int argc, char **args)
{
	if(argc < 2) return;

    char *archEntrada = new char[strlen(args[1]) + 4];
    char *archSalida = new char[strlen(args[1]) + 5];
    strcpy(archEntrada, args[1]);
    strcpy(archEntrada + strlen(args[1]), ".in");
	strcpy(archSalida, args[1]);
    strcpy(archSalida + strlen(args[1]), ".out");

    FILE *fin = fopen(archEntrada, "r");
	FILE *fout = fopen(archSalida, "w");

	int numCasos;
	fscanf(fin, "%d", &numCasos);

    char *txt;
    char txtAux[501];

	fgets(txtAux, 501, fin);

    int fint, sz;

	for(int caso = 1; caso <= numCasos; caso++)
	{
    	memset(txtAux, 0, 501);
		fgets(txtAux, 501, fin);
		txt = txtAux;
        while(*txt && (*txt != 'w')) txt++;
        for(fint = strlen(txt) - 1; (fint) && (*(txt + fint) != 'm'); fint--);

        txt[fint + 1] = 0;

        sz = strlen(txt);
        if(sz < len)
        {
	        fprintf(fout, "Case #%d: 0000\n", caso);
            continue;
        }

		num = 0;

        cuenta(txt, 0);

		fprintf(fout, "Case #%d: %04I64u\n", caso, (num % 10000));
	}

	fclose(fin);
	fclose(fout);

    delete [] archEntrada;
    delete [] archSalida;
}