#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#include <stdio.h>

FILE *Fin = fopen("A-large.in","r");
//FILE *Fou = stdout;
FILE *Fou = fopen("a.out","w");

int n,m;
int p[2000][3];

int main()
{
	int i,j,k,caseN;
	fscanf(Fin,"%d",&caseN);
	for (int t=1; t<=caseN; t++)
	{
		fscanf(Fin,"%d",&n);
		int minx = 200000000, maxx = -100000000, miny = 200000000, maxy = -100000000;
		memset(p,0,sizeof(p));
		for (int i=0; i<n; i++)
		{
			char line[100];
			fscanf(Fin,"%d%d %s",p[i],p[i]+1,line);
			if (line[0]=='B'||line[0]=='b')
			{
				p[i][2] = 1;
				if (p[i][0]<minx) minx = p[i][0];
				if (p[i][0]>maxx) maxx = p[i][0];
				if (p[i][1]<miny) miny = p[i][1];
				if (p[i][1]>maxy) maxy = p[i][1];
			}
			else
			{
				p[i][2] = 0;
				fscanf(Fin,"%s",line);
			}
		}
		fscanf(Fin,"%d",&m);
		fprintf(Fou,"Case #%d:\n",t);
		for (int i=0; i<m; i++)
		{
			int x, y;
			fscanf(Fin,"%d%d",&x,&y);
			if (x>=minx&&x<=maxx&&y>=miny&&y<=maxy)
				fprintf(Fou,"BIRD\n");
			else
			{
				int minx1 = minx, maxx1 = maxx, miny1 = miny, maxy1 = maxy;
				if (x<minx1) minx1 = x;
				if (x>maxx1) maxx1 = x;
				if (y<miny1) miny1 = y;
				if (y>maxy1) maxy1 = y;
				bool okay = true;
				for (int j=0; j<n; j++)
					if (p[j][0]>=minx1&&p[j][0]<=maxx1 && p[j][1]>=miny1 && p[j][1]<=maxy1 && p[j][2] == 0)
					{
						okay = false;
						break;
					}
				if (!okay)
					fprintf(Fou,"NOT BIRD\n");
				else
					fprintf(Fou,"UNKNOWN\n");
			}
		}
	}
	return 0;
}
