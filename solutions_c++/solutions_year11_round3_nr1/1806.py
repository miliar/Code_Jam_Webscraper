#include <stdio.h>

void main()
{
	int n, m;
	int t;
	char **field;
	char c;
	FILE* input = fopen("input.in","r");
	FILE* output = fopen("output.out","w");
	fscanf(input,"%d",&t);
	for(int k=1;k<=t;k++)
	{
		fscanf(input, "%d",&n);
		fscanf(input, "%d",&m);
		field = new char*[n];
		for(int i=0;i<n;i++)
		{
			field[i] = new char[m];
			fscanf(input,"%c",&c);
			for(int j=0;j<m;j++)
				fscanf(input,"%c",&(field[i][j]));
		}
		bool impossible = false;
		for(int i=0;i<n && !impossible;i++)
		{
			for(int j=0;j<m && !impossible;j++)
			{
				if(field[i][j]=='#')
				{
					if(i+1<n && j+1<m)
					{
						if(field[i+1][j]=='#' && field[i][j+1]=='#' && field[i+1][j+1]=='#')
						{
							field[i][j] = '/';
							field[i][j+1] = '\\';
							field[i+1][j] = '\\';
							field[i+1][j+1] = '/';
						}
						else
						{
							impossible = true;
						}
					}
					else
					{
						impossible = true;
					}
				}
			}
		}
		fprintf(output,"Case #%d:\n",k);
		if(!impossible)
		{
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<m;j++)
					fprintf(output,"%c",field[i][j]);
				fprintf(output,"%c",'\n');
			}
		}
		else
		{
			fprintf(output,"Impossible\n",k);
		}
		for(int i=0;i<n;i++)
			delete[] field[i];
		delete[] field;
	}
	fclose(input);
	fclose(output);
}