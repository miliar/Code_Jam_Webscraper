#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

string res[100];
char letter = 'a' - 1;
int m[100][100];
int W, H;

char process(int y, int x)
{
	cout << "> " << y << " " << x << "\n";
	int n=m[y][x], w=m[y][x], e=m[y][x], s=m[y][x];
	if(y>0) n = m[y-1][x];
	if(x>0) w = m[y][x-1];
	if(x<W-1) e = m[y][x+1];
	if(y<H-1) s = m[y+1][x];

	int x1, y1;
	int mn = min(n, min(w, min(e, s)));
	if(m[y][x]<=mn) {letter+=1; res[y][x] = letter; cout << "min: " << y << ' ' << x << "\n";return letter; }
	if(mn==n) {x1=x;y1=y-1;}
	else if(mn==w) {x1=x-1;y1=y;}
	else if(mn==e) {x1=x+1;y1=y;}
	else if(mn==s) {x1=x;y1=y+1;}

	if(res[y1][x1]==' ') { res[y][x] = process(y1,x1); }
	else res[y][x] = res[y1][x1];
	return res[y][x];
	
}

int wmain(void)
{
	FILE* fin = fopen("A-small.in", "r");
	FILE* fout = fopen("out", "w");
	int n;
	fscanf(fin, "%d", &n);
	for(int i=0;i<n;++i)
	{
		letter = 'a'-1;
		fscanf(fin, "%d%d", &H, &W);
		string sw(W,' ');
		for(int i1=0;i1<H;++i1) res[i1] = sw;

		for(int j=0;j<H;++j)
			for(int k=0;k<W;++k)
				fscanf(fin, "%d", &m[j][k]); 

		for(int j=0;j<H;++j)
			for(int k=0;k<W;++k)
				if(res[j][k]==' ') res[j][k] = process(j,k);

		fprintf(fout, "Case #%d:\n", i+1);
		for(int j=0;j<H;++j)
		{
			for(int k=0;k<W;++k)
				fprintf(fout, "%c ", res[j][k]);
			fprintf(fout, "\n");
		}
		printf("Case #%d:\n", i+1);
		for(int j=0;j<H;++j)
		{
			for(int k=0;k<W;++k)
				printf("%c ", res[j][k]);
			printf("\n");
		}
	}
	fclose(fin);fclose(fout);
	return 0;
}

