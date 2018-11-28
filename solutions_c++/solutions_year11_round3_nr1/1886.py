#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <map>
#include <set>
using namespace std;

#define MAX_BUF_SIZE 40960

int  main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "Usage:command.exe infile outfile" << endl;
		exit(1);
	}
	FILE* in = fopen(argv[1], "r");
	if (!in)
	{
		cout << "cannot open infile" << endl;
		exit(1);
	}
	FILE* out = fopen(argv[2], "w");
	if (!out)
	{
		cout << "cannot open outfile" << endl;
		exit(1);
	}
	char buf[MAX_BUF_SIZE];
	fgets(buf, MAX_BUF_SIZE, in);
	long long count = 0;
	while (fgets(buf, MAX_BUF_SIZE, in))
	{
		count ++;
		printf("\r%d", count);
		char* toke = strtok(buf, " \n");
		int m = atoi(toke);
		toke = strtok(NULL, " \n");
		int n = atoi(toke);
		char** a = new char*[m];
		for (int i = 0; i < m; i++)
		{
			a[i] = new char[n];
		}
		for (int i = 0; i < m; i++)
		{
			fgets(buf, MAX_BUF_SIZE, in);
			for (int j = 0; j < n; j++)
			{
				a[i][j] = buf[j];
			}
		}
		
		for (int i = 0; i < m-1; i++)
		{
			for (int j = 0; j < n-1; j++)
			{
				if (a[i][j] == '#' && a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#')
				{
					a[i][j] = '/';
					a[i][j+1] = '\\';
					a[i+1][j] = '\\';
					a[i+1][j+1] = '/';
				}
			}
		}
		int flag = 0;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] == '#')
				{
					flag = 1;
					break;
				}
			}
			if (flag)
			{
				break;
			}
		}
		if (flag == 1)
		{
			fprintf(out, "Case #%d:\nImpossible\n", count);
		}
		else
		{
			fprintf(out, "Case #%d:\n", count);
			for (int i = 0; i < m; i++)
			{
				for (int j = 0; j < n; j++)
				{
					fprintf(out, "%c", a[i][j]);
				}
				fprintf(out,"\n");
			}
		}
		
		for (int i = 0; i < m; i++)
		{
			delete[] a[i];
		}
		delete[] a;
		
	}
	fclose(in);
	fclose(out);
}