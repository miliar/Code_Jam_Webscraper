#include <vector>
#include <algorithm>
using namespace std;
#include <stdio.h>
#include <string.h>

FILE *Fin = fopen("A-large.in","r");
FILE *Fou = fopen("a.out","w");
//FILE *Fin = stdin;
//FILE *Fou = stdout;

const int d[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};

int n,m;

struct Line
{
	int x1,y1,x2,y2;
	Line (int _x1, int _y1, int _x2, int _y2) : x1(_x1), y1(_y1), x2(_x2), y2(_y2) {}
	Line () {}
};
vector<Line> lines;

#define BASE 3500

int min1[7000], max1[7000];
int min2[7000], max2[7000];

int main()
{
	int i,j,k,caseN;
	fscanf(Fin,"%d",&caseN);
	for (int t=1; t<=caseN; t++)
	{
		fscanf(Fin,"%d",&n);
		int x,y; lines.clear();
		int K = 0; x=y=0;
		long long tot = 0;
		for (i=0; i<n; i++)
		{
			char line[1000]; int c;
			fscanf(Fin,"%s %d",line,&c);
			int len = strlen(line);
			for (j=0; j<c; j++)
			{
				for (k=0; k<len; k++)
					if (line[k]=='F')
					{
						lines.push_back(Line(x,y,x+d[K][0],y+d[K][1]));
						x += d[K][0], y += d[K][1];
					}
					else if (line[k]=='R')
						K = (K+1)%4;
					else if (line[k]=='L')
						K = (K+3)%4;
			}
		}
		for (i=0; i<lines.size(); i++)
			if (lines[i].y1==lines[i].y2)
				tot += (lines[i].x2-lines[i].x1) * (lines[i].y2);
		if (tot<0) tot = -tot;

		for (i=-3001; i<=3001; i++)
		{
			int min = 0x7FFFFFFF, max = -10000;
			//fprintf(stderr,"%d\n",i);
			for (j=0; j<lines.size(); j++)
				if (lines[j].y1>=i+1 && i>=lines[j].y2 ||lines[j].y2>=i+1 && i>=lines[j].y1 )
				{
					if (lines[j].x1<min) min = lines[j].x1;
					if (lines[j].x1>max) max = lines[j].x1;
				}
			min1[i+BASE] = min;
			max1[i+BASE] = max-1;
		}
		for (i=-3001; i<=3001; i++)
		{
			int min = 0x7FFFFFFF, max = -10000;
			for (j=0; j<lines.size(); j++)
				if (lines[j].x1>=i+1 && i>=lines[j].x2 ||lines[j].x2>=i+1 && i>=lines[j].x1 )
				{
					if (lines[j].y1<min) min = lines[j].y1;
					if (lines[j].y1>max) max = lines[j].y1;
				}
			min2[i+BASE] = min;
			max2[i+BASE] = max-1;
		}

		for (i=-3001; i<=3001; i++)
			for (j=-3001; j<=3001; j++)
				if ( j>=min1[BASE+i] && j<=max1[BASE+i] ||
					 i>=min2[BASE+j] && i<=max2[BASE+j] )
					tot--;

		fprintf(Fou,"Case #%d: %lld\n",t, -tot);
		printf("Case #%d: %lld\n",t, -tot);
	}
	return 0;
}

