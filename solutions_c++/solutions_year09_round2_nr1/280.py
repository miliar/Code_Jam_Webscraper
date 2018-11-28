#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MX 50000
#define ERROR(s) ({ fprintf(stderr, "%d: " s, t); exit(1); })

int N, t, l[MX], r[MX], n, A;
double p[MX];
char name[MX][20], fx[100][20];



int parse()
{
	int res=0;

	name[t][0]=0;
	l[t]=r[t]=0;
	int tx=t;	t++;
	char dummyc;
	scanf(" %c", &dummyc);
	if (dummyc!='(') ERROR("'(' expected\n");

	if (scanf(" %lf", &p[tx]))
		;
	else ERROR("Invalid p\n");

	if (scanf(" %s", name[tx]))
	{
		if (name[tx][0]==')') return strlen(name[tx])-1;

		l[tx]=t; parse();
		r[tx]=t; res=parse();
	}
	else
		ERROR("nani o kore\n");

	if (res) return res-1;

	scanf(" %c", &dummyc);
	if (dummyc!=')') ERROR("')' expected\n");	
	return 0;
}

double cute(int t, double pp)
{
	pp*=p[t];
	if (l[t])
	{
		for(int i=0; i<n; i++)
			if (!strcmp(fx[i], name[t])) return cute(l[t], pp);
		return cute(r[t], pp);
	}
	return pp;
}

int main()
{
	scanf(" %d", &N);
	for(int cs=1; cs<=N; cs++)
	{
		int dummy;
		scanf(" %d", &dummy);
		t=0;
		parse();

		printf("Case #%d:\n", cs);
		scanf(" %d", &A);

		for(int a=1; a<=A; a++)
		{
			char nx[200];
			scanf(" %s %d", nx, &n);
			for(int i=0; i<n; i++) scanf(" %s", fx[i]);
			printf("%.7f\n", cute(0, 1.0));
		}
	}
	return 0;
}
