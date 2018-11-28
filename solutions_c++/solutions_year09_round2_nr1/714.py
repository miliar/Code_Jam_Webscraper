#include <stdio.h>
#include <string.h>

#include <algorithm>
#include <set>
using namespace std;

#define		DEBUG	1

typedef struct node
{
	char	name[20];
	double	wt;
	int lef, rig;
}Node;


int		CAS = 0, T;
FILE	*in, *out;

int		L;
char	line[10000];
int		pos;
int		A;
int		ca;
char	anl[20];
char	attr[100][20];

int		cnt;
Node	nod[1200];

void	makeTree(int cnode)
{	
	int		cc = 0;
	while (1)
	{
		if (line[pos] == '(')
		{
			pos++;
			nod[cnt].lef = -1;
			nod[cnt].rig = -1;
			nod[cnt].name[0] = 0;

			if (cc == 0)
			{
				nod[cnode].lef = cnt;
				cc++;
			}
			else
				nod[cnode].rig = cnt;
			makeTree(cnt++);
		}
		else if('0' <= line[pos] && line[pos] <= '9')
		{
			bool	before = true;
			double	wt =  0.0, base = 0.1;
			while ('0' <= line[pos] && line[pos] <= '9' || line[pos] == '.')
			{
				if (line[pos] == '.')	
					before = false;
				else
				{
					wt = before ? wt * 10.0 + line[pos]-'0' : wt + base * (line[pos]-'0');
					if (before == false)	base /= 10.0;	
				}
				pos++;
			}
			nod[cnode].wt = wt;
		}
		else if ('a' <= line[pos] && line[pos] <= 'z')
		{
			char	name[20];
			int		t = 0;
			memset(name, 0, sizeof(name));
			while ('a' <= line[pos] && line[pos] <= 'z')
			{
				name[t++] = line[pos++];
			}
			strcpy(nod[cnode].name, name);
		}
		else if(line[pos] == ')')
		{
			pos++;
			return ;
		}
		else
			pos++;
	}
}

bool	find(int pos)
{
	int		i, j;

	for (i=0; i<ca; i++)
	{
		if (strcmp(nod[pos].name, attr[i]) == 0)	return true;
	}
	return false;
}


double	Cal()
{
	int		att = 0;
	double	rnt = 1.0;

	while (1)
	{
		rnt *= nod[att].wt;

		if (nod[att].lef == -1 && nod[att].rig == -1)	break;
		if(find(att))
			att = nod[att].lef;
		else
			att = nod[att].rig;
	}

	return rnt;
}

int main()
{
	int		i, j, k;
	int		STATE; // 0 - before ., and 1 for after
	char	temp[100];

	in = (DEBUG) ? stdin : fopen("D:/round1/2.in", "rt");
	out =(DEBUG) ? stdout : fopen("D:/round1/2.out", "wt");

	fscanf(in, "%d", &T);
	
	while (T--)
	{
		fscanf(in, "%d", &L);	gets(temp);
		
		STATE = 0;
		memset(line, 0, sizeof(line));
		for (i=0; i<L; i++)
		{
			gets(temp);
			strcat(line, temp);
		}
		//printf("%s\n", line);
		
		pos = cnt = 0;

		for (; line[pos]!='('; pos++);

		nod[cnt].lef = -1;
		nod[cnt].rig = -1;
		nod[cnt].name[0] = 0;
		pos++;
		makeTree(cnt++);
		
		fprintf(out, "Case #%d:\n", ++CAS );
		fscanf(in, "%d", &A);
		for (i=0; i<A; i++)
		{
			fscanf(in, "%s %d", anl, &ca);
			for (j=0; j<ca; j++)
			{
				fscanf(in, "%s", attr[j]);
			}
			double ans = Cal();
			fprintf(out, "%.7lf\n", ans);
		}
		
	}

	return 0;
}