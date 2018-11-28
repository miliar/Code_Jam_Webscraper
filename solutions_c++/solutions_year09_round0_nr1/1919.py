#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fin, *fout;
int l, d, n;

typedef struct litera
{
	char lit;
	int nr;
	litera *urm[26];
}litera;

litera *init(char lit)
{
	litera *p;
	p = (litera *)calloc(sizeof(litera),1);
	p->lit = lit;
    return p;
}

void insereaza(litera *p, char *cuv, int i)
{
	if(p->urm[cuv[i]-'a'] == NULL)
		p->urm[cuv[i]-'a'] = init(cuv[i]);
	if(i<l-1)  insereaza(p->urm[cuv[i]-'a'], cuv, i+1);
	else p->nr == 1;
	p->nr++;
}

int cauta(litera *p, char *cuv, int i)
{
	int j, nr=0, k;
    if(p==NULL) return 0;
    if(i>l) return 1;
	if(cuv[0]=='(')
	{
		j=1;
		while(cuv[j]!=')') j++;
		k = j;
		for(j=1; j<k; j++)
			nr += cauta(p->urm[cuv[j]-'a'],cuv+k+1,i+1);
		return nr;
	}
	return cauta(p->urm[cuv[0]-'a'], cuv+1, i+1);
}
	
	
int main()
{
	int i;
    char cuv[500];
	litera *r, *p;
	r = init(0);
	fin = fopen("date.in", "rt");
    fout = fopen("date.out", "wt");
	fscanf(fin, "%i %i %i", &l, &d, &n);
	for(i=1; i<=d; i++)
	{
		fscanf(fin, "%s", cuv);
		insereaza(r, cuv, 0);
	}
	for(i=1; i<=n; i++)
	{
		fscanf(fin, "%s", cuv);
		fprintf(fout, "Case #%i: %i\n", i, cauta(r,cuv,1));
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
