#include <cstdio>
#include <cstring>
using namespace std;
char s[2][60][60];
int t,n,k;

bool pass(int x,int y)
{
	if (s[1][x][y]=='.') return false;
	bool b;
	if (y+k-1<n)
	{
		b=true;
		for (int i=1;i<=k && b;i++)
			if (s[1][x][y]!=s[1][x][y+i-1])
				b=false;
		if (b) return true;
	}

	if (x+k-1<n)
	{
		b=true;
		for (int i=1;i<=k && b;i++)
			if (s[1][x][y]!=s[1][x+i-1][y])
				b=false;
		if (b) return true;
	}

	if (x+k-1<n && y+k-1<n)
	{
		b=true;
		for (int i=1;i<=k && b;i++)
			if (s[1][x][y]!=s[1][x+i-1][y+i-1])
				b=false;
		if (b) return true;
	}

	if (x-k+1>=0 && y+k-1<n)
	{
		b=true;
		for (int i=1;i<=k && b;i++)
			if (s[1][x][y]!=s[1][x-i+1][y+i-1])
				b=false;
		if (b) return true;
	}

	return false;
}

int main()
{
	FILE *input=fopen("a.in","r");
	FILE *output=fopen("a.out","w");
	fscanf(input,"%d",&t);
	for (int t0=1;t0<=t;t0++)
	{
		fscanf(input,"%d%d",&n,&k);
		memset(s,0,sizeof(s));
		for (int i=0;i<n;i++)
			fscanf(input,"%s",s[0][i]);
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				s[1][j][n-1-i]=s[0][i][j];
		for (int i=0;i<n;i++)
		{
			int x=n-1;
			for (int j=n-1;j>=0;j--)
				if (s[1][j][i]!='.')
				{
					s[1][x][i]=s[1][j][i];
					x--;
				}
			for (int j=x;j>=0;j--)
				s[1][j][i]='.';
		}
		bool br=false,bb=false;
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				if (pass(i,j))
					if (s[1][i][j]=='R')
						br=true;
					else bb=true;
		if (br)
			if (bb)
				fprintf(output,"Case #%d: Both\n",t0);
			else fprintf(output,"Case #%d: Red\n",t0);
		else if (bb)
			fprintf(output,"Case #%d: Blue\n",t0);
		else fprintf(output,"Case #%d: Neither\n",t0);
	}
	fclose(input);
	fclose(output);
	return 0;
}