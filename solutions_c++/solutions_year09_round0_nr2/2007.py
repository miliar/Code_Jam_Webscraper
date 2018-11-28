#include<stdio.h>

FILE *fin, *fout;

int h,w, m[101][101];
char b[101][101], urm;

char cauta(int i, int j)
{
	int min = m[i][j], l, c;
	if(b[i][j]!=0) return b[i][j];
	if(i>1 && m[i-1][j]<min)
	{
		min = m[i-1][j];
		l=i-1;
		c=j;
	}
	if(j>1 && m[i][j-1]<min)
	{
		min = m[i][j-1];
		l=i;
		c=j-1;
	}if(j<w && m[i][j+1]<min)
	{
		min = m[i][j+1];
		l=i;
		c=j+1;
	}
	if(i<h && m[i+1][j]<min)
	{
		min = m[i+1][j];
		l=i+1;
		c=j;
	}
	if(min == m[i][j]) 
	{
		b[i][j] = urm;
		urm++;
		return urm-1;
	}
	b[l][c] = cauta(l,c);
	return b[l][c];
}

int main()
{
    int n, i, j, t;
    fin = fopen("date.in", "rt");
    fout = fopen("date.out", "wt");
    fscanf(fin,"%i",&n);
    for(t=1; t<=n; t++)
	{
		fscanf(fin, "%i %i", &h, &w);
		for(i=1; i<=h; i++)
			for(j=1; j<=w; j++)
			{
				fscanf(fin, "%i", &(m[i][j]));
				b[i][j] = 0;
			}
		urm = 'a';
		for(i=1; i<=h; i++)
			for(j=1; j<=w; j++)
				if(b[i][j]==0) b[i][j] = cauta(i,j);
		fprintf(fout, "Case #%i:\n", t);
		for(i=1; i<=h; i++)
		{
			for(j=1; j<=w; j++) fprintf(fout, "%c ", b[i][j]);
			fprintf(fout, "\n");
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
		
			
		
	
		
