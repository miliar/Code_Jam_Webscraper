#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
	FILE	*fin,*fout;
	fin = fopen("\A-large.in","r");
	fout = fopen("\A-large.out","w");

int t,z,n,i,j,k,x;
	char map[60][60],g[60][60];
	fscanf(fin,"%d",&t);
	for (z = 1; z <= t; z++)
	{
		fscanf(fin,"%d%d\n",&n,&k);
		for (i = 0; i < n; i++)
			fscanf(fin,"%s",map[i]);
		memset(g,'.',sizeof(g));
		for (i = 0; i < n; i++)
		{
			for (x = 0, j = n-1; j >= 0; j--)
				if (map[i][j] != '.')
					g[i][x++] = map[i][j];
		}
		bool ans1, ans2;
		ans1 = ans2 = false;
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				for (x = 0; x < k; x++)
					if(! (j+x<n && g[i][j+x]=='R'))
						break;
				if (x == k)
					ans1 = true;

				for (x = 0; x < k; x++)
					if(! (i+x<n&& g[i+x][j]=='R'))
						break;
				if (x == k)
					ans1 = true;

				for (x = 0; x < k; x++)
					if(! (i+x<n && j+x<n && g[i+x][j+x]=='R'))
						break;
				if (x == k)
					ans1 = true;for (x = 0; x < k; x++)
					if(! (i-x<n && j+x<n && g[i-x][j+x]=='R'))
						break;
				if (x == k)
					ans1 = true;
				if (ans1)
					break;
			}
			if (ans1)
				break;
		}

		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				for (x = 0; x < k; x++)
					if(! (j+x<n && g[i][j+x]=='B'))
						break;
				if (x == k)
					ans2 = true;

				for (x = 0; x < k; x++)
					if(! (i+x<n&& g[i+x][j]=='B'))
						break;
				if (x == k)
					ans2 = true;

				for (x = 0; x < k; x++)
					if(! (i+x<n && j+x<n && g[i+x][j+x]=='B'))
						break;
				if (x == k)
					ans2 = true;for (x = 0; x < k; x++)
					if(! (i-x<n && j+x<n && g[i-x][j+x]=='B'))
						break;
				if (x == k)
					ans2 = true;
				if (ans2)
					break;
			}
			if (ans2)
				break;
		}
		fprintf(fout,"Case #%d: ",z);
		if (ans1 && ans2)
			fprintf(fout,"Both\n");
		else if (ans1)
			fprintf(fout,"Red\n");
		else if(ans2)
			fprintf(fout,"Blue\n");
		else
			fprintf(fout,"Neither\n");
	}
}
