#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

#include<memory.h>

using namespace std;

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");


	int T;

	fscanf(fp,"%d",&T);
	for(int t = 1; t<=T; t++)
	{
		char str[5][5];
		int n = 4;
		for(int i = 0; i<n; i++)
			fscanf(fp,"%s",&str[i]);
		bool notComplete = false;
		int won = 0;
		int element = 0;
		
		if(str[0][n-1] == '.'){element = -1; notComplete = true;}
		else if(str[0][n-1] == 'X')element = 1;
		else if(str[0][n-1] == 'O')element = 2;
		else element = 3;
		for(int i = 1; i<n; i++)
		{
			if(str[i][n-1-i] == 'X')
			{
				if(element == 2) {element = -1; break;}
				else element = 1;
			}
			else if(str[i][n-1-i] == 'O')
			{
				if(element == 1) {element = -1; break;}
				else element = 2;
			}
			else if(str[i][n-1-i] == '.')
			{
				element = -1;
				break;
			}
		}
		if(element != -1)
		{
			if(element == 1) fprintf(ofp, "Case #%d: X won\n",t);
			else fprintf(ofp, "Case #%d: O won\n",t);
			continue;
		}


		element = 0;
		if(str[0][0] == '.'){element = -1; notComplete = true;}
		else if(str[0][0] == 'X')element = 1;
		else if(str[0][0] == 'O')element = 2;
		else element = 3;
		for(int i = 1; i<n; i++)
		{
			if(str[i][i] == 'X')
			{
				if(element == 2) {element = -1; break;}
				else element = 1;
			}
			else if(str[i][i] == 'O')
			{
				if(element == 1) {element = -1; break;}
				else element = 2;
			}
			else if(str[i][i] == '.')
			{
				element = -1;
				break;
			}
		}
		if(element != -1)
		{
			if(element == 1) fprintf(ofp, "Case #%d: X won\n",t);
			else fprintf(ofp, "Case #%d: O won\n",t);
			continue;
		}

		element = 0;
		for(int i = 0; i<n; i++)
		{
			if(str[i][0] == '.'){element = -1; notComplete = true; continue;}
			else if(str[i][0] == 'X')element = 1;
			else if(str[i][0] == 'O')element = 2;
			else element = 3;
			for(int j = 1; j<n; j++)
			{
				if(str[i][j] == '.')
				{
					element = -1;
					notComplete = true;
				}
				if(element == -1)continue;
				else if(str[i][j] == 'X')
				{
					if(element == 2) element = -1;
					else element = 1;
				}
				else if(str[i][j] == 'O')
				{
					if(element == 1) element = -1;
					else element = 2;
				}
			}
			if(element != -1)break;
		}
		if(element != -1)
		{
			if(element == 1) fprintf(ofp, "Case #%d: X won\n",t);
			else fprintf(ofp, "Case #%d: O won\n",t);
			continue;
		}

		element = 0;
		for(int i = 0; i<n; i++)
		{
			if(str[0][i] == '.'){element = -1; notComplete = true; continue;}
			else if(str[0][i] == 'X')element = 1;
			else if(str[0][i] == 'O')element = 2;
			else element = 3;
			for(int j = 1; j<n; j++)
			{
				if(str[j][i] == '.')
				{
					element = -1;
					notComplete = true;
					break;
				}
				else if(str[j][i] == 'X')
				{
					if(element == 2) {element = -1; break;}
					else element = 1;
				}
				else if(str[j][i] == 'O')
				{
					if(element == 1) {element = -1; break;}
					else element = 2;
				}
			}
			if(element != -1)break;
		}
		if(element != -1)
		{
			if(element == 1) fprintf(ofp, "Case #%d: X won\n",t);
			else fprintf(ofp, "Case #%d: O won\n",t);
			continue;
		}

		if(notComplete) fprintf(ofp, "Case #%d: Game has not completed\n",t);
		else fprintf(ofp, "Case #%d: Draw\n",t);
	
	}
	
	return 0;
}